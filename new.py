import telebot
from telebot import types
from datetime import datetime
from zoneinfo import ZoneInfo
import threading
import random
now = datetime.now(ZoneInfo("Asia/Tashkent"))
# Hozirgi sana-vaqtni olish

current_date = now.strftime("%d.%m.%Y")    # 08.12.2025
current_time = now.strftime("%H:%M:%S")    # 14:35:20



BOT_TOKEN = "8538888273:AAEvheo3TLnHsnhWXJVRohfJ89k_qq6d6GY"
CHANNEL_ID = "@bright_future_asakaa"

bot = telebot.TeleBot(BOT_TOKEN)

ADMIN_IDS = [5552666379]  # bu yerga o'zingizning telegram id yozing
QUIZ_CHANNEL_ID = "@bright_future_asakaa"  # natija shu kanalga boradi


user_data = {}

def start_process(chat_id):
    user_data[chat_id] = {"step": "wait_media"}
    bot.send_message(chat_id, "Rasm yoki video tashlang 📷🎥")


excel_tasks = [
    "tasks/excel1.jpg",
    "tasks/excel2.jpg",
    "tasks/excel3.jpg",
    "excel4.jpg",
    "excel6.jpg",
    "excel7.jpg",
    "excel77.jpg",
    "excel8.jpg",
    "excel88.jpg",
    "excel9.jpg",
    "excel10.jpg",
    "excel11.jpg",
    "excel12.jpg",
]
word_tasks = [
    "tasks/word1.jpg",
    "tasks/word2.jpg",
    "tasks/word3.jpg",
    "tasks/word4.jpg",
    "tasks/word5.jpg",
    "tasks/word6.jpg",
    "tasks/word7.jpg",
    "tasks/word8.jpg",
]

powerpoint_tasks = [
    "vazifa1.mp4",
    "vazifa2.mp4",
    "vazifa3.mp4",
    "vazifa4.mp4",
    "vazifa5.mp4",
]


def funksiyalar():
    keyboard = types.InlineKeyboardMarkup()
    prev_btn = types.InlineKeyboardButton(
        "Word tezkor tugmalar ⌨️",
        callback_data="tezkor"
    )
    next_btn = types.InlineKeyboardButton(
        "Excel funksiyalar 📚",
        callback_data="excel"
    )

    keyboard.row(prev_btn, next_btn)
    return keyboard

def task_keyboard(index):
    keyboard = types.InlineKeyboardMarkup()
    prev_btn = types.InlineKeyboardButton("◀️ Oldingi", callback_data=f"excel_prev_{index}")
    next_btn = types.InlineKeyboardButton("▶️ Keyingi", callback_data=f"excel_next_{index}")
    center_btn = types.InlineKeyboardButton(f"{index+1}/{len(excel_tasks)}", callback_data="none")

    keyboard.row(prev_btn, center_btn, next_btn)
    return keyboard

def task_keyboard_ppt(index):
    keyboard = types.InlineKeyboardMarkup()
    prev_btn = types.InlineKeyboardButton("◀️ Oldingi", callback_data=f"ppt_prev_{index}")
    next_btn = types.InlineKeyboardButton("▶️ Keyingi", callback_data=f"ppt_next_{index}")
    center_btn = types.InlineKeyboardButton(f"{index+1}/{len(powerpoint_tasks)}", callback_data="ppt_none")

    keyboard.row(prev_btn, center_btn, next_btn)
    return keyboard


def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add("Word vazifa", "Excel vazifa")
    kb.add("PowerPoint vazifa", "📝 Quiz")
    kb.add("Yodlash uchun", "💎 vazifa qoshish")
    return kb


def check_subscription(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False


quiz_questions = {
    "Word": [
        {"q": "Ctrl + C nima qiladi?", "options": ["A) Kesadi", "B) Nusxalaydi", "C) Saqlaydi"], "answer": "B"},
        {"q": "Ctrl + P nima qiladi?", "options": ["A) Chop etish", "B) Yopish", "C) O'chirish"], "answer": "A"},
        {"q": "Ctrl + V nima qiladi?", "options": ["A) Nusxalaydi", "B) Joylashtiradi", "C) Yopadi"], "answer": "B"},
        {"q": "Ctrl + Z nima qiladi?", "options": ["A) Qaytaradi", "B) Bekor qiladi", "C) Saqlaydi"], "answer": "B"},
        {"q": "Ctrl + S nima qiladi?", "options": ["A) Saqlaydi", "B) Yopadi", "C) Chop etadi"], "answer": "A"},
        {"q": "Ctrl + O nima qiladi?", "options": ["A) Faylni ochadi", "B) Yopadi", "C) Saqlaydi"], "answer": "A"},
        {"q": "Ctrl + N nima qiladi?", "options": ["A) Yangi hujjat", "B) Yopadi", "C) Nusxalaydi"], "answer": "A"},
        {"q": "Ctrl + B nima qiladi?", "options": ["A) Italic", "B) Qalin", "C) Tagiga chiziq"], "answer": "B"},
        {"q": "Ctrl + I nima qiladi?", "options": ["A) Qalin", "B) Italic", "C) Tagiga chiziq"], "answer": "B"},
        {"q": "Ctrl + U nima qiladi?", "options": ["A) Qalin", "B) Italic", "C) Tagiga chiziq"], "answer": "C"},
        {"q": "Ctrl + L nima qiladi?", "options": ["A) Chapga tekislash", "B) O‘ngga tekislash", "C) Markazlash"], "answer": "A"},
        {"q": "Ctrl + R nima qiladi?", "options": ["A) Chapga tekislash", "B) O‘ngga tekislash", "C) Markazlash"], "answer": "B"},
        {"q": "Ctrl + E nima qiladi?", "options": ["A) Chapga", "B) O‘ngga", "C) Markazlash"], "answer": "C"},
        {"q": "Ctrl + F nima qiladi?", "options": ["A) Qidirish", "B) Chop etish", "C) Yopish"], "answer": "A"},
        {"q": "Ctrl + K nima qiladi?", "options": ["A) Hyperlink qo‘shadi", "B) Faylni yopadi", "C) Saqlaydi"], "answer": "A"},
    ],
    "Excel": [
        {"q": "SUM funksiyasi nima qiladi?", "options": ["A) Ayiradi", "B) Qo‘shadi", "C) Bo‘ladi"], "answer": "B"},
        {"q": "MAX funksiyasi nima qiladi?", "options": ["A) Eng kichik", "B) O‘rtacha", "C) Eng katta"], "answer": "C"},
        {"q": "MIN funksiyasi nima qiladi?", "options": ["A) Eng katta", "B) Eng kichik", "C) O‘rtacha"], "answer": "B"},
        {"q": "AVERAGE funksiyasi nima qiladi?", "options": ["A) Bo‘ladi", "B) O‘rtacha", "C) Eng katta"], "answer": "B"},
        {"q": "IF funksiyasi nima qiladi?", "options": ["A) Shart tekshiradi", "B) Qo‘shadi", "C) Bo‘ladi"], "answer": "A"},
        {"q": "VLOOKUP nima qiladi?", "options": ["A) Jadval ustunidan qidiradi", "B) Satrdan qidiradi", "C) Hamma katakni sanaydi"], "answer": "A"},
        {"q": "HLOOKUP nima qiladi?", "options": ["A) Satrdan qidiradi", "B) Jadval ustunidan qidiradi", "C) Qo‘shadi"], "answer": "A"},
        {"q": "UPPER nima qiladi?", "options": ["A) Kichik harf", "B) Katta harf", "C) Hech narsa"], "answer": "B"},
        {"q": "LOWER nima qiladi?", "options": ["A) Kichik harf", "B) Katta harf", "C) Hech narsa"], "answer": "A"},
        {"q": "PROPER nima qiladi?", "options": ["A) Hamma bosh harf", "B) Kichik", "C) Hech narsa"], "answer": "A"},
        {"q": "ROUND nima qiladi?", "options": ["A) Yaxlitlaydi", "B) Bo‘ladi", "C) Qo‘shadi"], "answer": "A"},
        {"q": "NOW nima qiladi?", "options": ["A) Sana va vaqt", "B) Faol bo‘ladi", "C) Hech narsa"], "answer": "A"},
        {"q": "TODAY nima qiladi?", "options": ["A) Hozirgi sana", "B) Qo‘shadi", "C) Bo‘ladi"], "answer": "A"},
        {"q": "ABS nima qiladi?", "options": ["A) Modul", "B) Bo‘ladi", "C) O‘chadi"], "answer": "A"},
        {"q": "PMT nima qiladi?", "options": ["A) Kredit to‘lovi", "B) Bo‘ladi", "C) Qo‘shadi"], "answer": "A"},
    ],
    "PowerPoint": [
        {"q": "F5 nima qiladi?", "options": ["A) Saqlaydi", "B) Slideshow boshlaydi", "C) Yopadi"], "answer": "B"},
        {"q": "Ctrl + M nima qiladi?", "options": ["A) Yangi slayd", "B) Yopadi", "C) Saqlaydi"], "answer": "A"},
        {"q": "Ctrl + D nima qiladi?", "options": ["A) Nusxalaydi", "B) O‘chadi", "C) Saqlaydi"], "answer": "A"},
        {"q": "Ctrl + P nima qiladi?", "options": ["A) Chop etish", "B) Slayd qo‘shish", "C) Saqlash"], "answer": "A"},
        {"q": "Alt + F5 nima qiladi?", "options": ["A) Slideshow boshlaydi", "B) Yopadi", "C) Saqlaydi"], "answer": "A"},
        {"q": "F2 nima qiladi?", "options": ["A) Edit slayd", "B) O‘chadi", "C) Saqlaydi"], "answer": "A"},
        {"q": "Ctrl + G nima qiladi?", "options": ["A) Go to slide", "B) Yopadi", "C) Saqlaydi"], "answer": "A"},
        {"q": "Ctrl + Shift + C nima qiladi?", "options": ["A) Format nusxasi", "B) Chop etadi", "C) Yopadi"], "answer": "A"},
        {"q": "Ctrl + Shift + V nima qiladi?", "options": ["A) Format joylashtirish", "B) O‘chadi", "C) Saqlaydi"], "answer": "A"},
        {"q": "Ctrl + E nima qiladi?", "options": ["A) Markazlash", "B) Chapga", "C) O‘ngga"], "answer": "A"},
        {"q": "Ctrl + L nima qiladi?", "options": ["A) Chapga tekislash", "B) Markaz", "C) O‘ngga"], "answer": "A"},
        {"q": "Ctrl + R nima qiladi?", "options": ["A) O‘ngga tekislash", "B) Chapga", "C) Markaz"], "answer": "A"},
        {"q": "Ctrl + Shift + > nima qiladi?", "options": ["A) Katta shrift", "B) Kichik", "C) Hech narsa"], "answer": "A"},
        {"q": "Ctrl + Shift + < nima qiladi?", "options": ["A) Kichik shrift", "B) Katta", "C) Hech narsa"], "answer": "A"},
        {"q": "Alt + N nima qiladi?", "options": ["A) Yangi slayd", "B) Chop", "C) Yopish"], "answer": "A"},
    ]
}
quiz_users = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    if check_subscription(user_id):
        bot.send_message(
            message.chat.id,
            "Assalomu alaykum! Siz allaqachon obuna bo'lgansiz ✔️\n\nAsosiy menyudan foydalanishingiz mumkin.",
            reply_markup=main_menu()
        )
    else:
        kb = types.InlineKeyboardMarkup()
        kb.add(
            types.InlineKeyboardButton("📢 Kanalga obuna bo‘lish", url=f"https://t.me/{CHANNEL_ID[1:]}"),
            types.InlineKeyboardButton("✔️ Tasdiqlash", callback_data="check_sub")
        )
        bot.send_message(
            message.chat.id,
            "❗ Botdan foydalanish uchun quyidagi kanalga obuna bo‘ling:",
            reply_markup=kb
        )

# --- Tasdiqlash tugmasini bosganda ---
@bot.callback_query_handler(func=lambda call: call.data == "check_sub")
def check_sub(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id

    if check_subscription(user_id):
        bot.edit_message_text(
            "🎉 Siz muvaffaqiyatli obuna bo'ldingiz!\n\nAsosiy menyuga xush kelibsiz 👇",
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=None
        )
        bot.send_message(chat_id, "Asosiy menyu:", reply_markup=main_menu())
    else:
        kb = types.InlineKeyboardMarkup()
        kb.add(
            types.InlineKeyboardButton("📢 Kanalga obuna bo‘lish", url=f"https://t.me/{CHANNEL_ID[1:]}"),
            types.InlineKeyboardButton("✔️ Yana tekshirish", callback_data="check_sub")
        )
        bot.answer_callback_query(call.id, "❌ Obuna topilmadi!")
        bot.edit_message_text(
            "❗ Siz hali obuna bo‘lmagansiz. Iltimos, avval obuna bo‘ling.",
            chat_id=chat_id,
            message_id=call.message.message_id,
            reply_markup=kb
        )


def task_keyboard_excel(index):
    keyboard = types.InlineKeyboardMarkup()
    prev_btn = types.InlineKeyboardButton("◀️ Oldingi", callback_data=f"excel_prev_{index}")
    next_btn = types.InlineKeyboardButton("▶️ Keyingi", callback_data=f"excel_next_{index}")
    center_btn = types.InlineKeyboardButton(f"{index+1}/{len(excel_tasks)}", callback_data="excel_none")

    keyboard.row(prev_btn, center_btn, next_btn)
    return keyboard

# --- Word knopkalar ---
def task_keyboard_word(index):
    keyboard = types.InlineKeyboardMarkup()
    prev_btn = types.InlineKeyboardButton("◀️ Oldingi", callback_data=f"word_prev_{index}")
    next_btn = types.InlineKeyboardButton("▶️ Keyingi", callback_data=f"word_next_{index}")
    center_btn = types.InlineKeyboardButton(f"{index+1}/{len(word_tasks)}", callback_data="word_none")

    keyboard.row(prev_btn, center_btn, next_btn)
    return keyboard


# --- Excel vazifa bosilganda ---
@bot.message_handler(func=lambda m: m.text == "Excel vazifa")
def excel_start(message):
    chat_id = message.chat.id

    with open(excel_tasks[0], "rb") as img:
        bot.send_photo(
            chat_id,
            img,
            caption="Excel vazifa 1",
            reply_markup=task_keyboard_excel(0)
        )


# --- Word vazifa bosilganda ---
@bot.message_handler(func=lambda m: m.text == "Word vazifa")
def word_start(message):
    chat_id = message.chat.id

    with open(word_tasks[0], "rb") as img:
        bot.send_photo(
            chat_id,
            img,
            caption="Word vazifa 1",
            reply_markup=task_keyboard_word(0)
        )



@bot.message_handler(func=lambda m: m.text == "📝 Quiz")
def choose_quiz(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("Word Quiz", "Excel Quiz", "PowerPoint Quiz")
    kb.add("⬅️ Orqaga")
    bot.send_message(message.chat.id, "Bo‘limni tanlang:", reply_markup=kb)

# ================= TIMER =================

def start_quiz_timer(chat_id):
    def timeout():
        if chat_id in quiz_users:
            user = quiz_users[chat_id]
            score = user["score"]
            total = len(user["questions"])

            bot.send_message(chat_id, f"⏰ Vaqt tugadi!\nNatija: {score}/{total}", reply_markup=main_menu())
            send_result(chat_id, score, total)
            del quiz_users[chat_id]

    timer = threading.Timer(1800, timeout)
    timer.start()

# ================= QUIZ BOSHLASH =================

@bot.message_handler(func=lambda m: m.text in ["Word Quiz", "Excel Quiz", "PowerPoint Quiz"])
def start_quiz(message):
    chat_id = message.chat.id
    subject = message.text.split()[0]

    questions = random.sample(quiz_questions[subject], len(quiz_questions[subject]))

    quiz_users[chat_id] = {
        "subject": subject,
        "questions": questions,
        "index": 0,
        "score": 0
    }

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🛑 Testni to‘xtatish")

    bot.send_message(chat_id, f"✅ {subject} testi boshlandi!\n⏳ Sizda 30 daqiqa vaqt bor.", reply_markup=kb)

    send_question(chat_id)

# ================= SAVOL YUBORISH =================

def send_question(chat_id):
    user = quiz_users[chat_id]
    index = user["index"]
    q = user["questions"][index]

    markup = types.InlineKeyboardMarkup()
    for opt in q["options"]:
        # Agar foydalanuvchi avval tanlagan bo'lsa ✅ qo'shish
        chosen = user.get("answers", {}).get(index)
        label = ("✅ " + opt) if chosen == opt[0] else opt
        markup.add(types.InlineKeyboardButton(label, callback_data=f"ans|{opt[0]}"))

    nav = []
    if index > 0:
        nav.append(types.InlineKeyboardButton("⬅️ Oldingi", callback_data="prev"))
    if index < len(user["questions"]) - 1:
        nav.append(types.InlineKeyboardButton("➡️ Keyingi", callback_data="next"))
    markup.row(*nav)

    text = f"❓ {q['q']}"

    last_msg_id = user.get("last_message_id")
    if last_msg_id:
        try:
            bot.edit_message_text(text, chat_id, last_msg_id, reply_markup=markup)
            return
        except:
            pass

    msg = bot.send_message(chat_id, text, reply_markup=markup)
    user["last_message_id"] = msg.message_id
# ================= JAVOB / NAVIGATION =================



# ================= STOP TUGMA =================

@bot.message_handler(func=lambda m: m.text == "🛑 Testni to‘xtatish")
def stop_quiz(message):
    chat_id = message.chat.id
    user = quiz_users.get(chat_id)
    if not user:
        bot.send_message(chat_id, "Aktiv test yo‘q.", reply_markup=main_menu())
        return

    score = user["score"]
    total = len(user["questions"])
    bot.send_message(chat_id, f"🛑 Test to‘xtatildi.\nNatija: {score}/{total}", reply_markup=main_menu())
    send_result(chat_id, score, total)
    del quiz_users[chat_id]

# ================= KANALGA NATIJA =================

def send_result(chat_id, score, total):
    user_info = bot.get_chat(chat_id)
    text = f"📊 Quiz natijasi\n👤 {user_info.first_name}\n📚 {quiz_users.get(chat_id, {}).get('subject','')}\n✅ {score}/{total}\n📅 {current_date} ⏰ {current_time}"
    bot.send_message(CHANNEL_ID, text)

# ================= JAVOB TEKSHIRISH =================


# ================= STOP TUGMA =================

@bot.message_handler(func=lambda m: m.text == "🛑 Testni to‘xtatish")
def stop_quiz(message):
    chat_id = message.chat.id

    if chat_id not in quiz_users:
        bot.send_message(chat_id, "Aktiv test yo‘q.", reply_markup=main_menu())
        return



    user = quiz_users[chat_id]
    score = user["score"]
    total = len(user["questions"])

    bot.send_message(chat_id, f"🛑 Test to‘xtatildi.\nNatija: {score}/{total}", reply_markup=main_menu())
    send_result(chat_id, score, total)
    del quiz_users[chat_id]

# ================= KANALGA NATIJA =================

def send_result(chat_id, score, total):
    user = bot.get_chat(chat_id)

    text = (
        f"📊 Quiz natijasi\n\n"
        f"👤 {user.first_name}\n"
        f"📚 {quiz_users.get(chat_id, {}).get('subject','')}\n"
        f"✅ {score}/{total}\n"
        f"📅 {current_date} ⏰ {current_time}"
    )

    bot.send_message(CHANNEL_ID, text)

# ================= ADMIN PANEL =================

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id not in ADMIN_IDS:
        return

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("📊 Statistika", "👥 Aktiv testlar")
    kb.add("⬅️ Orqaga")

    bot.send_message(message.chat.id, "Admin panel:", reply_markup=kb)

@bot.message_handler(func=lambda m: m.text == "📊 Statistika")
def stats(message):
    if message.from_user.id not in ADMIN_IDS:
        return

    bot.send_message(message.chat.id, f"Aktiv testlar soni: {len(quiz_users)}")

@bot.message_handler(func=lambda m: m.text == "👥 Aktiv testlar")
def active_users(message):
    if message.from_user.id not in ADMIN_IDS:
        return

    if not quiz_users:
        bot.send_message(message.chat.id, "Aktiv test yo‘q.")
        return

    text = "🟢 Aktiv testlar:\n\n"
    for user_id in quiz_users:
        user = bot.get_chat(user_id)
        text += f"{user.first_name} ({user_id})\n"

    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: m.text == "Yodlash uchun")
def yodla(message):
    chat_id = message.chat.id

    bot.send_message(
        chat_id,
        "Qaysi birini tanlaysiz?",
        reply_markup=funksiyalar()
    )

@bot.message_handler(func=lambda m: m.text == "PowerPoint vazifa")
def ppt_start(message):
    chat_id = message.chat.id

    with open(powerpoint_tasks[0], "rb") as vid:
        bot.send_video(
            chat_id,
            vid,
            caption="PowerPoint vazifa 1",
            reply_markup=task_keyboard_ppt(0)
        )


@bot.callback_query_handler(func=lambda call: call.data.startswith("excel_"))
def excel_callbacks(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    data = call.data.split("_")
    action = data[1]
    index = int(data[2])

    if action == "next":
        new_index = index + 1
        if new_index >= len(excel_tasks):
            new_index = 0

    elif action == "prev":
        new_index = index - 1
        if new_index < 0:
            new_index = len(excel_tasks) - 1

    # Yangi rasmni yuborish
    with open(excel_tasks[new_index], "rb") as img:
        new_media = types.InputMediaPhoto(img, caption=f"Excel vazifa {new_index+1}")

        bot.edit_message_media(
            media=new_media,
            chat_id=chat_id,
            message_id=msg_id,
            reply_markup=task_keyboard_excel(new_index)
        )


@bot.callback_query_handler(func=lambda call: call.data.startswith("word_"))
def word_callbacks(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    data = call.data.split("_")
    action = data[1]
    index = int(data[2])

    if action == "next":
        new_index = index + 1
        if new_index >= len(word_tasks):
            new_index = 0

    elif action == "prev":
        new_index = index - 1
        if new_index < 0:
            new_index = len(word_tasks) - 1

    # Yangi rasmni yuborish
    with open(word_tasks[new_index], "rb") as img:
        new_media = types.InputMediaPhoto(img, caption=f"Word vazifa {new_index+1}")

        bot.edit_message_media(
            media=new_media,
            chat_id=chat_id,
            message_id=msg_id,
            reply_markup=task_keyboard_word(new_index)
        )

@bot.message_handler(commands=['add'])
def add(message):
    start_process(message.chat.id)


@bot.callback_query_handler(func=lambda call: call.data == "tezkor")
def word_tezkor(call):
    text = (
        "📘 *Microsoft Word tezkor tugmalari*\n\n"
        "1. Ctrl + C — Nusxalash\n"
        "2. Ctrl + X — Kesish\n"
        "3. Ctrl + V — Joylashtirish\n"
        "4. Ctrl + Z — Bekor qilish\n"
        "5. Ctrl + S — Saqlash\n"
        "6. Ctrl + O — Faylni ochish\n"
        "7. Ctrl + N — Yangi hujjat\n"
        "8. Ctrl + P — Chop etish\n"
        "9. Ctrl + A — Hammasini belgilash\n"
        "10. Ctrl + F — Qidirish\n"
        "11. Ctrl + B — Qalin (Bold)\n"
        "12. Ctrl + I — Italic\n"
        "13. Ctrl + U — Tagiga chiziq\n"
        "14. Ctrl + L — Chapga tekislash\n"
        "15. Ctrl + R — O‘ngga tekislash\n"
        "16. Ctrl + E — Markazlash\n"
        "17. Ctrl + J — Justify\n"
        "18. Ctrl + K — Hyperlink\n"
        "19. Ctrl + Y — Qayta bajarish\n"
        "20. Ctrl + F4 — Hujjatni yopish"
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("ppt_"))
def ppt_callbacks(call):
    chat_id = call.message.chat.id
    msg_id = call.message.message_id

    data = call.data.split("_")
    action = data[1]
    index = int(data[2])

    if action == "next":
        new_index = index + 1
        if new_index >= len(powerpoint_tasks):
            new_index = 0

    elif action == "prev":
        new_index = index - 1
        if new_index < 0:
            new_index = len(powerpoint_tasks) - 1

    with open(powerpoint_tasks[new_index], "rb") as vid:
        new_media = types.InputMediaVideo(vid, caption=f"PowerPoint vazifa {new_index+1}")

        bot.edit_message_media(
            media=new_media,
            chat_id=chat_id,
            message_id=msg_id,
            reply_markup=task_keyboard_ppt(new_index)
        )


@bot.callback_query_handler(func=lambda call: call.data == "excel")
def excel_funksiyalar(call):
    text = (
        "📊 *Microsoft Excel asosiy funksiyalari*\n\n"
        "🔹 *SUM* – СУММ → Sonlarni qo‘shadi\n\n"
        "🔹 *AVERAGE* – СРЗНАЧ → O‘rtacha qiymatni hisoblaydi\n\n"
        "🔹 *IF* – ЕСЛИ → Shart tekshiradi va natijaga qarab qiymat qaytaradi\n\n"
        "🔹 *VLOOKUP* – ВПР → Jadval ustunidan ma’lumot qidiradi\n\n"
        "🔹 *HLOOKUP* – ГПР → Jadval satridan ma’lumot qidiradi\n\n"
        "🔹 *UPPER* – ПРОПИСН → Hamma harflarni katta qiladi\n\n"
        "🔹 *LOWER* – СТРОЧН → Hamma harflarni kichik qiladi\n\n"
        "🔹 *PROPER* – ПРОПНАЧ → Har bir so‘zni bosh harf bilan yozadi\n\n"
        "🔹 *COUNT* – СЧЁТ → Raqamli kataklar sonini sanaydi\n\n"
        "🔹 *COUNTA* – СЧЁТЗ → Bo‘sh bo‘lmagan kataklar sonini sanaydi\n\n"
        "🔹 *MAX* – МАКС → Eng katta qiymatni topadi\n\n"
        "🔹 *MIN* – МИН → Eng kichik qiymatni topadi\n\n"
        "🔹 *ROUND* – ОКРУГЛ → Sonni belgilangan raqamgacha yaxlitlaydi\n\n"
        "🔹 *CONCAT / TEXTJOIN* – СЦЕПИТЬ → Matnlarni birlashtiradi\n\n"
        "🔹 *NOW* – ТДАТАВРЕМЯ → Hozirgi sana va vaqtni ko‘rsatadi\n\n"
        "🔹 *TODAY* – СЕГОДНЯ → Hozirgi sanani ko‘rsatadi\n\n"
        "🔹 *ABS* – ABS → Sonning musbat qiymatini qaytaradi (modul)\n\n"
        "🔹 *PMT* – ПЛТ → Kredit to‘lovini hisoblaydi"
    )

    bot.send_message(
        call.message.chat.id,
        text,
        parse_mode="Markdown"
    )
# --- Matn orqali vazifa qo'shish ---
@bot.message_handler(func=lambda m: m.text.lower() == "💎 vazifa qoshish")
def add_text(message):
    start_process(message.chat.id)

@bot.message_handler(content_types=['photo', 'video','animation'])
def handle_media(message):
    chat_id = message.chat.id

    if chat_id in user_data and user_data[chat_id]["step"] == "wait_media":

        if message.content_type == "photo":
            user_data[chat_id]["media_type"] = "photo"
            user_data[chat_id]["file_id"] = message.photo[-1].file_id

        elif message.content_type == "video":
            user_data[chat_id]["media_type"] = "video"
            user_data[chat_id]["file_id"] = message.video.file_id


        elif message.content_type == "animation":
            user_data[chat_id]["media_type"] = "gif"
            user_data[chat_id]["file_id"] = message.animation.file_id

        user_data[chat_id]["step"] = "wait_name"
        bot.send_message(chat_id, "Ism familiyangizni yozing ✍️")


@bot.message_handler(func=lambda msg: True)
def handle_name(message):
    chat_id = message.chat.id

    if chat_id in user_data and user_data[chat_id]["step"] == "wait_name":
        full_name = message.text
        media_type = user_data[chat_id]["media_type"]
        file_id = user_data[chat_id]["file_id"]

        if media_type == "photo":
            bot.send_photo(
                CHANNEL_ID,
                file_id,
                caption=f"👤 {full_name}\n bugungi vazifasi\n{current_date}\n⏰ {current_time}"
            )
        elif media_type == "video":
            bot.send_video(
                CHANNEL_ID,
                file_id,
                caption=f"👤 {full_name}\n bugungi vazifasi\n{current_date}\n⏰ {current_time}"
            )
        elif media_type == "gif":
            bot.send_animation(
                CHANNEL_ID,
                file_id,
                caption=f"👤 {full_name} bugungi vazifasi\n{current_date}\n⏰ {current_time}"
            )

        bot.send_message(chat_id, "Ma'lumotlar ushbu @bright_future_asakaa kanlaga yuborildi! ✅\nYana rasm yoki video yuborish uchun /add bosing.")

        user_data.pop(chat_id, None)

bot.infinity_polling()
