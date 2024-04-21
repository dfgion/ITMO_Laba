import asyncio
import datetime

import flet as ft

from app.controls.registration import SingInPage
from bot.bot_run import run_bot
from app.app_run import run_app


async def main():
    task_app = asyncio.create_task(ft.app_async(target=run_app, assets_dir=r"app\assets"))
    asyncio.create_task(run_bot())
    await task_app


if __name__ == "__main__":
    asyncio.run(main())
