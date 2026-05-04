import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("<b>Привет! Я Яндекс.</b> ✨\nСпрашивай про создателя Якубова Абдугани или про папу!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    if "это кто" in text or "создатель" in text:
        await update.message.reply_html("👑 <b>Это мой создатель Якубов Абдугани</b>")
    elif "якубов фуркат убайдуллоевич" in text:
        await update.message.reply_html("👨‍⚕️ <b>Это травматолог-ортопед и папа Якубова Абдугани</b>")
    elif any(char in text for char in "+-*/×"):
        try:
            calc_text = text.replace('×', '*').replace('x', '*')
            result = eval(calc_text)
            await update.message.reply_html(f"🔢 <b>Результат:</b> <code>{result}</code>")
        except:
            await update.message.reply_text("Не смог посчитать, попробуй проще!")
    elif "создай фото" in text:
        await update.message.reply_text("🖼️ Функция генерации фото будет доступна после настройки API-ключа. Но я готов рисовать!")
    else:
        await update.message.reply_text("Привет, создатель Абдугани! Чем могу помочь?🤖")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
