from typing import Any, List, Optional, Union

import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import (
    AnimationValue,
    ClipBehavior,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)


class ProfileImage(ft.UserControl):
    def build(self):
        return ft.Container(
            content=ft.Image(
                src=r"app\assets\images\profile_photo.png",
                width=200,
                height=200,
            ),
            width=160,
            height=160,
            bgcolor="grey",
            margin=ft.margin.only(top=10, left=10),
        )


class Left_Part(ft.UserControl):
    def build(self):
        return ft.Column(
            controls=[ProfileImage(), ft.TextField()],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )


class Right_Part(ft.UserControl):
    def build(self):
        return ft.Column(
            controls=[ft.TextField()], alignment=ft.MainAxisAlignment.CENTER
        )


class HomeOption(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    async def end(self, e):
        e.control.visible = (
            False if e.control.offset == ft.transform.Offset(0, 2) else True
        )
        e.control.disabled = (
            True if e.control.offset == ft.transform.Offset(0, 2) else False
        )
        await self.update_async()

    def build(self):
        return ft.Container(
            height=750,
            width=800,
            border_radius=20,
            opacity=1,
            bgcolor="purple",
            disabled=False,
            visible=True,
            animate_offset=ft.animation.Animation(
                600, ft.AnimationCurve.ELASTIC_IN_OUT
            ),
            offset=ft.transform.Offset(0, -2),
            # on_animation_end=self.end
        )

    async def update_async(self):
        return await super().update_async()
