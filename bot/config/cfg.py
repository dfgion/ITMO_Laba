import os

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"")

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()


async def set_commands(bot: Bot):
    commands = [BotCommand(command="/start", description="Начало работы")]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
