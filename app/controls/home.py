import datetime

import flet as ft


class ProfileImage(ft.UserControl):
    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.Image(
                src=r"app\assets\images\profile_photo.png",
                width=200,
                height=200,
                border_radius=30
            ),
            border_radius=20,
            width=170,
            height=170,
            bgcolor='black',
            margin=ft.margin.only(left=170, top=10)
        )
        
class LeftPart(ft.UserControl):
    def __init__(self, nickname) -> None:
        super().__init__()
        self.nickname = nickname
    def build(self) -> ft.Column:
        return ft.Column(controls=[
                            ft.TextField(width=180,
                                         label='Nickname',
                                         value=self.nickname,
                                         border=ft.InputBorder.UNDERLINE,
                                         icon=ft.icons.VERIFIED_USER,
                                         color='black',
                                         border_color='black',
                                         bgcolor='transparent',
                                         filled=True,
                                         read_only=True,
                                         label_style=ft.TextStyle(
                                             size=15,
                                             weight="BOLD",
                                             font_family=r"app\assets\fonts\ocra.ttf",
                                             color='black'
                                         )
                                         ),
                            ft.TextField(width=180,
                                         label='Access rights',
                                         value='Administrator',
                                         border=ft.InputBorder.UNDERLINE,
                                         icon=ft.icons.ADMIN_PANEL_SETTINGS,
                                         color='black',
                                         border_color='black',
                                         bgcolor='transparent',
                                         filled=True,
                                         read_only=True,
                                         label_style=ft.TextStyle(
                                             size=15,
                                             weight="BOLD",
                                             font_family=r"app\assets\fonts\ocra.ttf",
                                             color='black'
                                         )
                                         )
                            ],
                         alignment=ft.MainAxisAlignment.CENTER,
                         spacing=20
                         )
    
class RightPart(ft.UserControl):
    def build(self) -> ft.Column:
        return ft.Column(controls=[
                            ft.TextField(width=180,  
                                         label='Last login',
                                         value=str(datetime.date.today()).replace('-', '.'),
                                         border=ft.InputBorder.UNDERLINE,
                                         icon=ft.icons.UPDATE,
                                         color='black',
                                         border_color='black',
                                         bgcolor='transparent',
                                         filled=True,
                                         read_only=True,
                                         label_style=ft.TextStyle(
                                                        size=15,
                                                        weight="BOLD",
                                                        font_family=r"app\assets\fonts\ocra.ttf",
                                                        color='black'
                                                        )
                                         ),
                            ft.TextField(width=180,
                                         label='Status',
                                         value='🟢 Online',
                                         border=ft.InputBorder.UNDERLINE,
                                         icon=ft.icons.ONLINE_PREDICTION,
                                         color='black',
                                         border_color='black',
                                         bgcolor='transparent',
                                         filled=True,
                                         read_only=True,
                                         label_style=ft.TextStyle(
                                                        size=15,
                                                        weight="BOLD",
                                                        font_family=r"app\assets\fonts\ocra.ttf",
                                                        color='black'
                                                        )
                                         )
                            ],
                         alignment=ft.MainAxisAlignment.CENTER,
                         spacing=20
                         )
        
class ProfileInfo(ft.UserControl):
    def __init__(self, nickname) -> None:
        super().__init__()
        self.nickname = nickname
    def build(self) -> ft.Container:
        return ft.Container(
                    content=ft.Column(
                                controls=[
                                    ft.Container(
                                        content=ft.Text(
                                                    value='INFORMATION',
                                                    size=25,
                                                    font_family=r"app\assets\fonts\ocra.ttf",
                                                    weight='BOLD'
                                                    ),
                                        width=250,
                                        border=ft.Border(bottom=ft.BorderSide(width=1, color='grey')),
                                        margin=ft.margin.only(top=20, left=120),
                                        alignment=ft.alignment.Alignment(0, 0)
                                        ),
                                    ft.Row(
                                        controls=[
                                            LeftPart(nickname=self.nickname),
                                            RightPart()
                                            ],
                                        spacing=20,
                                        alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                    ],
                                spacing=100
                                ),
                    width=500,
                    height=500,
                    bgcolor='white',
                    border_radius=20,
                    border=ft.Border(top=ft.BorderSide(width=5, color='black'),
                                    left=ft.BorderSide(width=5, color='black'),
                                    bottom=ft.BorderSide(width=5, color='black'),
                                    right=ft.BorderSide(width=5, color='black'))
                    )

class HomePage(ft.UserControl):
    def __init__(self, page, nickname) -> None:
        super().__init__()
        self.page = page
        self.nickname = nickname

    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                controls=[
                    ProfileImage(),
                    ProfileInfo(nickname=self.nickname)
                    ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15
            ),
            height=750,
            width=800,
            border_radius=20,
            opacity=0.88,
            bgcolor="grey",
            disabled=False,
            visible=True,
            alignment=ft.alignment.Alignment(0, 0),
            animate_offset=ft.animation.Animation(
                600, ft.AnimationCurve.ELASTIC_IN_OUT
            ),
            offset=ft.transform.Offset(0, -2),
            # on_animation_end=self.end
        )
