    # Подготовка текста для проверки
    text_low = text.lower()

    # --- БЛОК 1: КРУТОЙ ДИЗАЙН ПРО СОЗДАТЕЛЯ ---
    if any(word in text_low for word in ["кто создатель", "создатель", "кто тебя сделал"]):
        caption = (
            "<b>─── 🧬 SYSTEM INFO ───</b>\n\n"
            "👤 <b>Creator:</b> <code>Обувь Абдугани</code>\n"
            "⭐ <i>Status: Lead Developer</i>\n\n"
            "👨‍⚕️ <b>Family Root:</b>\n"
            "└ <b>Якубов Фуркат Убайдуллоевич</b>\n"
            "   👨‍⚕️ <code>Травматолог-ортопед</code>\n"
            "   🏥 <i>Professional Medical Support</i>\n\n"
            "<b>──────────────────</b>"
        )
        # Если хочешь, можно добавить ссылку на фото создателя
        await update.message.reply_html(caption)

    # --- БЛОК 2: ПРОФЕССИОНАЛЬНЫЙ ОТВЕТ ПРО ПАПУ ---
    elif "фуркат" in text_low or "травматолог" in text_low:
        doctor_card = (
            "<b>🏥 КАРТОЧКА СПЕЦИАЛИСТА</b>\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "👨‍⚕️ <b>Врач:</b> Якубов Фуркат Убайдуллоевич\n"
            "🩺 <b>Специализация:</b> Травматолог-ортопед\n"
            "💎 <b>Опыт:</b> Высшая категория\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "<i>Лучший специалист в своей области!</i>"
        )
        await update.message.reply_html(doctor_card)

    # --- БЛОК 3: ГЕНЕРАЦИЯ ФОТО (С КРУТЫМ ДИЗАЙНОМ) ---
    elif text_low.startswith("создай ") or text_low.startswith("рисуй "):
        prompt = text.replace("создай ", "").replace("рисуй ", "")
        
        waiting_msg = await update.message.reply_html("<b>🎨 ИИ генерирует ваш шедевр...</b>\n<code>[▒▒▒▒▒▒▒▒▒▒] 0%</code>")
        
        # Ссылка на генерацию
        image_url = f"https://pollinations.ai{prompt}?width=1024&height=1024&model=flux"
        
        try:
            await waiting_msg.edit_text("<b>🎨 Фото готово! Отправляю...</b>", parse_mode='HTML')
            await update.message.reply_photo(
                photo=image_url, 
                caption=f"<b>🖼 Результат генерации:</b>\n«<code>{prompt}</code>»",
                parse_mode='HTML'
            )
        except:
            await update.message.reply_text("❌ Ошибка при связи с нейросетью.")

    # --- БЛОК 4: УМНАЯ МАТЕМАТИКА ---
    elif any(char in text for char in "+-*/"):
        try:
            safe_text = "".join(c for c in text if c in "0123456789+-*/.()")
            result = eval(safe_text)
            await update.message.reply_html(f"<b>🔢 CALCULATOR</b>\n└ <b>Результат:</b> <code>{result}</code>")
        except:
            pass # Если это не пример, просто молчим
