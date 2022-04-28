from sre_constants import CHARSET
from selenium.webdriver.common.by import By



class TelegramLocators():
    #You should add here the selector of User, who you want to send message
    #It will be enough if you will change only numbers in ...-id = "numbers"
    USER = (By.CSS_SELECTOR, 'li[data-peer-id = "694593421"] [class = "c-ripple"]')
    #Here the selector of message field with this user, this selector is unique for all 
    CHAT = (By.CSS_SELECTOR, '[class="input-message-input scrollable scrollable-y i18n no-scrollbar"]')
    #Here the selector of button to send message, it is also unique selector for all
    SEND_BUTTON = (By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div[1]/div[5]/button/div')
    


#There is some selectors for testing google main page
class GoogleLocators():
    LOGIN_GMAIL = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[1]/a')
    USER_ICON = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/div[2]/div/a/img')
    SEARCH = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')
    SITE = (By.XPATH, '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[3]/div/div[1]/div/a/h3')
    GMAIL = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/a')
    EMAIL = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
