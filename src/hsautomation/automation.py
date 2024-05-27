from hsautomation.urls import FRONTPAGE, LOGINURL, PASSWD, UNAME
from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class WebAutomation:
    def __init__(self) -> None:
        options = Options()
        options.add_argument("--headless=new")
        self.browser = Chrome(options=options)
        self.browser.get(FRONTPAGE)
        sleep(0.5)
        if not self.is_logged_in():
            self.login()

    def login(self):
        self.browser.get(LOGINURL)
        sleep(0.5)

    def is_logged_in(self) -> bool:
        return False
