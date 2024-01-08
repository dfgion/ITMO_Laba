import flet as ft
import re

from app.controls.registration import SingInPage

async def run_app(page: ft.Page):
    page.padding = 0
    page.title = "ITMO Administrator"
    page.window_maximizable = False
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 700
    page.window_height = 900
    page.window_resizable = False
    await page.add_async(SingInPage(page=page))
    print('Приложение запущено')