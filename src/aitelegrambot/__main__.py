from aitelegrambot.bot import TelegramBot
from dotenv import load_dotenv
import logging
import os


def main():
    load_dotenv()

    # Setup logging
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)

    # Check if the token has been given.
    required_values = [
        "TELEGRAM_BOT_TOKEN",
    ]
    missing_values = [
        value for value in required_values if os.environ.get(value) is None
    ]
    if len(missing_values) > 0:
        logging.error(
            f'The following environment values are missing in your .env: {", ".join(missing_values)}'
        )
        exit()

    # Run the bot.
    bot = TelegramBot(
        ollama_host=os.environ.get("OLLAMA_HOST", "localhost:11434"),
        bot_token=os.environ["TELEGRAM_BOT_TOKEN"],
        default_model=os.environ.get("DEFAULT_MODEL", "tusharhero/rationalai"),
    )

    bot.run()


if __name__ == "__main__":
    main()
