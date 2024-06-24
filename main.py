from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keyboard.keyboards  import get_keyboard_1, get_keyboard_2
from keyboard.keyboardinline import get_keyboard_inline_1, get_keyboard_inline_2, get_keyboard_inline_5, get_keyboard_inline_6
from keyboard.keyboardinline import get_keyboard_inline_B1, get_keyboard_inline_B2,get_keyboard_inline_B3, get_keyboard_inline_B4, get_keyboard_inline_B5, get_keyboard_inline_B6, get_keyboard_inline_B7, get_keyboard_inline_B8
from keyboard.keyboardinline import get_keyboard_inline_A1
bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async  def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description='Запустить бота'),
        types.BotCommand(command='/help', description='Все команды и их описание'),
        types.BotCommand(command='/poroda', description='Основные породы лис'),
        types.BotCommand(command='/infolis', description='Информация о породах'),
        types.BotCommand(command='/domfox', description='Домашние лисы')




    ]

    await bot.set_my_commands(commands)


 
@dp.message_handler(commands= 'start')
async def cm1(message: types.message):
    await message.reply('Привет! Я бот Фокси. Я помогу тебе узнать какие лисы существуют на планете Земля!', reply_markup=get_keyboard_1())


@dp.message_handler(commands= 'help')
async def cm2(message: types.message):
    await message.reply('Я могу помочь тебе',)



@dp.message_handler(commands= 'poroda')
async def cm5(message: types.message):
    await message.reply("""Бенгальская лисица (Vulpes bengalensis)
Афганская лисица (Vulpes cana)
Южноафриканская лисица (Vulpes chama)
Корсак (Vulpes corsac)
Тибетская лисица (Vulpes ferrilata)
Песец (Vulpes lagopus)
Американская лисица (Vulpes macrotis)
Африканская лисица (Vulpes pallida)""")





@dp.message_handler(commands= 'infolis')
async def cm6(message: types.message):
    await message.reply('Выберите породу лисы', reply_markup=get_keyboard_inline_A1())

@dp.callback_query_handler(lambda c: c.data == 'goC0')
async def go2(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Выберите породу лисы', reply_markup=get_keyboard_inline_A1())




@dp.callback_query_handler(lambda c: c.data == 'goA1')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, """Бенгальская лисица — эндемик Индийского субконтинента. Обитает в предгорьях южных Гималаев, в Непале, Бангладеш и Индии вплоть до южной оконечности Индостана.
Это лисица среднего размера. Длина тела составляет 45–60 см, хвоста — 25–35 см, высота в холке достигает 26–28 см. Масса 1,8–3,2 кг. Шерсть короткая, приглаженная. Окраска варьирует от песчано-оранжевой до красновато-коричневой. Кончик хвоста чёрный.""", reply_markup=get_keyboard_inline_B1())

@dp.callback_query_handler(lambda c: c.data == 'goA2')
async def go2(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, """Афганская лисица — мелкая лисица. Высота в холке — около 30 см, длина тела — 40—50 см, длина хвоста — 33—41 см, высота уха — около 9 см; вес — 1,5—3 кг. Окраска зимней шерсти буровато-серая, с заметным налётом, распространяющимся и по верху длинного пушистого хвоста.
Афганская лисица была описана как вид кошачьей внешности и поведения. Эта маленькая лиса имеет короткую, стройную морду, длинный, густо опушённый хвост, который равняется длине тела лисы, с длинными и темными остевыми волосками.
Подушки лапок не покрыты волосами в отличие от других пустынных лис, которые имеют толстый слой волос, чтобы защитить их лапы от горячего песка. Самцы и самки очень похожи между собой.
Голову украшают очень большие уши, которые помогают не только хорошо слышать, но и рассеивают лишнее тепло, помогая охлаждать организм в жаркую погоду. Острая стройная мордочка имеет отличительную чёрную полосу, простирающуюся от глаз к верхней губе.""", reply_markup=get_keyboard_inline_B2())

@dp.callback_query_handler(lambda c: c.data == 'goA3')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, """Окрас шерсти южноафриканской лисицы варьирует от чёрного до серебристо-серого с лёгким желтоватым оттенком по бокам и на животе.
Кончик хвоста всегда чёрный. Лисица небольшая — размером с домашнего кота.
Длина тела составляет 45—61 см, длина хвоста 35—40 см, высота в холке 28—33 см, а вес от 3,6 до 5 кг[2].""", reply_markup= get_keyboard_inline_B3())

@dp.callback_query_handler(lambda c: c.data == 'goA4')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, """Корсаковая лиса - это лиса среднего размера, с длиной головы и тела от 45 до 65 см (от 18 до 26 дюймов) и хвостом длиной от 19 до 35 см (от 7,5 до 13,8 дюйма).
Взрослые особи весят от 1,6 до 3,2 кг (3,5 -7,1 фунта). У него серый или желтоватый мех на большей части тела, с более светлой нижней частью и бледными отметинами на пасти, подбородке и горле.
Зимой шерсть становится намного гуще и шелковистее по текстуре, она соломенно-серого цвета с более темной линией, идущей по спине""", reply_markup=get_keyboard_inline_B4())

@dp.callback_query_handler(lambda c: c.data == 'goA5')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, """Тибетская лиса — одна из самых маленьких лисьих разновидностей. Зубы хорошо развиты, с чрезвычайно длинными клыками, большими, чем у всех других лис. Тело лисицы покрыто толстым, мягким мехом с плотной нижней подпушью, который хорошо защищает их от сильных ветров.
Морда тибетской лисицы кажется квадратной за счёт густого меха вокруг шеи. Цвет по бокам изменяется от ржаво-коричневого сверху до серого к низу, что создает иллюзию полосы по бокам животного.
Горло, брюшная область, полоска от горла до брюха и кончик хвоста белого цвета.
Длина тела взрослой лисы от 60 до 70 см. Хвост длиной от 30 до 45 см.
Вес взрослой особи от 4 до 5,5 килограммов[2].""", reply_markup=get_keyboard_inline_B5())

@dp.callback_query_handler(lambda c: c.data == 'goA6')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, """Небольшой хищник, по виду напоминающий лису. Длина тела составляет 46,5—73 см, длина хвоста около 25—52 см. Масса составляет 2—8,8 кг. Тело удлинённое, хвост составляет около половины длины тела, у стоящего животного достигает земли.
Голова вытянутая. Уши широко расставленные, длинные, но слабо выступающие из зимнего меха, вершины ушей закруглённые. Единственный представитель псовых, который имеет ярко выраженный сезонный диморфизм в окраске. Зимний мех белый, летний — тёмный со светлыми подпалинами.
Существует морфа голубых песцов, мех которых одноцветен, цвет зимой и летом меняется очень незначительно, варьирует от песочной, серой и светло-кофейной до тёмно-пепельной с голубоватым оттенком. В природе живёт в среднем 3—4 года.""", reply_markup=get_keyboard_inline_B6())

@dp.callback_query_handler(lambda c: c.data == 'goA7')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, """Длина тела 37,5—50,0 см, длина хвоста 22,5—32,3 см, вес самцов 2,2 кг, вес самок 1,9 кг.
Спина светло-седая или желтовато-серая, плечи и бока от жёлто-коричневого до оранжевого, брюхо белое.
Уши расположены близко друг к другу[5]. Тело тонкое, хвост пушистый, слегка сужающийся к концу, составляет около 40 % длины тела.
Ноги длинные, стройные, подошвы ног хорошо покрыты волосами. Покровный волос менее 50 мм в длину и особенно плотный в середине спины. Уши рыжевато-коричневые или серые сзади, меняя окраску на жёлто-коричневую или оранжевую у основания.
Мордочка по бокам и все вибриссы черноватые или коричневатые. Хвост около 60—70 мм толщиной, серый кроме проксимальной (и чем ближе к месту прикрепления) половины нижней поверхности, которая жёлто-коричневого цвета.""", reply_markup=get_keyboard_inline_B7())

@dp.callback_query_handler(lambda c: c.data == 'goA8')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, """Строением своего тела африканская лисица напоминает рыжую лисицу, однако она обладает меньшими размерами, более длинными ногами и более длинными ушами. Длина её тела 38—45 см, длина хвоста 28—29 см.
Высота в плечах 25 см. Масса тела — 1,5—3,6 кг.[2] Окрас светло-рыжий, коричневатый, хвост рыжевато-коричневатый с чёрным концом. Лапы и спина рыжие. Посередине спины располагается тёмная полоса.
Нижняя сторона тела, морда и изнанки ушей — белые.[2] У африканских лисиц пушистый хвост, у взрослых особей глаза окружены тёмным выразительным ободком.""", reply_markup=get_keyboard_inline_B8())




@dp.callback_query_handler(lambda c: c.data == 'goB1')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo= 'https://biologymir.ru/wp-content/uploads/2023/02/indian_fox_at_little_rann_of_kutch.jpg')

@dp.callback_query_handler(lambda c: c.data == 'goB2')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo= 'https://laplaya-rus.ru/wp-content/uploads/2/c/4/2c4c7b91f8b46bca5194896478697c53.jpeg')

@dp.callback_query_handler(lambda c: c.data == 'goB3')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://get.wallhere.com/photo/1920x1225-px-African-fox-look-south-1643165.jpg')

@dp.callback_query_handler(lambda c: c.data == 'goB4')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://laplaya-rus.ru/wp-content/uploads/9/0/9/909714397e0b3cd3d40ad70e1d137300.jpeg')

@dp.callback_query_handler(lambda c: c.data == 'goB5')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://avatars.dzeninfra.ru/get-zen_doc/248942/pub_5c000930618c1b00aaa344e0_5c000b8c03cd6400aaf9acc0/scale_1200')

@dp.callback_query_handler(lambda c: c.data == 'goB6')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://foto-zverey.ru/1/lisa_10.jpg')

@dp.callback_query_handler(lambda c: c.data == 'goB7')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://animals.pibig.info/uploads/posts/2023-04/1680827185_animals-pibig-info-p-bengalskaya-lisitsa-zhivotnie-instagram-63.jpg')

@dp.callback_query_handler(lambda c: c.data == 'goB8')
async def go1(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo='https://ornella.club/uploads/posts/2023-05/1684846724_ornella-club-p-lisa-porodi-fenek-instagram-85.jpg')





@dp.message_handler(commands= 'domfox')
async def cm8(message: types.message):
    await message.reply('Переключись на клавууууууууууу 2', reply_markup=get_keyboard_inline_5())


@dp.callback_query_handler(lambda c: c.data == 'go4')
async def go4(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("""Домашние лисы — группа одомашненных лис, выведенных в ходе продолжительного эксперимента в Новосибирском институте цитологии и генетики.
Эксперимент по одомашниванию лис был начат в 1959 году советским генетиком Дмитрием Беляевым и специалистом по поведению животных Людмилой Трут.
В результате была выведена группа лис, схожих по поведению с собаками: они проявляют более социальное поведение как с другими особями, так и с людьми, более игривы и дружелюбны, а также сохраняют юношеские черты в зрелом возрасте.
Домашние лисы живут в Америке, Германии, Нидерландах. Их поведение близко к поведению собаки, но при этом лисицы остаются такими же независимыми, как кошки. Перед продажей лисиц стерилизуют.""", reply_markup=get_keyboard_inline_6())

@dp.callback_query_handler(lambda c: c.data == 'go3')
async def go3(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("""Домашние лисы — группа одомашненных лис, выведенных в ходе продолжительного эксперимента в Новосибирском институте цитологии и генетики.
Эксперимент по одомашниванию лис был начат в 1959 году советским генетиком Дмитрием Беляевым и специалистом по поведению животных Людмилой Трут.
В результате была выведена группа лис, схожих по поведению с собаками: они проявляют более социальное поведение как с другими особями, так и с людьми, более игривы и дружелюбны, а также сохраняют юношеские черты в зрелом возрасте.
Домашние лисы живут в Америке, Германии, Нидерландах. Их поведение близко к поведению собаки, но при этом лисицы остаются такими же независимыми, как кошки. Перед продажей лисиц стерилизуют.""", reply_markup=get_keyboard_inline_5())








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
