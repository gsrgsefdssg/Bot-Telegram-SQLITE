import telebot
import sqlite3

bot = telebot.TeleBot('8473742081:AAGiUeuS7LlT4CIn78blpw5fZyj998g8Mo8')

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.reply_to(message, 'Привет! Напиши свое имя и мы тебя зарегистрируем')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    name = message.text.strip()
    bot.reply_to(message, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass, name)

def user_pass(message, name):
    password = message.text.strip()

    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass) VALUES (?, ?)', (name, password))
    conn.commit()
    cur.close()
    conn.close()

    bot.reply_to(message, 'Вы успешно зарегистрированы!')


bot.polling(non_stop=True)