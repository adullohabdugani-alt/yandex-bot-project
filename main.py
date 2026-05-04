import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html("<b>Привет, создатель Абдугани!</b> ✨\nЯ твой верный помощник Яндекс. Спрашивай что угодно!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    
    # 1. Приветствие
    if text in ["привет", "хай", "здравствуй"]:
        await update.message.reply_html("👋 <b>Привет, мой создатель Якубов Абдугани!</b> Чем я могу тебе помочь?")
    
    # 2. О создателе
    elif "это кто" in text or "создатель" in text:
        await update.message.reply_html("👑 <b>Это мой создатель Якубов Абдугани</b>")
    
    # 3. О папе
    elif "якубов фуркат убайдуллоевич" in text:
        await update.message.reply_html("👨‍⚕️ <b>Это травматолог-ортопед и папа Якубова Абдугани</b>")
    
    # 4. Математика (включая умножение x и ×)
    elif any(char in text for char in "+-*/×x"):
        try:
            calc_text = text.replace('×', '*').replace('x', '*')
            # Убираем все лишнее, оставляем только цифры и знаки
            safe_text = "".join(c for c in calc_text if c in "0123456789+-*/(). ")
            result = eval(safe_text)
            await update.message.reply_html(f"🔢 <b>Результат:</b> <code>{result}</code>")
        except:
            await update.message.reply_text("Не смог посчитать, напиши пример проще!")
            
    # 5. Фото
    elif "создай фото" in text:
        await update.message.reply_text("🖼️ <b>Я готов рисовать!</b> Опиши, что ты хочешь увидеть на фото?")
        
    else:
        await update.message.reply_text("Я Яндекс🤖. Спроси про создателя или напиши пример!")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
