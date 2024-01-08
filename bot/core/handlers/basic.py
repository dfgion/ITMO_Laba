import asyncio
import secrets

from aiogram import F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.utils.cipher import cipher
from app.utils.server import run_server
from bot.client import run_client
from bot.config.cfg import bot, dp
from bot.core.statesgroup import BlockStatesGroup

router = Router()


@router.message(BlockStatesGroup.block)
async def already_have_code(message: Message):
    await message.answer("Вы уже получили свой код аутентификации")

@router.message(
    Command("start"),
)
async def start(message: Message, state: FSMContext):
    await message.answer(
        "Здравствуйте\n❗️Коннект Telegram является обязательной частью подключения❗️\nВведите код в приложении, после чего нажмите enter."
    )
    await state.set_state(BlockStatesGroup.block)
    photos = await bot.get_user_profile_photos(user_id=message.from_user.id, limit=1)
    # Фотография скачивается на компьютер, с которого было отправлено сообщение, так как хост это и сервер и клиент, следовательно нет потребности в том, чтобы отправлять фотографию по сети. В других же случаях фотография будет отправлять по сети.
    file = await bot.get_file(photos.photos[0][0].file_id)
    await bot.download_file(file.file_path, "app/assets/images/profile_photo.png")
    token = secrets.token_hex(8)
    info_to_send = f"{token} {message.from_user.first_name}"
    task1 = asyncio.create_task(run_server(), name='Server')
    task2 = asyncio.create_task(run_client(cipher.encrypt(info_to_send.encode("utf-8"))), name='Client')
    await message.answer(f"Ваш код {token}")
    await task2