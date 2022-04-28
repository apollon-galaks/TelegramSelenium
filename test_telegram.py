from .pages.base_page import BasePage
from .pages.telegram_page import TelegramPage

import time
import pytest


class TestSendMessage():
    def test_send_message(self, browser):
        url = "https://web.telegram.org/"
        page = TelegramPage(browser,url)
        page.open()
        page.diana_dialogue()