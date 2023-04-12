from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

import json
import config

from validators import CheckoutValidator
from services import InvoiceService



if config.APP_URL == '':
    print('APP_URL is empty')
    exit()

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)
invoice = InvoiceService

data = []


@dp.message_handler(
    commands=['start']
)
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton(
            text='Open products',
            web_app=WebAppInfo(url=config.APP_URL)
        )
    )
    await message.answer(
        text=f'Greeting you in {config.APP_NAME}',
        reply_markup=markup)


@dp.message_handler(
    content_types=['web_app_data']
)
async def web_app(message: types.Message):
    global data
    data = json.loads(message.web_app_data.data)

    if CheckoutValidator.valid(data):
        try:
            await InvoiceService.send(message, bot, data)
        except Exception as e:
            print(e)
            await message.answer(
                text='Something wrong'
            )

    else:
        await message.answer(
            text='Wrong payment data. Please try again.'
        )


@dp.pre_checkout_query_handler(
    lambda query: True
)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(
        pre_checkout_query_id=pre_checkout_query.id,
        ok=True,
        error_message="Checkout error"
    )


@dp.message_handler(
    content_types=types.ContentType.SUCCESSFUL_PAYMENT
)
async def success(message: types.Message):
    await message.answer(
        text='Thank you for buying'
    )


executor.start_polling(dp)
