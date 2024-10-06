from io import BytesIO

from PIL import Image
from telegram import Update, InlineKeyboardMarkup


async def display_frame(update: Update, frame_num: int, frame_data: bytes, reply_markup: InlineKeyboardMarkup):
    """
    Sends the frame image to the user via Telegram with interactive buttons.
    """
    img = Image.open(BytesIO(frame_data))
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)
    await update.message.reply_photo(
        photo=img_byte_arr, caption=f"Frame {frame_num}: Did the rocket launch?",
        reply_markup=reply_markup
    )
