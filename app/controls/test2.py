from typing import Any, List, Optional, Union
import flet as ft
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import AnimationValue, ClipBehavior, OffsetValue, ResponsiveNumber, RotateValue, ScaleValue


class Data(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.table = ft.ListView(controls=[ft.DataTable(
            border=ft.border.all(2, "red"),
            show_bottom_border=True,
            #columns 里必须添加 DataColumn 类型的控件
            columns=[
                    ft.DataColumn(ft.Text("名字")),
                    ft.DataColumn(ft.Text("电话")),
                    ft.DataColumn(ft.Text("地址"), numeric=True),
                ],
            #rows 里必须添加 DataRow 类型的控件
            #DataRow 
            rows=[
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ]),
                ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("John")),
                    ])
                ])
        ], 
                          expand=1, spacing=10, padding=20, auto_scroll=True)
    def build(self):
        return self.table
def gui(page: ft.Page):
    page.padding = 0
    page.title = "ITMO Administrator"
    page.window_maximizable = False

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 1100
    page.window_height = 900
    page.window_resizable = False
    page.add(ft.Container(content=Data()))

ft.app(target=gui)