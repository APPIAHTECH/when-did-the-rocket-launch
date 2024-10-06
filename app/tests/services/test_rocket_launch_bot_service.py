import unittest
from unittest.mock import AsyncMock, patch

from telegram import Update

from app.services.rocket_launch_bot_service import RocketLaunchBotService


class TestRocketLaunchBotService(unittest.TestCase):

    def setUp(self):
        self.bot_service = RocketLaunchBotService()

    @patch('telegram.ext._application.Application.run_polling')
    def test_start_bot(self, mock_run_polling):
        """Test if the bot starts correctly."""
        self.bot_service.start_bot()
        mock_run_polling.assert_called_once()

    @patch('telegram.ext.Update.message')
    async def test_start_command(self, mock_message):
        """Test the /start command."""
        mock_update = AsyncMock(spec=Update)
        mock_update.message.reply_text = AsyncMock()

        await self.bot_service.start(mock_update, AsyncMock())
        mock_update.message.reply_text.assert_called_once_with(
            "Welcome! Let's find the rocket launch frame. Type /launch to start.")
