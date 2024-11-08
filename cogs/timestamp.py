import discord
from discord import app_commands
from discord.ext import commands
import logging
import datetime

logger = logging.getLogger(__name__)

class TimestampCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="timestamp",
        description="Generate a timestamp for a specified date, time, and format.",
    )
    async def timestamp(
        self,
        interaction: discord.Interaction,
        time: str = None,
        format: str = "full",
        date: str = None,
    ):
        """Generates a Discord timestamp for the specified time, date, and format."""
        try:
            # Default to the current date
            current_date = datetime.datetime.utcnow().date()
            
            # Parse the date, if provided
            if date:
                try:
                    year, month, day = map(int, date.split("-"))
                    custom_date = datetime.date(year, month, day)
                    current_date = custom_date  # Use the custom date if provided
                except ValueError:
                    await interaction.response.send_message("Invalid date format. Please use `YYYY-MM-DD` format.")
                    return

            # Parse time, handling midnight and other cases
            if time:
                try:
                    hour, minute = map(int, time.split(":"))

                    # Adjust if time is exactly at midnight
                    custom_time = datetime.datetime.combine(current_date, datetime.time(hour, minute))
                except ValueError:
                    await interaction.response.send_message("Invalid time format. Please use `HH:MM` format.")
                    return
            else:
                # Default to the current time in UTC
                custom_time = datetime.datetime.combine(current_date, datetime.datetime.utcnow().time())

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

            if format.lower() not in formats:
                format_list = "\n".join([f"`{key}`: {desc}" for key, desc in formats.items()])
                await interaction.response.send_message(f"Available formats:\n{format_list}\n\nPlease choose one of the formats listed.")
                return

            # Get the formatted timestamp or default to full if invalid
            timestamp_message = formats.get(format.lower(), formats["full"])

            # Send the formatted timestamp
            await interaction.response.send_message(f"{timestamp_message}")

            # Log successful execution
            logger.info(f"Timestamp command executed at time: {time if time else 'current time'}, date: {date if date else 'current date'}, format: {format}")

        except Exception as e:
            await interaction.response.send_message("An error occurred while processing the timestamp command.")
            logger.error(f"Failed to execute timestamp command: {e}")

async def setup(bot):
    await bot.add_cog(TimestampCog(bot))
