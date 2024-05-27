from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async  def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description='Команда чтобы начать'),
        types.BotCommand(command='/help', description='Помощ по командам'),
        types.BotCommand(command='/lis', description='Жмякни'),
        types.BotCommand(command='/viki', description='Определение про лис'),
        types.BotCommand(command='/poroda', description='Бот выдаст разные породы лис')
    ]

    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def cm1(message: types.message):
    await message.reply('Ку, Я твой эхо бот')

@dp.message_handler(commands= 'help')
async def cm2(message: types.message):
    await message.reply('Я могу помочь тебе')

@dp.message_handler(commands= 'lis')
async def cm3(message: types.message):
    await message.reply('Тут есть лиса')

@dp.message_handler(commands= 'viki')
async def cm4(message: types.message):
    await message.reply('Обыкнове́нная лиси́ца или ры́жая лиси́ца (лат. Vulpes vulpes; обиходное русское название — лиса́) — хищное млекопитающее семейства псовых, наиболее распространённый и самый крупный вид рода лисиц. Длина тела 60—90 см, хвоста — 40—60 см, масса — 6—10 кг.')

@dp.message_handler(commands= 'poroda')
async def cm5(message: types.message):
    await message.reply('Бенгальская лисица (Vulpes bengalensis)'
                        'Афганская лисица (Vulpes cana)'
                        'Южноафриканская лисица (Vulpes chama)'
                        'Корсак (Vulpes corsac)'
                        'Тибетская лисица (Vulpes ferrilata)'
                        'Песец (Vulpes lagopus)'
                        'Американская лисица (Vulpes macrotis)'
                        'Африканская лисица (Vulpes pallida)')

@dp.message_handler()
async def echo(message: types.message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
