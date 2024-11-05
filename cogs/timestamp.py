# timestamp.py
import discord
from discord import app_commands
from discord.ext import commands
import logging
import datetime
import pytz

logger = logging.getLogger(__name__)


class TimestampCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="timestamp",
        description="Generate a timestamp in the specified timezone, time, and format.",
    )
    async def timestamp(
        self,
        interaction: discord.Interaction,
        tz: str = "UTC",
        time: str = None,
        format: str = "full",
    ):
        """Generates a Discord timestamp for the specified timezone, time, and format."""
        try:
            # Validate and set the timezone
            timezone = pytz.timezone(tz)

            # Get the current date and use it as a base
            current_date = datetime.datetime.now(timezone).date()

            # If time is specified, parse it; otherwise, use the current time
            if time:
                try:
                    # Parse the time argument in HH:MM format
                    hour, minute = map(int, time.split(":"))

                    hour = (hour - 1) % 24
                    custom_time = datetime.datetime.combine(
                        current_date, datetime.time(hour, minute)
                    )
                    custom_time = timezone.localize(
                        custom_time
                    )  # Localize to the specified timezone

                except ValueError:
                    await interaction.response.send_message(
                        "Invalid time format. Please use `HH:MM` format."
                    )
                    return
            else:
                # Default to the current time in the specified timezone
                custom_time = datetime.datetime.now(timezone)

            # Convert to Unix timestamp
            unix_timestamp = int(custom_time.timestamp())

            # Define format options for Discord timestamp
            formats = {
                "full": f"<t:{unix_timestamp}:F>",  # Full date and time
                "short": f"<t:{unix_timestamp}:f>",  # Short date and time
                "relative": f"<t:{unix_timestamp}:R>",  # Relative time
                "date": f"<t:{unix_timestamp}:D>",  # Date only
                "time": f"<t:{unix_timestamp}:t>",  # Time only
            }

            # Get the formatted timestamp or default to full if invalid
            timestamp_message = formats.get(format.lower(), formats["full"])

            # Send the formatted timestamp
            await interaction.response.send_message(
                f"{timestamp_message} in {tz} timezone"
            )

            # Log successful execution
            logger.info(
                f"Timestamp command executed for timezone: {tz} at time: {time if time else 'current time'}, format: {format}"
            )
        except pytz.UnknownTimeZoneError:
            await interaction.response.send_message(
                "Unknown timezone. Please provide a valid timezone."
            )
            logger.error(f"Invalid timezone specified: {tz}")
        except Exception as e:
            await interaction.response.send_message(
                "An error occurred while processing the timestamp command."
            )
            logger.error(f"Failed to execute timestamp command: {e}")


async def setup(bot):
    await bot.add_cog(TimestampCog(bot))
