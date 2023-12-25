import asyncio
import logging
import tok

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command

bot = Bot(token = tok.token)
dp = Dispatcher()

styles_list = ['bottts', 'adventurer', 'avataaars', 'big-ears', 'big-smile',
            'croodles', 'fun-emoji', 'icons', 'identicon', 'initials',
            'lorelei', 'micah', 'miniavs', 'notionists', 'open-peeps',
            'personas', 'pixel-art', 'rings', 'shapes', 'thumbs']

@dp.message(CommandStart())
async def start_handle(message: types.Message):
    await message.answer(
        text = "Привет, я генерирую картинки"
    )
@dp.message(Command("help", prefix = "!/@#\\-"))
async def help_handle(message: types.Message):
    await message.answer(
        text = "Чтобы сгенерировать картинку напиши выбранный_стиль:текст"
    )

@dp.message(Command("styles", prefix = "!/@#\\-"))
async def styles_handle(message: types.Message):
    await message.answer(
        text = "Есть, такие стили: \n"
               "bottts, adventurer, avataaars, big-ears, big-smile, \n"
               "croodles, fun-emoji, icons, identicon, initials, \n"
               "lorelei, micah, miniavs, notionists, open-peeps, \n"
               "personas, pixel-art, rings, shapes, thumbs"

    )

@dp.message()
async def message(message: types.Message):
    check_style = False
    if ':' in message.text:
        result = message.text.split(':')
        for style in styles_list:
            if style == result[0]:
                check_style = True
                await bot.send_photo(
                    chat_id=message.chat.id,
                    photo=f'https://api.dicebear.com/7.x/{result[0]}/png?seed={result[1]}'
                )
                await message.answer(text=f"Помоему эта картинка похожа на {result[1]}")
        if not check_style:
            await bot.send_message(
                chat_id = message.chat.id,
                text = 'Такого стиля нет'
            )

    else:
        await message.answer(
            text = 'Некорректный ввод, введите команду help'
        )

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())