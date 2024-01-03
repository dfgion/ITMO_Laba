import sys

import flet as ft

sys.path.append(r"C:\Users\Даниил\Desktop\laba_for_programming")
from app.controls.bans import BansPage
from app.controls.database import DatabasePage
from app.controls.home import HomeOption


class ITMOLogo(ft.UserControl):
    async def animate(self, e):
        e.control.border = ft.Border()

    def build(self):
        return ft.Container(
            content=ft.Image(src=r"app\assets\images\label.png", width=200, height=200),
            on_hover=self.animate,
        )


class Points(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    async def animate(self, e):
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
        bans = (
            self.page.controls[0]
            .controls[0]
            .content.controls[1]
            .controls[1]
            .controls[2]
            .controls[0]
        )
        if e.control.text == "| HOME":
            # move database up animation
            database.offset = ft.transform.Offset(0, -2)
            await database.update_async()

            # move bans up animation
            bans.offset = ft.transform.Offset(0, -2)
            await bans.update_async()

            # show home animation
            home.offset = ft.transform.Offset(0, 0)
            await home.update_async()

        elif e.control.text == "| DATABASE":
            # move home up animation
            home.offset = ft.transform.Offset(0, -2)
            await home.update_async()

            # move bans up animation
            bans.offset = ft.transform.Offset(0, -2)
            await bans.update_async()

            # show database animation
            database.offset = ft.transform.Offset(0, 0)
            await database.update_async()

        elif e.control.text == "| BANS":
            # move database up animation
            database.offset = ft.transform.Offset(0, -2)
            await database.update_async()

            # move bans up animation
            home.offset = ft.transform.Offset(0, -2)
            await home.update_async()

            # show bans animation
            bans.offset = ft.transform.Offset(0, 0)
            await bans.update_async()

    def build(self):
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
                    ft.ElevatedButton(
                        icon=ft.icons.SCREEN_LOCK_LANDSCAPE,
                        text="| BANS",
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
    def __init__(self, page):
        super().__init__()
        self.page = page

    async def switch_theme(self, e):
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT

        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.page.controls[0].controls[0].content.controls[0].controls[
                0
            ].src = r"app\assets\images\black_background.gif"
        else:
            self.page.controls[0].controls[0].content.controls[0].controls[
                0
            ].src = r"app\assets\images\white_background.gif"

        await self.page.controls[0].controls[0].content.controls[0].controls[
            0
        ].update_async()

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
        await self.page.controls[0].controls[0].content.controls[1].controls[
            0
        ].controls[0].content.controls[1].controls[0].content.update_async()

        await self.page.update_async()

    def build(self):
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
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[ITMOLogo(), Points(page=self.page), Theme(page=self.page)],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            width=200,
            height=750,
            opacity=0.8,
            bgcolor="grey",
        )


class BackgroundImage(ft.UserControl):
    def build(self):
        return ft.Image(
            src=r"app\assets\images\black_background.gif",
            width=1000,
            height=750,
            fit="fill",
        )


class MainPage(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.home = HomeOption(page=self.page)
        self.database = DatabasePage(page=self.page)
        self.bans = BansPage(page=self.page)

    def build(self):
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
            width=1000,
            height=750,
            bgcolor="transparent",
            opacity=1,
            border_radius=20,
        )


async def gui(page: ft.Page):
    page.padding = 0
    page.title = "ITMO Administrator"
    page.window_maximizable = False

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1100
    page.window_height = 900
    page.window_resizable = False
    await page.add_async(MainPage(page=page))


if __name__ == "__main__":
    ft.app(target=gui, assets_dir=r"app\assets")
