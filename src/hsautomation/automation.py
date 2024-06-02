from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

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
        # wait the ready state to be complete
        WebDriverWait(driver=self.browser, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )
        if not self.is_logged_in():
            self.login()

    def login(self):
        self.browser.find_element(By.ID, UNAMEINPUTID).send_keys(UNAME)
        self.browser.find_element(By.ID, PASSWDINPUTID).send_keys(PASSWD)
        self.browser.find_element(By.ID, "submit").click()
        # wait the ready state to be complete
        WebDriverWait(driver=self.browser, timeout=10).until(
            lambda x: x.execute_script("return document.readyState === 'complete'")
        )

    def is_logged_in(self) -> bool:
        if LOGINURL in self.browser.current_url:
            return False
        return True
