from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from hsautomation.urls import (
    FRONTPAGE,
    LOGINURL,
    PASSWD,
    PASSWDINPUTID,
    UNAME,
    UNAMEINPUTID,
)


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
        self.browser.find_element(By.ID, UNAMEINPUTID).send_keys(UNAME)
        self.browser.find_element(By.ID, PASSWDINPUTID).send_keys(PASSWD)
        self.browser.find_element(By.ID, "submit").click()
        sleep(0.5)

    def is_logged_in(self) -> bool:
        if LOGINURL in self.browser.current_url:
            return False
        return True
