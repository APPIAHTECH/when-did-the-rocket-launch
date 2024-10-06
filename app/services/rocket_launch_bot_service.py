import logging

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from app.classes.bisection import BisectionAlgorithm
from app.classes.framex_api import FrameXAPI
from settings.config import TELEGRAM_TOKEN
from utils.frame import display_frame

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)


class RocketLaunchBotService:

    def __init__(self):
        self.user_bisection_sessions = {}

    async def start(self, update: Update, context):
        await update.message.reply_text("Welcome! Let's find the rocket launch frame. Type /launch to start.")

    async def error(self, update: Update, context: CallbackQueryHandler):
        logger.error(f"Update {update} caused error {context}")

    async def launch(self, update: Update, context):
        logger.info(f"Launching frame finder for chat_id: {update.message.chat_id}")
        chat_id = update.message.chat_id
        bisector = BisectionAlgorithm(FrameXAPI())
        self.user_bisection_sessions[chat_id] = bisector
        frame_num, frame_data = bisector.get_next_frame()
        if frame_num is None:
            await update.message.reply_text("Failed to fetch frame.")
            return

        keyboard = [[InlineKeyboardButton("Yes", callback_data="yes"),
                     InlineKeyboardButton("No", callback_data="no")]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await display_frame(update, frame_num, frame_data, reply_markup)
        logger.info(f"Sent frame {frame_num} to user {chat_id}")

    async def handle_answer(self, update: Update, context):
        query = update.callback_query
        chat_id = query.message.chat_id

        bisector = self.user_bisection_sessions.get(chat_id)

        if bisector:
            answer = query.data == "yes"
            frame_num, frame_data = bisector.test_frame(answer)

            if frame_num is not None:
                keyboard = [[InlineKeyboardButton("Yes", callback_data="yes"),
                             InlineKeyboardButton("No", callback_data="no")]]
                reply_markup = InlineKeyboardMarkup(keyboard)

                await display_frame(query, frame_num, frame_data, reply_markup)
            else:
                await query.message.reply_text(f"Found the rocket launch at frame {bisector.result_frame}!")
        await query.answer()

    def start_bot(self):
        app = Application.builder().token(TELEGRAM_TOKEN).build()

        # Commands
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(CommandHandler("launch", self.launch))

        # Messages
        app.add_handler(CallbackQueryHandler(self.handle_answer))

        # Errors
        app.add_error_handler(self.error)

        app.run_polling()
