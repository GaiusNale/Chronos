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
        date: str = None,
    ):
        """Generates a Discord timestamp for the specified timezone, time, date, and format."""
        try:
            # Validate and set the timezone
            timezone = pytz.timezone(tz)

            # Default to the current date
            current_date = datetime.datetime.now(timezone).date()
            
            # Parse the date, if provided
            if date:
                try:
                    year, month, day = map(int, date.split("-"))
                    
                    # If the day is greater than 1, subtract one day to adjust
                    if day >1:
                        custom_date = datetime.date(year, month, day)
                    else:
                        custom_date = datetime.date(year, month, day = 1 )  # For some reason this lets the program function please don't ask 
                    
                    # Set current_date to the potentially adjusted custom date
                    current_date = custom_date
                except ValueError:
                    await interaction.response.send_message("Invalid date format. Please use `YYYY-MM-DD` format.")
                    return

            # Parse time, subtracting one hour as needed
            if time:
                try:
                    hour, minute = map(int, time.split(":"))
                    hour = (hour - 1) % 24  # Manual hour adjustment
                    custom_time = datetime.datetime.combine(current_date, datetime.time(hour, minute))
                    custom_time = timezone.localize(custom_time)  # Localize to timezone
                except ValueError:
                    await interaction.response.send_message("Invalid time format. Please use `HH:MM` format.")
                    return
            else:
                # Default to the current time
                custom_time = datetime.datetime.combine(current_date, datetime.datetime.now(timezone).time())
                custom_time = timezone.localize(custom_time)

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
            logger.info(f"Timestamp command executed for timezone: {tz} at time: {time if time else 'current time'}, date: {date if date else 'current date'}, format: {format}")

        except pytz.UnknownTimeZoneError:
            await interaction.response.send_message("Unknown timezone. Please provide a valid timezone.")
            logger.error(f"Invalid timezone specified: {tz}")
        except Exception as e:
            await interaction.response.send_message("An error occurred while processing the timestamp command.")
            logger.error(f"Failed to execute timestamp command: {e}")

async def setup(bot):
    await bot.add_cog(TimestampCog(bot))

# test to see if the branch is active
