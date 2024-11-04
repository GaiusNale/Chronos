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
    async def timestamp(self, interaction: discord.Interaction, tz: str = 'UTC'):
        """Generates a Discord timestamp for the specified timezone."""
        try:
            timezone = pytz.timezone(tz)
            current_time = datetime.datetime.now(timezone)
            unix_timestamp = int(current_time.timestamp())
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
