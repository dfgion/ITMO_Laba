from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command

from app.utils.server import run_server

from bot.client import run_client
from bot.core.statesgroup import BlockStatesGroup
from bot.config.cfg import bot, dp

import secrets

import asyncio

from app.utils.cipher import cipher

router = Router()

@router.message(BlockStatesGroup.block)
async def already_have_code(message: Message):
    await message.answer('Вы уже получили свой код аутентификации')

@router.message(Command('start'), )
async def start(message: Message, state: FSMContext):
    await message.answer('Здравствуйте\n❗️Коннект Telegram является обязательной частью подключения❗️\nВведите код в приложении, после чего нажмите enter.')
    await state.set_state(BlockStatesGroup.block)
    photos = await bot.get_user_profile_photos(user_id=message.from_user.id, limit=1)
    file = await bot.get_file(photos.photos[0][0].file_id)
    await bot.download_file(file.file_path, "app/assets/images/profile_photo.png")
    token = secrets.token_hex(8)
    task1 = asyncio.create_task(run_server())
    task2 = asyncio.create_task(run_client(cipher.encrypt(token.encode('utf-8'))))
    await message.answer(f'Ваш код {token}')