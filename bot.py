from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os
TOKEN = os.getenv("BOT_TOKEN")

# تخزين الحالة الحالية لكل مستخدم
USER_STATE = {}

# --- الردود ---
WHO_WE_ARE_MENU = [
    ["🍃رؤيتنا🍃"],
    ["هدفن🍃ا🍃"],
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    USER_STATE[update.effective_user.id] = "MAIN"
    chat_id = update.effective_chat.id
    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://hassanhandal.github.io/SAIHSBOT/start.jpg",  
        caption=(
            " مرحبًا بك في *الأكاديمية العلمية للدراسات الإسلامية والإنسانية ✨*\n"
            "اختر من القائمة التالية:"
        ),
        parse_mode="Markdown"
    )
reply_markup = ReplyKeyboardMarkup(MAIN_MENU, resize_keyboard=True)
    await update.message.reply_text("⬇️ القائمة الرئيسية:", reply_markup=reply_markup)
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
        if text == "من نحن":
            USER_STATE[user_id] = "WHO"
            reply_markup = ReplyKeyboardMarkup(WHO_WE_ARE_MENU, resize_keyboard=True)
            await update.message.reply_text("📖 اختر من نحن:", reply_markup=reply_markup)
        elif text == "التقييم الدراسي":
            await update.message.reply_video(
                video=os.getenv("grading"),caption="#التقييم_الدراسي"
            )
        elif text == "المشرف الدراسي":
            await update.message.reply_video(
                video=os.getenv("mentor"),caption="#الإشراف_الدراسي"
                )
        elif text == "الدعم الفني":
            await update.message.reply_text(
                "للتواصل مع الدعم الفني اضغط هنا @Al_Da3m_Alfanny" )
        elif text == "كيفية التسجيل":
            await update.message.reply_video(video=os.getenv("howtoadmit"),caption="#كيفية_التسجيل")
        elif text == "تعرف علينا":
            await update.message.reply_video(video=os.getenv("knowus"),caption="#تعرف_علينا")
        else:
            await update.message.reply_text("يرجى اختيار خيار من القائمة الرئيسية.")

    elif state == "WHO":
        if text == "رؤيتنا":
            await update.message.reply_text(
                "🌟 رؤيتنا:\n"
                "✨ نفتح لك آفاق التعلم\n"
                "🧭 نؤسس لك القواعد العلمية التي تمكنك من الإبحار في مستويات العلم الشرعي بسهولة.\n"
                "👨‍🏫 تتعلم على يد نخبة من المتخصصين في مجال العلم الشرعي.\n"
                "💻 تتعلم من خلال وسائل التعلم المتقدمة المعتمدة في برنامج الأكاديمية."
            )
        elif text == "هدفنا":
            await update.message.reply_text(
                "🎯 هدفنا:\n"
                "📢 المساهمة في توصيل العلم الشرعي للراغبين فيه من خلال تيسير ما لا يسع المسلم جهله لعامة المسلمين.\n"
                "💻 إزالة موانع تعلم العلم الشرعي من خلال استخدام التقنية في تعليم العلوم الشرعية.\n"
                "📖 نشر العلم الشرعي القائم على كتاب الله وسنة صلى الله عليه وسلم.\n"
                "🌟 تعليم العلم صافيًا نقيًا بفهم خير القرون."
            )
        elif text == "مميزات الأكاديمية":
            await update.message.reply_text(
                "🏅 مميزات الأكاديمية:\n"
                "🎥 1- البث المباشر لجميع المحاضرات، ليتمكن الطالب: من التفاعل مع المحاضر – لئلا تكون المحاضرة مجرد تلقين\n"
                "🧑‍🏫 2- ونظام الإشراف الدراسي: بحيث يوجد لكل طالبٍ – مشرفٌ يتابع حضوره، ويجيب على إشكالاته\n"
                "📝 3- والتدريبات الدورية على كل محاضرة ليتمكن الطالب من تثبيت المعلومات\n"
                "🌱 4- والاهتمام بالجانب التربوي والعملي – لكيلا يكون (العلم) مجردًا عن العمل .........\n"
                "\n"
                "📝 بادر بتسجيل اسمك – في الدفعة الجديدة لهذا العام\n"
                "📢 وتأكد من اشتراكك في القناة العامة للأكاديمية على التليجرام:\n"
                "🔗 https://t.me/Academy_of_Human_Sciences\n"
                "\n"
                "🏛️ الأكاديمية العلمية (للدراسات الإسلامية والإنسانية): طريقك نحو ميراث الأنبياء."
            )
        
        else:
            await update.message.reply_text("اختر من القائمة الفرعية أو اضغط ↩ للرجوع.")

# إعداد البوت
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("🤖 البوت شغال... جرب /start من تيليجرام")
app.run_polling()
