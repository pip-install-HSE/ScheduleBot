
from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Узнать_расписание')
kb_client = ReplyKeyboardMarkup()
kb_client.add(b1)



TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
res = []

@dp.message_handler(commands=['Узнать_расписание'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id, str(res))

@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    markup = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton("Могу", callback_data="but_1") #"but_Mon00-Yes"
    but_2 = InlineKeyboardButton("Не удобно", callback_data="but_2")
    but_3 = InlineKeyboardButton("Не могу", callback_data="but_3")

    markup.add(but_1)
    markup.add(but_2)
    markup.add(but_3)
    await bot.send_message(message.chat.id, "привет", reply_markup=kb_client)
    await bot.send_message(message.chat.id, "Понедельник 00.00-06.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Понедельник 06.00-12.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Понедельник 12.00-18.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Понедельник 18.00-24.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Вторник 00.00-06.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Вторник 06.00-12.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Вторник 12.00-18.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Вторник 18.00-24.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Среда 00.00-06.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Среда 06.00-12.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Среда 12.00-18.00", reply_markup=markup)
    await bot.send_message(message.chat.id, "Среда 18.00-24.00", reply_markup=markup)

@dp.callback_query_handler(Text(startswith="but_"))
async def buttom_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    res.append(str(call.data.split('_')[1]))
    #await bot.send_message(call.message.chat.id, str(res))
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)




executor.start_polling(dp, skip_updates=True)
