import logging
from PIL import Image
from io import BytesIO
import asyncio
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram import F

TOKEN = '6824113704:AAGOTm1sEVxlLhG7PCOShxfFN6yrzNaT-6M'
IS_CAR_PHOTO = False

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    kb = [
        [
            types.KeyboardButton(text="Upload car!")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Нажми кнопочку!"
    )
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=keyboard)


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    help_text = "A bot for getting a car brand based on a photo\n\n"
    help_text += "/start - Find out the car!\n"
    help_text += "/help - Show help"
    await message.answer(help_text)


@dp.message(F.text == "Upload car!")
async def with_puree(message: types.Message):
    await message.reply("Send me your photo!", reply_markup=types.ReplyKeyboardRemove())


@dp.message(F.photo)
async def download_photo(message: Message, bot: Bot):
    # await bot.download(
    #     message.photo[-1],
    #     destination=f"./tmp/{message.photo[-1].file_id}.jpg"
    # )
    # path = f"./tmp/{message.photo[-1].file_id}.jpg"

    fp = BytesIO()
    d = await bot.download(message.photo[-1], fp)
    # image = message.photo[-1]
    print(d)
    result = await get_car_info("")
    await message.reply(f"Hmm... I think it's a {result}")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


async def get_car_info(image_path):
    return image_path


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
