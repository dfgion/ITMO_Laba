import flet as ft

animate = ft.AnimationCurve.ELASTIC_IN_OUT


class DatabasePage(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=ft.Row(controls=[]),
            height=750,
            width=800,
            border_radius=20,
            opacity=1,
            bgcolor="blue",
            disabled=True,
            visible=True,
            animate_offset=ft.animation.Animation(600, animate),
            offset=ft.transform.Offset(0, -2),
            # on_animation_end=self.end
        )


class HomeOption(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            height=750,
            width=800,
            border_radius=20,
            opacity=1,
            bgcolor="purple",
            disabled=False,
            visible=True,
            animate_offset=ft.animation.Animation(600, animate),
            offset=ft.transform.Offset(0, -2),
            # on_animation_end=self.end
        )


class ITMOLogo(ft.UserControl):
    def build(self):
        return ft.Image(
            src=r"app\assets\images\label.png",
            width=200,
            height=200,
        )


class Points(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    async def animate(self, e):
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
            database.offset = ft.transform.Offset(0, -2)
            await database.update_async()

            home.offset = ft.transform.Offset(0, 0)
            await home.update_async()

        elif e.control.text == "| DATABASE":
            home.offset = ft.transform.Offset(0, -2)
            await home.update_async()

            database.offset = ft.transform.Offset(0, 0)
            await database.update_async()

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
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.page.controls[0].controls[0].content.controls[0].controls[0].src = (
            r"app\assets\images\black_background.gif"
            if self.page.theme_mode == ft.ThemeMode.DARK
            else r"app\assets\images\white_background.gif"
        )
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

    def build(self):
        return ft.Container(
            content=ft.Stack(
                controls=[
                    BackgroundImage(),
                    ft.Row(
                        controls=[
                            Navigation(page=self.page),
                            ft.Stack(
                                controls=[self.home, self.database],
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
