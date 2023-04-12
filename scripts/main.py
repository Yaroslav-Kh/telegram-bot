from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo;

import json
import config

if config.APP_URL == '':
    print('APP_URL is empty')
    exit
    

bot = Bot(config.BOT_TOKEN);
dp = Dispatcher(bot)

data = [];

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Open products', web_app=WebAppInfo(url=config.APP_URL)))
    await message.answer('Greeting you in lightsabers shop', reply_markup=markup)


@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    global data
    data = json.loads(message.web_app_data.data)
    if data['user_name'] != '' and data['email'] != '' and data['phone'] != '':
        await bot.send_invoice(
            message.chat.id, 
            'Lightsaber for Padawan', 
            'Buying Lightsaber for Padawan',
            'invoice',
            config.PAYMENT_TOKEN,
            data['currency'], 
            [types.LabeledPrice(data['product_name'],int(data['product_price']) * 100)]
        ) 
    else :
       await message.answer('Wrong payment data. Please try again.')


@dp.pre_checkout_query_handler(lambda query: True)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                        error_message="Aliens tried to steal your card's CVV,"
                                                      " but we successfully protected your credentials,"
                                                      " try to pay again in a few minutes, we need a small rest.")


@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def success(message: types.Message):
    await message.answer('Thank you for buying')


executor.start_polling(dp)
