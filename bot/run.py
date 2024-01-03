import asyncio

from bot.config.cfg import bot, dp, set_commands
from bot.core.handlers import basic


async def on_startup(dispatcher):
    print("Бот Запущен")


async def run_bot() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await set_commands(bot)
    dp.include_router(basic.router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(run_bot())
