from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
TOKEN = os.getenv("BOT_TOKEN")

# تخزين الحالة الحالية لكل مستخدم
USER_STATE = {}

# --- الردود ---
WHO_WE_ARE_MENU = [
    ["🍃رؤيتنا🍃"],
    ["🍃هدفنا🍃"],
    ["🍃مميزات الأكاديمية🍃"],
    ["↩ العودة للقائمة الرئيسية"]
]

MAIN_MENU = [
    ["🍃تعرف علينا🍃"],
    ["🍃من نحن🍃"],
    ["🍃كيفية التسجيل🍃"],
    ["🍃التقييم الدراسي🍃"],
    ["🍃المشرف الدراسي🍃"],
    ["👨‍💻الدعم الفني"]
    
]
async def send_welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    USER_STATE[update.effective_user.id] = "MAIN"
    reply_markup = ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
    await update.message.reply_photo(
        photo="https://hassanhandal.github.io/SAIHSBOT/start.jpg",
        caption="مرحبًا بك في الأكاديمية العلمية للدراسات الإسلامية والإنسانية ✨\nاختر من القائمة التالية:",
        reply_markup=reply_markup
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_welcome(update, context)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text

    if text == "↩ العودة للقائمة الرئيسية":
        USER_STATE[user_id] = "MAIN"
        reply_markup = ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
        await update.message.reply_text("تم الرجوع إلى القائمة الرئيسية:", reply_markup=reply_markup)
        return

    state = USER_STATE.get(user_id, "MAIN")

    if state == "MAIN":
        if text == "🍃من نحن🍃":
            USER_STATE[user_id] = "WHO"
            reply_markup = ReplyKeyboardMarkup(WHO_WE_ARE_MENU, resize_keyboard=True)
            await update.message.reply_text("📖 اختر من نحن:", reply_markup=reply_markup)
        elif text == "🍃التقييم الدراسي🍃":
            await update.message.reply_video(
                video=os.getenv("grading"),caption="#التقييم_الدراسي"
            )
        elif text == "🍃المشرف الدراسي🍃":
            await update.message.reply_video(
                video=os.getenv("mentor"),caption="#الإشراف_الدراسي"
                )
        elif text == "👨‍💻الدعم الفني":
            await update.message.reply_text(
                "للتواصل مع الدعم الفني اضغط هنا @Al_Da3m_Alfanny" )
        elif text == "🍃كيفية التسجيل🍃":
            await update.message.reply_video(video=os.getenv("howtoadmit"),caption="#كيفية_التسجيل")
        elif text == "🍃تعرف علينا🍃":
            await update.message.reply_video(video=os.getenv("knowus"),caption="#تعرف_علينا")
        else:
            await send_welcome(update,context)

    elif state == "WHO":
        if text == "🍃رؤيتنا🍃":
            await update.message.reply_photo(
        photo="https://hassanhandal.github.io/SAIHSBOT/vision.jpg",
        caption="#رؤيتنا")
        elif text == "🍃هدفنا🍃":
            await update.message.reply_photo(
        photo="https://hassanhandal.github.io/SAIHSBOT/mission.jpg",
        caption="#هدفنا")
        elif text == "🍃مميزات الأكاديمية🍃":
            await update.message.reply_photo(
        photo="https://hassanhandal.github.io/SAIHSBOT/benefits.jpg",
        caption="#مميزات_الأكاديمية")
        
        else:
             USER_STATE[user_id] = "WHO"
             reply_markup = ReplyKeyboardMarkup(WHO_WE_ARE_MENU, resize_keyboard=True)
             await update.message.reply_text("📖 اختر من نحن:", reply_markup=reply_markup)

# إعداد البوت
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🤖 البوت شغال... جرب /start من تيليجرام")
app.run_polling()
