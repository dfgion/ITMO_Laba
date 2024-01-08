import flet as ft
import flet_core as ft_core

from app.functions.database_func import get_entries, get_entries_async, delete_user_async


class DatabaseText(ft.UserControl):
    def build(self) -> ft.Container:
        return ft.Container(
                    content=ft.Text(
                                value='DATABASE',
                                size=25,
                                font_family=r"app\assets\fonts\ocra.ttf",
                                weight='BOLD'
                                ),
                    width=250,
                    height=100,
                    border_radius=20,
                    bgcolor='white',
                    margin=ft.margin.only(left=270, top=10),
                    alignment=ft.alignment.Alignment(0, 0),
                    border=ft.Border(top=ft.BorderSide(width=5, color='black'),
                                    left=ft.BorderSide(width=5, color='black'),
                                    bottom=ft.BorderSide(width=5, color='black'),
                                    right=ft.BorderSide(width=5, color='black'))
                    )   

class Entries(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.entries = [i for i in get_entries(r'app\utils\users.csv', disable_rewrite=False)]
        
    async def sort_by_id(self, e: ft.DataColumnSortEvent) -> None:
        self.controls[0].controls[0].controls[0].rows.sort(
            key=lambda x: x.cells[e.column_index].content.value,
            reverse=self.controls[0].controls[0].controls[0].sort_ascending,
        )
        self.controls[0].controls[0].controls[0].sort_ascending = not self.controls[0].controls[0].controls[0].sort_ascending
        await self.update_async()
        
    def build(self) -> ft.Row:
        return ft.Row(controls=[
                            ft.Column(
                                controls=[
                                    ft.DataTable(column_spacing=10,
                                                 sort_ascending=True,
                                                 sort_column_index=4,
                                                 heading_row_height=40,
                                                 width=750,
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
                                                                    on_sort=self.sort_by_id,
                                                                    tooltip='Sort by id'
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
                                                    ],
                                                )
                                    ],
                                scroll=True,
                                )
                            ], 
                      scroll=True,  
                      width=750)

class DatabaseEntriesBlock(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()
    def build(self):
        return ft.Container(
                    content=Entries(),
                    width=750,
                    height=525,
                    bgcolor=ft.colors.WHITE,
                    border_radius=0,
                    alignment=ft.alignment.Alignment(0, -1),
                    margin=ft.margin.only(left=20),
                    border=ft.Border(top=ft.BorderSide(width=5, color='black'),
                                    left=ft.BorderSide(width=0, color='black'),
                                    bottom=ft.BorderSide(width=5, color='black'),
                                    right=ft.BorderSide(width=0, color='black'))
                    
                    )
        
class Delete(ft.UserControl):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        
    async def delete(self, e: ft_core.ControlEvent) -> None:
        print(type(e.control.value))
        datatable: ft.DataTable = self.page.controls[0].controls[0].content.controls[1].controls[1].controls[1].controls[0].content.controls[1].controls[0].content.controls[0].controls[0].controls[0]
        if e.control.value == "":
            e.control.error_text = 'type ID'
        else:
            try:
                int(e.control.value)
                await delete_user_async(path=r'app\utils\correct_users.csv', user_id = e.control.value)
                datatable.rows = [i async for i in get_entries_async(path=r'app\utils\correct_users.csv')]
            except:
                e.control.error_text = 'type number'
        await e.control.update_async()
        await datatable.update_async()
        
    def build(self) -> ft.Row:
        return ft.Row(
            controls=[
                ft.TextField(bgcolor='white',
                             label='DELETE',
                             label_style=ft.TextStyle(
                                                     font_family=r"app\assets\fonts\ocra.ttf",
                                                     weight="BOLD",
                                                     color="black",
                                                     size=20,
                                                     ),
                             color='black',
                             height=100, 
                             max_length=3,
                             max_lines=1,
                             width=150,
                             multiline=False,
                             text_style=ft.TextStyle(
                                                    font_family=r"app\assets\fonts\ocra.ttf",
                                                    weight="BOLD",
                                                    color="black",
                                                    ),
                             text_size=15,
                             text_align=ft.TextAlign.CENTER, 
                             focused_bgcolor='white',
                             focused_color='black',
                             hint_text='type ID',
                             focused_border_color='black',
                             cursor_color='black',
                             border=ft.border.all(width=5, color='black'),
                             icon=ft.icons.GRID_OFF,
                             on_submit=self.delete,
                             hint_style=ft.TextStyle(
                                                    font_family=r"app\assets\fonts\ocra.ttf",
                                                    weight="BOLD",
                                                    color="grey",
                                                    )
                             )
                ],
            alignment=ft.MainAxisAlignment.CENTER
        )

class DatabasePage(ft.UserControl):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.page = page
        
    def build(self) -> ft.Container:
        return ft.Container(
            content=ft.Column(controls=[
                                DatabaseText(),
                                DatabaseEntriesBlock(),
                                Delete(page=self.page)
                                ]),
            height=750,
            width=800,
            border_radius=20,
            opacity=0.88,
            bgcolor="grey",
            disabled=False,
            visible=True,
            animate_offset=ft.animation.Animation(
                600, ft.AnimationCurve.ELASTIC_IN_OUT
            ),
            offset=ft.transform.Offset(0, -2)
        )
