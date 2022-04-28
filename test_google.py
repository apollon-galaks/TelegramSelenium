from .pages.base_page import BasePage
from .pages.locators import GoogleLocators
from.pages.google_page import GooglePage

import time
import pytest


Email = 'chemistr.orxan98@gmail.com'

@pytest.mark.login
class TestGoogleLogin():
    def test_user_can_login(self, browser):
        url = "https://www.google.com/"
        page = GooglePage(browser,url)
        page.open()
        page.user_login(Email)

    @pytest.mark.skip
    def test_user_have_icon(self,browser):
        url = "https://www.google.com/"
        page = GooglePage(browser, url)
        page.open()
        page.user_icon()

@pytest.mark.search
class TestGoogleSearch():
    def test_user_can_search(self, browser):
        url = 'https://www.google.com/'
        page = GooglePage(browser, url)
        page.open()
        page.search_in_google()



