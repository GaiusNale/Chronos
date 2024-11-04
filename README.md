
# NorahBot

NorahBot is a versatile Discord bot designed to enhance server management and user interaction. It offers features like user moderation, fun commands, and integrations with popular APIs such as OpenAI and weather services. This bot is part of my portfolio, showcasing my skills in Python, API integration, and bot development.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Environment Setup](#environment-setup)
3. [Running the Bot](#running-the-bot)
4. [Directory Overview](#directory-overview)
5. [Additional Resources](#additional-resources)
6. [Contact](#contact)

## Project Structure

NorahBot is organized into the following directories:

- **/cogs/**: Contains all command logic and modular bot functionality.
  - `example_cog.py`: An example of a command cog that handles user commands.
- **/dbs/**: Manages database schemas and static JSON files used across the bot.
  - `schema.py`: Defines the MongoDB schema and interaction logic.
  - **/dbs/statics/**: Stores static databases referenced in cogs.
- **/logs/**: Handles logging configuration and storage.
  - `log_config.py`: Configures logging for the bot.
- **/modules/**: Contains reusable modules such as API clients and background tasks.
  - `api.py`: Manages external API calls.

## Environment Setup

To run NorahBot, you'll need to create a `.env` file in the root directory with the following variables:

```
DB_NAME=your_database_name
DB_USERNAME=your_database_username
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
DISCORD_TOKEN=your_discord_token
ADMIN_ID=your_discord_admin_id
OPENAI_KEY=your_openai_api_key
DISCORD_CLIENT_ID=your_discord_client_id
DISCORD_CLIENT_SECRET=your_discord_client_secret
DISCORD_REDIRECT_URI=your_discord_redirect_uri
MONGO_ENCRYPT=your_mongodb_encryption_key
MONGO_SIGN=your_mongodb_signing_key
MONGO_URI=your_mongodb_connection_uri
```

**Note:** Keep this file secure and never commit it to version control.

## Running the Bot

To run the bot locally for testing, you can enter this into your terminal:

```bash
python norahbot.py
```

For production, it is recommended to deploy the bot on a server with the appropriate environment variables set.

For testing purposes, it is recommended to create a separate Discord bot application. Configure this test bot in your local `.env` file to avoid disruptions to your main bot.

## Directory Overview

Here's a brief overview of the key directories in the project:
- **/cogs/**: This directory houses all the logic for the bot's commands.
- **/dbs/**: Manages the MongoDB schema and other static databases.
  - **/dbs/statics/**: Contains JSON files used by the cogs for static data.
- **/logs/**: Stores log files and handles logging configuration.
- **/modules/**: Stores non-cog classes and functions used across the bot, like API integrations.

## Additional Resources

**Project Documentation:**
- **8/21/2024:** 190200 - Created the README.md and structured the repository appropriately for modular application development.
- **8/23/2024:** 175505 - Implemented MongoDB integration with the creation of the `dbs/schema.py` file, defining the `Ticket` document schema. Developed three cogs (`create_ticket.py`, `view_tickets.py`, and `close_ticket.py`) with detailed documentation and command functionality, including app commands for ticket management within the Discord bot.
- **8/23/2024** 183455 - Implemented logging with the creation of 'log_config.py', defining the logging mechanism and storing the logs in 'app.log' written in the '/logs/' directory.
- **8/24/2024** 222802 - Created 'reminder.py' to create a reminder based on a timer input and message, as well as integrated security features.

## Contact

For any questions or feedback, feel free to reach out:
- **Discord:** norahlia
- **GitHub:** [norahlia](https://github.com/norahlia)
