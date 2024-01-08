import flet as ft


class BansPage(ft.UserControl):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page

    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.Row(controls=[]),
            height=750,
            width=800,
            border_radius=20,
            opacity=0.88,
            bgcolor="grey",
            offset=ft.transform.Offset(0, -2),
            animate_offset=ft.animation.Animation(
                600, ft.AnimationCurve.ELASTIC_IN_OUT
            ),
            visible=True,
            disabled=False,
            # on_animation_end=self.end
        )
