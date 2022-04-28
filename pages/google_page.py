from .base_page import BasePage
from .locators import GoogleLocators
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import pytest

class GooglePage(BasePage):

    def user_login(self, email : str):
        gmail = self.browser.find_element(*GoogleLocators.GMAIL)
        assert gmail is not None, "Can't login!"

    def user_icon(self):
        user_icon = self.browser.find_element(*GoogleLocators.USER_ICON)
        assert user_icon is not None, "User is not logined!"

    def search_in_google(self):
        search = self.browser.find_element(*GoogleLocators.SEARCH)
        search.send_keys('Kitten photos')
        button = self.browser.find_element(*GoogleLocators.SEARCH_BUTTON)
        button.click()
        new_b = self.browser.window_handles[0]
        self.browser.switch_to.window(new_b)
        site = self.browser.find_element(*GoogleLocators.SITE)
        self.browser.execute_script("arguments[0].scrollIntoView();", site)
        site.click()
    