import typing as tp 
import re
import flet as ft
import csv

import asyncio

import aiofiles

from aiocsv import AsyncReader, AsyncWriter

from pprint import pprint


def formatting(row: str, disable_rewrite: bool) -> str:
    # МЕСТО ДЛЯ ВАШЕГО КОДА
    # Данная функция вызывается для каждой строки, содержащую Имя, Последняя активность, Город, Права доступа, ID, Паспорт, ИНН"
    # С помощью регулярного выражения вам нужно отформатировать строку
    #formatted_row = re.sub(pattern=pattern, repl=r'Имя: \1 | Актив: \2 | Город: \3 | Статус: \4 | ID: \5 | Паспорт: \6 | ИНН: \7', string=row)
  
    if disable_rewrite == False:
        pattern = r'([А-я]+),*([0-9\-]+),*([А-я\s\-]+),*([А-я]+),*([0-9]{3}),*([0-9\s]+),*([0-9]+)'
        formatted_row = re.sub(pattern=pattern, repl=r'\1,\2,\3,\4,\5,\6,\7', string=row)
        info = formatted_row.split(',')  
        print(info)
        generate_correct_csv(row=info)
    else:
        info = row.split(',')
        print(info)
    formatted_row = flutter_formatting(name=info[0], last_login=info[1], city=info[2], status=info[3], user_id=info[4], passport=info[5], tin=info[6])
    return formatted_row

def get_entries(path: str, disable_rewrite: bool = False) -> str:
    # В цикле возвращать результат функции formatting с аргументом row с помощью служебного слова yield
    with open(path, newline='', encoding='utf-8') as fp:
        fp.readline()
        reader = csv.reader(fp, delimiter='\n')
        for line in reader:
            yield formatting(line[0], disable_rewrite = disable_rewrite)

def generate_correct_csv(row: list, path: str = r'app\utils\correct_users.csv') -> None:
    with open(path, 'a', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp)
        writer.writerows([row])
        
async def get_entries_async(path: str, disable_rewrite: bool = True) -> str:
    async with aiofiles.open(path, newline='', encoding='utf-8') as af:
        await af.readline()
        async for line in AsyncReader(af, delimiter='\n'):
            yield formatting(line[0], disable_rewrite=disable_rewrite)
            
async def delete_user_async(user_id: str, path: str = r'app\utils\correct_users.csv') -> None:
    async with aiofiles.open(path, 'w', newline='', encoding='utf-8') as af:
        writer = AsyncWriter(af)
        await writer.writerows([]
                               )
        
def flutter_formatting(name, last_login, city, status, user_id, passport, tin) -> ft.Row:
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

def main():
    l = [i for i in get_entries(r'app\utils\users.csv')]
    print(l)

if __name__ == "__main__":
    main()
    # asyncio.run(main())
