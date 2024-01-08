import flet as ft


def formatting(row: str, disable_rewrite: bool) -> str:
    # МЕСТО ДЛЯ ВАШЕГО КОДА
    # Данная функция вызывается для каждой строки, содержащую Имя, Последняя активность, Город, Права доступа, ID, Паспорт, ИНН"
    # С помощью регулярного выражения вам нужно отформатировать строку
    #formatted_row = re.sub(pattern=pattern, repl=r'Имя: \1 | Актив: \2 | Город: \3 | Статус: \4 | ID: \5 | Паспорт: \6 | ИНН: \7', string=row)
    # Место для вашего кода
    pass

def get_entries(path: str, disable_rewrite: bool = False) -> str:
    # В цикле возвращать результат функции formatting с аргументом row с помощью служебного слова yield
    # Место для вашего кода
    yield

def generate_correct_csv(row: list, path: str = r'app\utils\correct_users.csv') -> None:
    # Место для вашего кода
    pass
        
async def get_entries_async(path: str = r'app\utils\correct_users.csv', disable_rewrite: bool = True) -> str:
    # Место для вашего кода
    yield
            
async def delete_user_async(user_id: str, path: str = r'app\utils\correct_users.csv') -> None:
    # Место для вашего кода
    pass
        
def flutter_formatting(name: str, last_login: str, city: str, status: str, user_id: str, passport: str, tin: str) -> ft.Row:
    return ft.DataRow(
                      cells=[
                        ft.DataCell(ft.Text(value=name, 
                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                            weight='BOLD', 
                                            color='black'),
                                    ),
                        ft.DataCell(ft.Text(value=last_login, 
                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                            weight='BOLD', 
                                            color='black'),
                                    ),
                        ft.DataCell(ft.Text(value=city, 
                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                            weight='BOLD', 
                                            color='black'),
                                    ),
                        ft.DataCell(ft.Text(value=status, 
                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                            weight='BOLD', 
                                            color='black'),
                                    ),
                        ft.DataCell(ft.Text(value=user_id, 
                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                            weight='BOLD', 
                                            color='black'),
                                    ),
                        ft.DataCell(ft.Text(value=passport, 
                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                            weight='BOLD', 
                                            color='black'),
                                    ),
                        ft.DataCell(ft.Text(value=tin, 
                                            font_family=r"app\assets\fonts\kbastrolyte.ttf", 
                                            weight='BOLD', 
                                            color='black'),
                                    ),
                        ]
                     )