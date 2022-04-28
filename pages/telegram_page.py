from .base_page import BasePage
from .locators import TelegramLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
import pytest
import time

class TelegramPage(BasePage):

    def user_dialogue(self):
        #If you need to swtich your browser uncomment code below
        #new_b = self.browser.window_handles[0]
        #self.browser.switch_to.window(new_b)

        #Change here numbers to id whom you want to send message
        #in ...-id = "numbers" and it will be enough
        #You can find id of every user in telegram page inspecting, 
        #just click on the user in inspector mode
        User = WebDriverWait(self.browser, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'li[data-peer-id = "907985181"] [class = "c-ripple"]'))
    )
        #This is for making user visible for selenium. Chat with user may be down,
        #not visible on the page at the opening, at this code will scroll down page to find it
        self.browser.execute_script("arguments[0].scrollIntoView();", User)
        User.click()
        chat = self.browser.find_element(*TelegramLocators.CHAT)
        chat.click()
        chat.send_keys("YOUR TEXT HERE")
        send = self.browser.find_element(*TelegramLocators.SEND_BUTTON)
        send.click()
        
    
