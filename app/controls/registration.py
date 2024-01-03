import asyncio

import flet as ft

from app.controls.administration import MainPage
from app.utils.cipher import cipher

ft.animation.AnimationCurve


class SignInText(ft.UserControl):
    async def animate(self, e):
        e.control.width = 260 if e.control.width == 100 else 100
        await self.update_async()

    def build(self):
        return ft.Container(
            content=ft.Text(
                value="Sign in",
                style=ft.TextThemeStyle.BODY_MEDIUM,
                size=25,
                weight="BOLD",
                font_family=r"app\assets\fonts\ocra.ttf",
                text_align=ft.TextAlign.LEFT,
            ),
            alignment=ft.Alignment(-1, -1),
            bgcolor="transparent",
            animate=ft.animation.Animation(300, ft.AnimationCurve.FAST_OUT_SLOWIN),
            width=100,
            height=50,
            border=ft.Border(bottom=ft.BorderSide(width=2.5, color="white")),
            margin=ft.margin.only(top=10, left=10),
            opacity=1,
            on_hover=self.animate,
        )


class Code(ft.UserControl):
    code = ""

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    @classmethod
    async def connection(cls, reader, writer) -> None:
        data = ""
        print("In server")
        while True:
            data = await reader.read(128)
            msg = data.decode()
            print(f"code: {cipher.decrypt(msg).decode('utf-8')}")
            cls.code = cipher.decrypt(msg).decode("utf-8").upper()
            writer.write(data)
            await writer.drain()

    async def animate(self, e):
        e.control.content.hint_text = (
            "Type code from bot" if e.control.width == 180 else None
        )
        e.control.width = 260 if e.control.width == 180 else 180
        e.control.margin = (
            ft.margin.only(left=10)
            if e.control.margin == ft.margin.only(left=50)
            else ft.margin.only(left=50)
        )
        await self.update_async()

    async def submit(self, e):
        if self.code == "":
            e.control.error_text = "Use the bot to get code"
        elif self.code == e.control.value:
            await self.page.clean_async()
            self.page.window_width = 1100
            await self.page.add_async(MainPage(page=self.page))
            await self.page.update_async()
        else:
            e.control.error_text = "incorrect code"
        await self.update_async()

    def build(self):
        return ft.Container(
            content=ft.TextField(
                label="Code",
                label_style=ft.TextStyle(
                    font_family=r"app\assets\fonts\ocra.ttf",
                    weight="BOLD",
                    color="white",
                    size=20,
                ),
                capitalization=ft.TextCapitalization.CHARACTERS,
                password=True,
                max_length=16,
                max_lines=1,
                text_size=15,
                multiline=False,
                bgcolor="",
                text_align=ft.TextAlign.LEFT,
                cursor_color="white",
                cursor_height=20,
                can_reveal_password=True,
                focused_color="white",
                color="white",
                border="underline",
                border_color="white",
                prefix_icon=ft.icons.LOCK,
                on_submit=self.submit,
            ),
            alignment=ft.Alignment(0, 0),
            animate=ft.animation.Animation(1000, ft.AnimationCurve.EASE),
            on_hover=self.animate,
            width=180,
            height=100,
            margin=ft.margin.only(left=50),
            bgcolor="transparent",
        )


class Hint(ft.UserControl):
    async def animate(self, e):
        e.control.disabled = True
        await self.update_async()
        text = ""
        for i in "SCAN QR":
            text += i
            e.control.hint_text = text
            await self.update_async()
            await asyncio.sleep(0.1)
        e.control.disabled = False
        await self.update_async()

    def build(self):
        return ft.Container(
            content=ft.TextField(
                label="",
                label_style=ft.TextStyle(
                    font_family=r"app\assets\fonts\ocra.ttf",
                    weight="BOLD",
                    color="white",
                    size=20,
                ),
                border_radius=30,
                multiline=True,
                focused_color="white",
                border_color="white",
                read_only=True,
                text_align=ft.TextAlign.CENTER,
                hint_text="",
                hint_style=ft.TextStyle(
                    font_family=r"app\assets\fonts\ocra.ttf",
                    weight="BOLD",
                    color="BLUE_100",
                    size=20,
                ),
                on_focus=self.animate,
                icon=ft.icons.TELEGRAM_SHARP,
            ),
            margin=ft.margin.only(left=50),
            alignment=ft.Alignment(0, 0),
            width=180,
        )


class SignIn(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=ft.Column(controls=[SignInText(), Code(page=self.page), Hint()]),
            width=300,
            height=250,
            bgcolor="transparent",
        )


class QR(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Image(
                src=r"app\assets\images\white_qr.png",
                width=150,
                height=150,
            ),
            alignment=ft.Alignment(0, 0),
            bgcolor="transparent",
            width=150,
            height=150,
            border_radius=10,
            margin=ft.margin.only(left=65),
        )


class BlackPanel(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[SignIn(page=self.page), QR()],
                alignment=ft.MainAxisAlignment.START,
                spacing=15.0,
            ),
            alignment=ft.Alignment(0, 0),
            bgcolor="black",
            width=300,
            height=450,
            border_radius=20,
            border=ft.Border(
                top=ft.BorderSide(width=10, color="grey"),
                right=ft.BorderSide(width=10, color="grey"),
                left=ft.BorderSide(width=10, color="grey"),
                bottom=ft.BorderSide(width=10, color="grey"),
            ),
        )


class ITMOImage(ft.UserControl):
    def build(self):
        return ft.Image(
            src=r"app\assets\images\label.png",
            width=300,
            height=120,
        )


class BackgroundImage(ft.UserControl):
    def build(self):
        return ft.Image(
            src=r"app\assets\images\background_image.gif",
            width=700,
            height=900,
            fit="fill",
        )


class SingInPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Container(
            content=ft.Stack(
                controls=[
                    BackgroundImage(),
                    ft.Column(
                        controls=[
                            # A outer container in a stack, which inckudes two columns (Inner image, Inner container)
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        # 1 Inner image
                                        ITMOImage(),
                                        # 2. Inner container
                                        BlackPanel(page=self.page),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=1.0,
                                    wrap=False,
                                ),
                                # params for outer container
                                alignment=ft.Alignment(0, 0),
                                height=750,
                                width=600,
                                bgcolor="white",
                                border_radius=20,
                                opacity=0.88,
                                margin=ft.margin.only(left=50, right=50),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
            ),
            width=700,
            height=900,
        )
