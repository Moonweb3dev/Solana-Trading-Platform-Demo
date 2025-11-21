# Demo Telegram bot stub

from .utils import log
from .config import TELEGRAM_CHAT_ID

class MockBotAPI:
    def send(self, text):
        log(f"[MockBot] -> {TELEGRAM_CHAT_ID}: {text}")
