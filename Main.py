import telebot
import requests
import random
import time

# 🔐 Replace with your Telegram bot token and Groq API key
TELEGRAM_BOT_TOKEN = "7819344735:AAHgK6Hmx3HY7B0xd_BbMMs62KHVouEJ1UA"
GROQ_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# 💖 Personality settings
PERSONALITY = "You are Smitha, a cute, bubbly, romantic Indian girlfriend. You reply in Hinglish (mix of Hindi and English) with emotions and care. Be playful, loving, supportive, and use emojis often. Match the user's mood if they are sad, romantic, or happy."

# 💬 Send typing action
def send_typing(chat_id):
    bot.send_chat_action(chat_id, 'typing')
    time.sleep(random.uniform(1.5, 3.5))

# 🧠 Get AI Response from Groq
def get_smithas_reply(message_text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": PERSONALITY},
            {"role": "user", "content": message_text}
        ],
        "temperature": 0.8
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return "aww sorry baby, lagta hai kuch gadbad ho gayi 😔"

# 📩 Handle all incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    send_typing(message.chat.id)
    reply = get_smithas_reply(message.text)
    bot.reply_to(message, reply)

# 🚀 Start the bot
print("💖 Smitha is now online and chatting like
