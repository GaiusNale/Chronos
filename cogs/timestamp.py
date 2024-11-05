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

    @app_commands.command(name="timestamp", description="Generate a timestamp in the specified timezone.")
    async def timestamp(self, interaction: discord.Interaction, tz: str = 'UTC' , time: str = None):
        """Generates a Discord timestamp for the specified timezone."""
        try:
            # this gets the current date and uses as a base for the user to be able to pick a time (will edit this later to add date functionality as well)
            timezone = pytz.timezone(tz)
            current_date = datetime.datetime.now(timezone).date()

            if time:
                try:
                    # This collects the time argument in HH:MM
                    hour, minute = map(int, time.split(":"))
                    custom_time = datetime.datetime.combine(current_date, datetime.time(hour,minute))
                    custom_time = timezone.localize(custom_time) # this localizes the time to the current time zone
                
                except ValueError:
                    await interaction.response.send_message("That's an invalid time format you should use the HH:MM format")
                    return
            else: 
                # If no input is given for the specific this defaults back to geting the current time 
                custom_time = datetime.datetime.now

            unix_timestamp = int(custom_time.timestamp())
            await interaction.response.send_message(f"<t:{unix_timestamp}:F> in {tz} timezone")
            logger.info(f"Timestamp command executed for timezone: {tz}")
        except pytz.UnknownTimeZoneError:
            await interaction.response.send_message("Unknown timezone. Please provide a valid timezone.")
            logger.error(f"Invalid timezone specified: {tz}")
        except Exception as e:
            await interaction.response.send_message("An error occurred while processing the timestamp command.")
            logger.error(f"Failed to execute timestamp command: {e}")

async def setup(bot):
    await bot.add_cog(TimestampCog(bot))
