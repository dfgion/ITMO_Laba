import sys
from typing import Any, List, Optional, Union

import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue

sys.path.append(r'C:\Users\Даниил\Desktop\programming')
from app.functions.database_func import get_entries

import flet as ft

class Entries(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.entries = [i for i in get_entries(r'app\utils\users.csv', disable_rewrite=False)]
        
    async def sort_by_id(self, e: ft.DataColumnSortEvent):
        self.controls[0].content.rows.sort(
            key=lambda x: x.cells[e.column_index].content.value,
            reverse=self.controls[0].content.sort_ascending,
        )
        self.controls[0].content.sort_ascending = not self.controls[0].content.sort_ascending
        await self.update_async()
        
    def build(self):
        return ft.Row(controls=[
                    ft.Column(
                        controls=[
                            ft.DataTable(column_spacing=15,
                            sort_ascending=True,
                            sort_column_index=4,
                            heading_row_height=40,
                            columns=[
                                    ft.DataColumn(ft.Text(value='Имя', 
                                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                                            weight='BOLD', 
                                                            color='black'),
                                                    ),
                                    ft.DataColumn(ft.Text(value='Последний актив', 
                                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                                            weight='BOLD', 
                                                            color='black'),
                                                    ),
                                    ft.DataColumn(ft.Text(value='Город', 
                                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                                            weight='BOLD', 
                                                            color='black'),
                                                    ),
                                    ft.DataColumn(ft.Text(value='Права', 
                                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                                            weight='BOLD', 
                                                            color='black'),
                                                    ),
                                    ft.DataColumn(ft.Text(value='ID', 
                                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                                            weight='BOLD', 
                                                            color='black'),
                                                    numeric=True,
                                                    on_sort=self.sort_by_id
                                                    ),
                                    ft.DataColumn(ft.Text(value='Паспорт', 
                                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                                            weight='BOLD', 
                                                            color='black'),
                                                    ),
                                    ft.DataColumn(ft.Text(value='ИНН', 
                                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                                            weight='BOLD', 
                                                            color='black'),
                                                    ),
                                    ],
                            rows=[
                                *self.entries
                            ]
                            )
                        ],
                        scroll=True)
                    ], 
               scroll=True,  
               width=750)

async def gui(page: ft.Page):
    page.padding = 0
    page.title = "ITMO Administrator"
    page.window_maximizable = False

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 1100
    page.window_height = 900
    page.window_resizable = False
    await page.add_async(Entries())


if __name__ == "__main__":
    ft.app(target=gui, assets_dir=r"app\assets")