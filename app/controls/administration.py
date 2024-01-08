import sys

import flet as ft

sys.path.append(r"C:\Users\Даниил\Desktop\programming")
from app.controls.bans import BansPage
from app.controls.database import DatabasePage
from app.controls.home import HomePage

from bot.config.cfg import bot


class ITMOLogo(ft.UserControl):
    def __init__(self, page) -> None:
        super().__init__()
        self.page = page
        
    async def animate(self, e) -> None:
        e.control.content.scale = 1.3 if e.control.content.scale == 1 else 1
        await self.update_async()

    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.Image(src=r"app\assets\images\label.png", 
                             width=200, 
                             height=200, 
                             scale=1, 
                             animate_scale=ft.animation.Animation(duration=1000, curve=ft.AnimationCurve.EASE_IN)
                             ),
            on_hover=self.animate,
            border_radius=20,
            width=200,
            height=200
            )


class Points(ft.UserControl):
    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    async def animate(self, e) -> None:
        # JSON MAGIC IN FLET??!111!
        home = (
            self.page.controls[0]
            .controls[0]
            .content.controls[1]
            .controls[1]
            .controls[0]
            .controls[0]
        )
        database = (
            self.page.controls[0]
            .controls[0]
            .content.controls[1]
            .controls[1]
            .controls[1]
            .controls[0]
        )
        if e.control.text == "| HOME":
            # move database up animation
            database.offset = ft.transform.Offset(0, -2)
            await database.update_async()

            # show home animation
            home.offset = ft.transform.Offset(0, 0)
            await home.update_async()

        elif e.control.text == "| DATABASE":
            # move home up animation
            home.offset = ft.transform.Offset(0, -2)
            await home.update_async()

            # show database animation
            database.offset = ft.transform.Offset(0, 0)
            await database.update_async()

    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton(
                        icon=ft.icons.HOME,
                        text="| HOME",
                        width=200,
                        height=100,
                        color="white",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=15),
                        ),
                        on_click=self.animate,
                    ),
                    ft.ElevatedButton(
                        icon=ft.icons.DATASET,
                        text="| DATABASE",
                        width=200,
                        height=100,
                        color="white",
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=15),
                        ),
                        on_click=self.animate,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
            width=200,
            height=450,
            margin=ft.margin.only(left=5, right=5),
            bgcolor="transparent",
        )


class Theme(ft.UserControl):
    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    async def switch_theme(self, e) -> None:
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT

        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.controls[0].controls[0].content.controls[0].controls[0].src = r"app\assets\images\black_background.gif"
        else:
            self.page.controls[0].controls[0].content.controls[0].controls[0].src = r"app\assets\images\white_background.gif"

        await self.page.controls[0].controls[0].content.controls[0].controls[0].update_async()

        e.control.text = (
            "| Light" if self.page.theme_mode == ft.ThemeMode.DARK else "| Dark"
        )
        e.control.color = (
            "white" if self.page.theme_mode == ft.ThemeMode.DARK else "black"
        )
        e.control.icon = (
            ft.icons.SUNNY
            if self.page.theme_mode == ft.ThemeMode.DARK
            else ft.icons.MODE_NIGHT
        )
        e.control.icon_color = (
            "white" if self.page.theme_mode == ft.ThemeMode.DARK else "black"
        )
        await self.update_async()

        for button in (
            self.page.controls[0]
            .controls[0]
            .content.controls[1]
            .controls[0]
            .controls[0]
            .content.controls[1]
            .controls[0]
            .content.controls
        ):
            button.color = (
                "white" if self.page.theme_mode == ft.ThemeMode.DARK else "black"
            )
            e.control.icon_color = (
                "white" if self.page.theme_mode == ft.ThemeMode.DARK else "black"
            )
        await self.page.controls[0].controls[0].content.controls[1].controls[0].controls[0].content.controls[1].controls[0].content.update_async()
        home_image = self.page.controls[0].controls[0].content.controls[1].controls[1].controls[0].controls[0].content.controls[0].controls[0]
        home_block = self.page.controls[0].controls[0].content.controls[1].controls[1].controls[0].controls[0].content.controls[1].controls[0]
        home_image.bgcolor = ft.colors.GREY_400 if self.page.theme_mode == ft.ThemeMode.LIGHT else 'black'
        home_block.border.top.color = ft.colors.GREY_400 if self.page.theme_mode == ft.ThemeMode.LIGHT else 'black'
        home_block.border.bottom.color = ft.colors.GREY_400 if self.page.theme_mode == ft.ThemeMode.LIGHT else 'black'
        home_block.border.left.color = ft.colors.GREY_400 if self.page.theme_mode == ft.ThemeMode.LIGHT else 'black'
        home_block.border.right.color = ft.colors.GREY_400 if self.page.theme_mode == ft.ThemeMode.LIGHT else 'black'
        await home_image.update_async()
        await home_block.update_async()
        
        await self.page.update_async()

    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.ElevatedButton(
                icon=ft.icons.SUNNY,
                on_click=self.switch_theme,
                width=150,
                height=50,
                text="| Light",
                icon_color="white",
                color="white",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=15),
                    shadow_color={ft.MaterialState.DEFAULT: "white"},
                ),
            ),
            alignment=ft.Alignment(0, 0),
            width=200,
            height=100,
        )


class Navigation(ft.UserControl):
    def __init__(self, page) -> None:
        super().__init__()
        self.page = page

    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                controls=[
                    ITMOLogo(page=self.page), 
                    Points(page=self.page), 
                    Theme(page=self.page)
                    ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            width=200,
            height=750,
            opacity=0.8,
            bgcolor="grey",
        )


class BackgroundImage(ft.UserControl):
    def build(self) -> ft.Image:
        return ft.Image(
            src=r"app\assets\images\black_background.gif",
            width=1000,
            height=750,
            fit="fill",
        )


class MainPage(ft.UserControl):
    def __init__(self, page, nickname) -> None:
        super().__init__()
        self.page = page
        self.home = HomePage(page=self.page, nickname = nickname)
        self.database = DatabasePage(page=self.page)
        self.bans = BansPage(page=self.page)

    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.Stack(
                        controls=[
                            BackgroundImage(),
                            ft.Row(
                                controls=[
                                    Navigation(page=self.page),
                                    ft.Stack(
                                        controls=[self.home, self.database, self.bans],
                                        width=800,
                                        height=750,
                                        ),
                                    ],
                                alignment=ft.MainAxisAlignment.START,
                                ),
                            ]
                        ),
            disabled=False,
            width=1000,
            height=750,
            bgcolor="transparent",
            opacity=1,
            border_radius=20,
        )


async def gui(page: ft.Page) -> None:
    page.padding = 0
    page.title = "ITMO Administrator"
    page.window_maximizable = False

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1100
    page.window_height = 900
    page.window_resizable = False
    await page.add_async(MainPage(page=page, nickname='Даниил'))


if __name__ == "__main__":
    ft.app(target=gui, assets_dir=r"app\assets")
