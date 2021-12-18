import logging
from aiogram import executor

import bot


"""enables logging info for aiogram lib"""
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    """
    starts listening to the telegram bot API.
    skip_updates set to true because aiogram updating is not working properly."""
    executor.start_polling(bot.dp, skip_updates=True)
