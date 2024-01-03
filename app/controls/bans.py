from typing import Any, List, Optional, Union
import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue

class BansPage(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    async def end(self, e):
        e.control.visible = False if e.control.offset == ft.transform.Offset(0, 2) else True
        e.control.disabled = True if e.control.offset == ft.transform.Offset(0, 2) else False
        await self.update_async()

    def build(self):
        return ft.Container(content=ft.Row(controls=[
                                                        ]),
                            height=750,
                            width=800,
                            border_radius=20,
                            opacity=1,
                            bgcolor='yellow',
                            
                            offset=ft.transform.Offset(0, -2),
                            animate_offset=ft.animation.Animation(600, ft.AnimationCurve.ELASTIC_IN_OUT),
                            visible=True,
                            disabled=True,
                            #on_animation_end=self.end
                            )