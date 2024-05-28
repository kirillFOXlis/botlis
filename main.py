from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from  keyboard.keyboards  import get_keyboard_1, get_keyboard_2
from keyboard.keyboardinline import get_keyboard_inline_1, get_keyboard_inline_2, get_keyboard_inline_3, get_keyboard_inline_4, get_keyboard_inline_5, get_keyboard_inline_6

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)



async  def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description='Команда чтобы начать'),
        types.BotCommand(command='/help', description='Помощь по командам'),
        types.BotCommand(command='/lis', description='Жмякни'),
        types.BotCommand(command='/viki', description='Определение про лис'),
        types.BotCommand(command='/poroda', description='Бот выдаст разные породы лис'),
        types.BotCommand(command='/kl1', description='sfsfsfsf'),
        types.BotCommand(command='/kl2', description='sfsfsffgfgfgfsf'),
        types.BotCommand(command='/kl3', description='sfsfsffgfgfgfsf'),
        types.BotCommand(command='/kl4', description='sfsfsffgfgfgfsf')


    ]

    await bot.set_my_commands(commands)



@dp.message_handler(commands= 'start')
async def cm1(message: types.message):
    await message.reply('Ку, Я твой эхо бот', reply_markup=get_keyboard_1())


@dp.message_handler(commands= 'help')
async def cm2(message: types.message):
    await message.reply('Я могу помочь тебе',)

@dp.message_handler(commands= 'lis')
async def cm3(message: types.message):
    await message.reply('Тут есть лиса')

@dp.message_handler(commands= 'viki')
async def cm4(message: types.message):
    await message.reply('Обыкнове́нная лиси́ца или ры́жая лиси́ца (лат. Vulpes vulpes; обиходное русское название — лиса́) — хищное млекопитающее семейства псовых, наиболее распространённый и самый крупный вид рода лисиц. Длина тела 60—90 см, хвоста — 40—60 см, масса — 6—10 кг.')

@dp.message_handler(commands= 'poroda')
async def cm5(message: types.message):
    await message.reply("Бенгальская лисица (Vulpes bengalensis)"
    "Афганская лисица (Vulpes cana)"
    "Южноафриканская лисица (Vulpes chama)"
    "Корсак (Vulpes corsac)"
    "Тибетская лисица (Vulpes ferrilata)"
    "Песец (Vulpes lagopus)"
    "Американская лисица (Vulpes macrotis)"
    "Африканская лисица (Vulpes pallida)")





@dp.message_handler(commands= 'kl1')
async def cm6(message: types.message):
    await message.reply('Переключсь на клаву 2', reply_markup=get_keyboard_inline_4())

@dp.message_handler(commands= 'kl2')
async def cm7(message: types.message):
    await message.reply('Переключись на клаву 1', reply_markup=get_keyboard_inline_3())


@dp.message_handler(commands= 'kl3')
async def cm8(message: types.message):
    await message.reply('Переключись на клавууууууууууу 2', reply_markup=get_keyboard_inline_5())


@dp.callback_query_handler(lambda c: c.data == 'go4')
async def go4(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на клавуууууууууууу 2', reply_markup=get_keyboard_inline_6())

@dp.callback_query_handler(lambda c: c.data == 'go3')
async def go3(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text('Ты перешёл на клавууууууууууууууууу 1', reply_markup=get_keyboard_inline_5())




@dp.callback_query_handler(lambda c: c.data == 'go2')
async def go2(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Ты перешёл на клаву 1', reply_markup=get_keyboard_inline_4())

@dp.callback_query_handler(lambda c: c.data == 'go1')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Ты перешёл на клаву 2', reply_markup=get_keyboard_inline_3())






@dp.message_handler(lambda message: message.text == 'Покажи взрослую лису')
async def bt_click1(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://www.purmuseum.ru/uploads/images/2021/Publikacii2021/LisaKrasnay/Big/%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D0%B0%D1%8F%20%D0%BB%D0%B8%D1%81%D0%B0%20(1).jpg', caption='Вот лис который охотится', reply_markup=get_keyboard_inline_1())

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def bt_click2(message: types.Message):
    await message.answer('Ты перешёл на следующую клавиатуру',reply_markup=get_keyboard_2())


@dp.message_handler(lambda message: message.text == 'Покажи маленького лисёнка')
async def bt_click3(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSgdfCcBOyR99on817dPFVWklZHqhHYbAJzmnEo70DDFA&s', caption='Вот тебе лисёнок', reply_markup=get_keyboard_inline_2())

@dp.message_handler(lambda message: message.text == 'Вернуться на предыдущую клавиатуру')
async def bt_click4(message: types.Message):
    await message.answer('Ты вернулся на предыдущую клавиатуру',reply_markup=get_keyboard_1())






@dp.message_handler()
async def echo(message: types.message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
