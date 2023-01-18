import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
from bs4 import BeautifulSoup as BS

#BBBBBBBOOOOOOOOOOOOOOTTTTTTTTTTTT
API_TOKEN = '5737745294:AAFHBgmpRnlTT0PdSwQPUpL2v6GyVQiOCOY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#кнопки
@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    mar = types.InlineKeyboardMarkup(row_width=2)
    kolizei = types.InlineKeyboardButton(text="Колизей", callback_data="ko")
    smena = types.InlineKeyboardButton(text="Смена", callback_data="sm")
    kolizeim = types.InlineKeyboardButton(text="Колизей(Макси)", callback_data="km")
    jam = types.InlineKeyboardButton(text="КиноДжем", callback_data="Ja")
    globus = types.InlineKeyboardButton(text="Глобус", callback_data="gl")
    mar.add(kolizei, kolizeim,smena,jam,globus)
    await message.answer("Привет, выбери кинотеатр где ты хочешь купить билет.", reply_markup=mar)
hed = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36'
}
r = requests.get(url="https://kinosmena.ru/", headers=hed)

html = BS(r.content,'html.parser')

g = []
for el in html.find_all("div", class_='EventList__Event-sc-14wck6-3 dKUEol event rental large'):
    t = el.find_all("a",class_="event-name")
    g.append(t[0].text)

for el in html.find_all("div", class_='EventList__Event-sc-14wck6-3 dKUEol event rental pushkin-card large'):
    t = el.find_all("a",class_="event-name")
    g.append(t[0].text)

@dp.callback_query_handler(text="sm")
async def v1(call: types.CallbackQuery):
    mar = types.InlineKeyboardMarkup(row_width=2)
    but = []
    for i in range(len(g)):
        but.append(types.InlineKeyboardButton(text=g[i], callback_data=g[i]))
    mar.add(*but)
    await call.answer("Выберите фильм", reply_markup=mar)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)