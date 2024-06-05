from time import sleep

import pytest
from selenium.webdriver.common.by import By

from hsautomation.automation import WebAutomation as wa
from hsautomation.urls import CSVURL, FRONTPAGE, REPORTURL


def test_play():
    from hsautomation.bandleader import BandLeader

    bandleader = BandLeader("db.csv")
    bandleader.play()
    sleep(10)
    assert bandleader.currently_playing()
    bandleader.browser.quit()


@pytest.mark.vcr()
def test_login():
    automator = wa()
    assert FRONTPAGE in automator.browser.current_url
    automator.browser.quit()


@pytest.mark.vcr()
def test_download_csv():
    automator = wa()
    automator.browser.get(CSVURL)
    sleep(10)
    automator.browser.quit()


@pytest.mark.vcr()
def test_report_page():
    automator = wa()
    automator.browser.get(REPORTURL)
    sleep(10)
    automator.browser.find_element(
        By.XPATH, "//*[@id='trStoreLevelStock']/input"
    ).click()
    sleep(10)
    automator.browser.find_element(
        By.ID, "sgMultiInputStores$ctl01$Selector"
    ).send_keys("انبار محصول اینکو")
    automator.browser.find_element(By.XPATH, '//*[@class="rtbUL"]/li[1]/a').click()
    sleep(10)
    automator.browser.find_element(By.XPATH, '//*[@class="rtbUL"]/li[2]/a').click()
    sleep(10)

    automator.browser.quit()
