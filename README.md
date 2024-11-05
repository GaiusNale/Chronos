# Timestamp Bot

A Discord bot that generates customizable, timezone-aware timestamps that automatically display in each user’s local time. Users can specify a timezone, time, and format for the timestamp.
Still a work in progress 

## Features

- Generate timestamps in various formats (full date, short date, time only, etc.).
- Specify a custom timezone.
- Optionally choose a specific time in `HH:MM` format.
- Outputs timestamps in a format compatible with Discord’s automatic timezone display.

## Setup

### Requirements

- Python 3.8+
- `discord.py` library
- `pytz` library for timezone support
- A `.env` file to securely store your Discord bot token

### Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/timestamp-bot.git
    cd timestamp-bot
    ```

2. Install the dependencies:
    ```bash
    pip install discord.py pytz python-dotenv
    ```

3. Create a `.env` file in the project directory and add your bot token:
    ```env
    DISCORD_TOKEN=your_discord_bot_token_here
    ```

4. Run the bot:
    ```bash
    python main.py
    ```

## Usage

### Available Commands

#### `/timestamp`
Generates a timestamp based on the specified timezone, time, and format.

- **Arguments:**
  - `tz` *(str)*: The timezone for the timestamp (default: `UTC`).
  - `time` *(str)*: (Optional) Time in `HH:MM` format. If omitted, the current time in the specified timezone is used.
  - `format` *(str)*: (Optional) Display format for the timestamp. Options are:
    - `full`: Full date and time (e.g., January 1, 2023, 1:00 PM)
    - `short`: Short date and time (e.g., Jan 1, 2023, 1:00 PM)
    - `relative`: Relative time (e.g., "in 3 days" or "2 hours ago")
    - `date`: Date only (e.g., January 1, 2023)
    - `time`: Time only (e.g., 1:00 PM)

- **Examples**:
  - `/timestamp tz=UTC time=12:30 format=full`
  - `/timestamp tz=EST format=relative`

### Notes

- Discord’s timestamp formatting automatically adjusts to the local timezone of the viewer.
- For a full list of timezones, refer to [pytz documentation](https://pythonhosted.org/pytz/).

## License

MIT License

---

This README provides a simple guide to setting up and using your bot, along with some usage examples and available format options. Let me know if you'd like to add more details!