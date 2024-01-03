import flet as ft
from app.controls.registration import SingInPage
from bot.run import run_bot
import asyncio


    
async def gui(page: ft.Page):
    page.padding = 0
    page.title = 'ITMO Administrator'
    page.window_maximizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 700
    page.window_height = 900
    page.window_resizable = False
    await page.add_async(SingInPage(page=page))

async def main():
    task_app = asyncio.create_task(ft.app_async(target=gui, assets_dir=r'app\assets'))
    task_telegram = asyncio.create_task(run_bot())
    await task_app
    await task_telegram


if __name__ == "__main__":
    asyncio.run(main())