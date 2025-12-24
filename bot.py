from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import logging
from scraper import get_facebook_info  # Import hàm scrape của bạn

# Cấu hình logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Xin chào! Gửi cho tôi username Facebook để kiểm tra.')

# Xử lý tin nhắn username
async def handle_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.strip()
    await update.message.reply_text(f'Đang xử lý {username}...')

    try:
        # Gọi hàm thu thập dữ liệu
        user_info = get_facebook_info(username)

        # Định dạng và trả kết quả (theo mẫu bạn cung cấp)
        response = f"""
FACEBOOK INFO | BOT DEMO
Tên: {user_info.get('name', 'N/A')}
UID: {user_info.get('uid', 'Không xác định')}
Username: {username}
"""
        await update.message.reply_text(response)
    except Exception as e:
        logger.error(f"Lỗi khi xử lý {username}: {e}")
        await update.message.reply_text("Có lỗi xảy ra. Vui lòng thử lại sau.")

def main():
    # THAY THẾ 'YOUR_BOT_TOKEN' BẰNG TOKEN THẬT CỦA BẠN
    application = Application.builder().token("8149003927:AAGwNVNB1QjmzNEXi6n5MpH4O_gfIsf30_A").build()

    # Đăng ký các trình xử lý
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_username))

    # Chạy bot
    application.run_polling()

if __name__ == '__main__':
    main()