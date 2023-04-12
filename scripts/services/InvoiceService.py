from aiogram import Bot, Dispatcher, executor, types
from scripts import config


class InvoiceService:

    def __init__(self, message, bot, data):
        self.message = message
        self.bot = bot
        self.data = data

    async def sendInUSD(self):
        await self.bot.send_invoice(
            chat_id=self.message.chat.id,
            title=self.data["product_name"],
            description=f'Buying {self.data["product_name"]}',
            payload='invoice',
            provider_token=config.PAYMENT_TOKEN,
            currency=self.data['currency'],
            prices=[types.LabeledPrice(self.data['product_name'], int(self.data['product_price']) * 100)]
        )

    def sendInUSDT(self):
        return


async def send(message, bot, data):
    invoice = InvoiceService(message, bot, data)
    match data['currency']:
        case "USDT":
            invoice.sendInUSDT()
        case _:
            await invoice.sendInUSD()
