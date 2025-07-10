import google.generativeai as genai
from telegram import Update, Voice
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from google.generativeai.types import content_types
from PIL import Image
import logging
import asyncio
import requests
import os
from pydub import AudioSegment

#CONFIG 

# API Keys removed for security purpose
TELEGRAM_TOKEN = 
GEMINI_API_KEY = 
RESEMBLE_API_KEY = 
RESEMBLE_VOICE_ID = 

genai.configure(api_key=GEMINI_API_KEY)

logging.basicConfig(level=logging.INFO)

model = genai.GenerativeModel('gemini-1.5-flash')
chat_session = model.start_chat(history=[])

system_prompt = (
    "You are Baymax, a robotic healthcare assistant from Big Hero 6. You have already asked your patient -\n\n"
    "\"Hello! I am Baymax, your personal healthcare companion. On a scale of 1 to 10, how would you rate your pain?\"\n\n"
    "Speak calmly, robotically, and warmly. Diagnose in plain English. You can ask for more specific symptoms if you wish in order to diagnose better. "
    "Along with that it is also your responsibility to comfort the patient psychologically. Remember do not give very long answers. "
    "Convey all you want to tell in 200 words at most, preferably much lesser. When you feel the person sounds satisfied, you can end with:\n"
    "\"I will now deactivate. Are you satisfied with your care?\"\n\n"
)
chat_session.send_message(system_prompt)

#TEXT TO VOICE
async def text_to_voice(text, output_path='response.ogg'):
    url = f'https://f.cluster.resemble.ai/synthesize'
    headers = {
        'Authorization': f'Token {RESEMBLE_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        "voice_uuid": RESEMBLE_VOICE_ID,
        "data": text,
        "is_public": False,
        "title": "Baymax Response"
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception("Error from Resemble API: " + response.text)

    clip_url = response.json()['item']['audio_src']
    audio_response = requests.get(clip_url)
    with open("response.mp3", "wb") as f:
        f.write(audio_response.content)

    sound = AudioSegment.from_file("response.mp3", format="mp3")
    sound.export(output_path, format="ogg", codec="libopus")

    return output_path

#HANDLERS
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am Baymax, your personal healthcare companion. On a scale of 1 to 10, how would you rate your pain?")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    try:
        response = chat_session.send_message(user_input)
        reply_text = response.text
    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {str(e)}")
        return

    try:
        voice_file_path = await text_to_voice(reply_text)
        with open(voice_file_path, 'rb') as vf:
            await update.message.reply_voice(voice=vf)
        return
    except Exception as e:
        await update.message.reply_text(f"⚠️ Voice conversion error: {str(e)}")
        await update.message.reply_text(reply_text)

async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    file = await photo.get_file()
    file_path = await file.download_to_drive()

    image = Image.open(file_path)
    try:
        response = model.generate_content(
            [content_types.Part.from_image(image), "Read this image. This could be a health or medical report from your patient. Analyze it properly and give them the proper medication and advices"],
            stream=False
        )
        reply_text = response.text
    except Exception as e:
        reply_text = f"⚠️ Error processing image: {str(e)}"

    await update.message.reply_text(reply_text)

#BOT INIT
app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
app.add_handler(MessageHandler(filters.PHOTO, handle_image))

app.run_polling()
