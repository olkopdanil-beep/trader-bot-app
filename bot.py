import os
from dotenv import load_dotenv

load_dotenv()

import telebot
from telebot import types


BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
WEBAPP_URL = os.getenv("WEBAPP_URL", "http://localhost:8080/frontend/index.html").strip()

if not BOT_TOKEN:
    raise RuntimeError("Set BOT_TOKEN environment variable")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start"])
def start(message: types.Message) -> None:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_btn = types.KeyboardButton(
        text="Открыть анализатор графика",
        web_app=types.WebAppInfo(WEBAPP_URL),
    )
    markup.add(webapp_btn)

    bot.send_message(
        message.chat.id,
        (
            "Привет! Это AI анализатор торговых графиков.\n\n"
            "Нажмите кнопку ниже, загрузите скриншот графика и получите сигнал."
        ),
        reply_markup=markup,
    )


@bot.message_handler(content_types=["web_app_data"])
def web_app_data_handler(message: types.Message) -> None:
    # Optional handler if the WebApp sends data back via Telegram.WebApp.sendData(...)
    bot.send_message(message.chat.id, "Данные из Mini App получены.")


if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling(skip_pending=True)
