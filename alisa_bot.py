import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
# Tugmalar menyusi
menu = [["🏠 Ijara", "🏢 TTJ"], ["💳 Kontrakt", "⛔ Stop"]]
# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(menu, resize_keyboard=True)
    await update.message.reply_text(
        "Salom! Men Alisa botman. Talabalarga quyidagi yo‘nalishlarda yordam beraman:\n\n"
        "🏠 Ijara shartnomasi\n🏢 TTJga joylashish\n💳 Kontrakt to‘lovi\n\n"
        "Kerakli bo‘limni tanlang 👇",
        reply_markup=reply_markup)
# /stop komandasi
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⛔ Bot to‘xtatildi. Xayr!")
    # sys.exit() Render’da xatolik beradi — o‘rniga pass qilamiz
# Ijara bo‘yicha maslahat
async def ijara(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
"📄 *Ijara shartnomasi tuzish tartibi:*\n\n"
        "1. Soliq ilovasida ijaraga beruvchi tomonidan elektron kalit(kuluch) yaratiladi yaratilgan bo'lishi ham mumkin\n"
        "2. Ijara shartnomasini tuzishda soliq xizmatlar foydalaning. Online tarizda tuzish ham mumkin.Online ijara shartnomasini tuzishni xohlasangiz quydagi Adminga murojat qiling. @hasanjozilov\n"
        "3. Ijara shartnoma tuzilgandan so'ng uni https://kontrakt.edu.uz saytidan shaxsiy kabinetingizga kirib quydagi ketmaketlikni bajaring: menyu》ijara to'lovlari》ariza. ariza yuboring\n"
        "4. Institutga quyidagi hujjatlarni olib boring:\n"
        "   - my.gov.uz saytidan doimiy yashash joyi haqida ma’lumotnoma\n"
        "   - kantrakt.edu.uzdan yuborgan arizangiz\n"
        "   - Pasport nusxasi(1 dona)\n"
        "   - Ijara shartnomasi nusxasi\n\n"
        "📌 Hujjatlarni institutning ro‘yxatga olish bo‘limiga topshiring.")
# TTJ bo‘yicha maslahat
async def ttj(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
"🏢 *TTJga joylashish tartibi:*\n\n"
        "1. Kantrakt.edu.uz saytidan shaxsiy kabinetga kiring undan manyuni tanlang talabalar turar joyi hamda ariza\n"
        "2. shu tariqa online ariza yuboring\n"
        "3. Hujjatlarni TTJ bo‘limiga olib boring\n\n"
        "📌 Joylashish muddati va narxlar haqida institutdan aniqlashtiring.")
# Kontrakt bo‘yicha maslahat
async def kontrakt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 *Kontrakt shartnomasi va to‘lov:*\n\n"
        "💳 *Kontrakt shartnomasi va to‘lov:*\n\n"
        "1. https://kontrakt.edu.uz saytiga kiring\n"
        "2. Shaxsiy kabinetga kirib, shartnomani yuklab oling\n"
        "3. To‘lov usullari:\n"
        "   - PayMe, Click, Zoomrad, Upay, Oson, Anorbank. Agar online to'lov qilishni bilmasangiz quydagi link orqali o'rganiahingiz mumkin yoki istalgan bank orqaliali amalga oshiring\n"
        "4. To‘lov cheki (kvitansiya) ni yuklab oling yoki chop eting\n\n"
        "📌 To‘lovni belgilangan muddatda amalga oshiring.")
# Botni ishga tushirish
def main():
    app = Application.builder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(MessageHandler(filters.Regex("Ijara"), ijara))
    app.add_handler(MessageHandler(filters.Regex("TTJ"), ttj))
    app.add_handler(MessageHandler(filters.Regex("Kontrakt"), kontrakt))
    app.add_handler(MessageHandler(filters.Regex("Stop"), stop))
    app.run_polling()
if __name__ == "__main__":
    main()
