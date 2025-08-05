import telebot
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

API_TOKEN = "7578617102:AAHSjA-e7I1u1XoaXWovQLx6pqrtj1H6aGU"
bot=telebot.TeleBot(API_TOKEN)

async def bantuan(update: Update, context: ContextTypes.DEFAULT_TYPE) ->None:
    await update.message.reply_text("Silakan ajukan pertanyaan Anda melalui akun telegram \n @WQTravel")

async def daftarhaji(update : Update, context : ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text("Informasi daftar haji akan diberitakan lebih lanjut")

async def daftarumroh(update : Update, context : ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text("Informasi daftar umroh akan diberitakan lebih lanjut")

async def pengumuman(update : Update, context : ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text("Belum ada pengumuman")
    print(update.message)

async def undangan(update : Update, context : ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text("Undangan akan segera disebarkan melalui bot ini")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    identitas=update.effective_user
    if identitas.first_name==None:
        nama_depan=''
    else:
        nama_depan = identitas.first_name
    if identitas.last_name==None:
        nama_belakang=''
    else:
        nama_belakang=identitas.last_name
    await update.message.reply_text(f"Assalamualaikum wr wb, {nama_depan} {nama_belakang}...🤗!! \n\n Terima kasih telah bersedia menggunakan bot telegram Waridat Qolbi Travel. Silakan pilih menu untuk mendapatkan informasi mengenai pendaftaran. \n {"🙏"*3} \n /bantuan -> Contact person \n /daftarhaji -> Untuk pendaftaran jemaah haji plus dan reguler \n /daftarumroh -> Pendaftaran untuk jemaah umroh \n /pengumuman -> Pengumuman kegiatan dan informasi jadwal \n Undangan untuk manasik dan atau pengambilan perlengkapan")

def main():
    print("🟢 bot.py mulai dijalankan")
    app = Application.builder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bantuan", bantuan))
    app.add_handler(CommandHandler("daftarhaji", daftarhaji))
    app.add_handler(CommandHandler("daftarumroh", daftarumroh))
    app.add_handler(CommandHandler("undangan", undangan))
    app.add_handler(CommandHandler("pengumuman", pengumuman))
    app.run_polling()

if __name__ == "__main__":
    main()
