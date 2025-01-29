import telebot
import os

# Получение API-токена из переменной окружения
API_TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(f"Received message from {message.chat.id}: {message.text}")
    //bot.reply_to(message, message.text)

if __name__ == '__main__':
    print("Starting the bot...")
    try:
        while True:
            bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(5)  # Пауза перед повторным запуском
