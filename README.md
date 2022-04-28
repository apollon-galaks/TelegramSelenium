# TelegramSelenium
Hello User!
I've written some experimental bot on Telegram, which now can only send a message to a specific user by its id selector
If you want to try it please pay attention to conftest.py file, 
There I wrote "__ChromeDriverManager().install()__" because I didn't add webdriver to PATH.
Don't change anything if You have not webdriver, an it will work, 
if You have it and it is in PATH - then delete this text between " ".
To start process open PowerShell and find this folder and call pytest method like below:
path > cd TelegramSelenium
path > TelegramSelenium > pytest -s -v test_telegram.py
