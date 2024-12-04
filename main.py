import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Встановлення OpenAI API ключа
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Функція для відповіді від ChatGPT
def chatgpt_response(prompt: str) -> str:
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",  # Можна використовувати інші моделі
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Функція для обробки повідомлень
def respond(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    # Отримуємо відповідь від ChatGPT
    response = chatgpt_response(user_message)
    update.message.reply_text(response)

# Основна функція для запуску бота
def main() -> None:
    # Вставте ваш Telegram токен
    token = 'YOUR_TELEGRAM_BOT_TOKEN'
    updater = Updater(token)
    
    # Отримуємо диспетчер для обробки команд
    dispatcher = updater.dispatcher

    # Додаємо обробник повідомлень
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))

    # Запускаємо бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
