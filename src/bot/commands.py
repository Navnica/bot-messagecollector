import aiogram
from aiogram import filters

router: aiogram.Router = aiogram.Router()

@router.message(filters.Command(commands=['start']))
async def start(message: aiogram.types.Message) -> None:
    markup = aiogram.types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                aiogram.types.KeyboardButton(
                    text='Настройки',
                    web_app=aiogram.types.web_app_info.WebAppInfo(
                        url='https://example.com'
                    )
                )
            ]
        ]
    )
    await message.answer('f', reply_markup=markup)