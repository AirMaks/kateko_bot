import telebot
from telebot import types
import const


bot = telebot.TeleBot(const.API_TOKEN)
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

btn_address = types.KeyboardButton('Адреса магазинов', request_location=True)
btn_payment = types.KeyboardButton('Способы оплаты')
btn_delivery = types.KeyboardButton('Способы доставки')
markup_menu.add(btn_address, btn_payment, btn_delivery)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, сегодня тренировка в 18.00, ты придёшь?', reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Способы доставки':
        bot.reply_to(message, "Доставка курьером, самовывоз, почта России", reply_markup=markup_menu)
    elif message.text == "Способы оплаты":
        bot.reply_to(message, "Наличные, По карте, Банковский перевод", reply_markup=markup_menu)
    else:
        bot.reply_to(message, message.text, reply_markup=markup_menu)


bot.polling(none_stop=True, timeout=123)

