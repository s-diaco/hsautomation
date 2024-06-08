from time import sleep

import pytest
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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


# @pytest.mark.vcr()
def test_report_page():
    automator = wa()
    automator.browser.get(REPORTURL)
    sleep(2)
    automator.browser.find_element(By.ID, "rdoStore").click()
    sleep(2)

    # select store
    automator.browser.find_elements(By.CLASS_NAME, "riButton")[1].click()
    sleep(2)
    automator.browser.find_elements(By.CLASS_NAME, "SgMultiInput_newrow")[1].click()
    sleep(2)
    automator.browser.find_element(
        By.ID, "sgMultiInputStores_ctl01_Selector_Input"
    ).send_keys("انبار محصول اینکو")
    sleep(2)
    automator.browser.find_element(
        By.ID, "sgMultiInputStores_ctl01_Selector_Input"
    ).send_keys(Keys.RETURN)
    sleep(2)

    # show and go to print
    # automator.browser.find_elements(By.CLASS_NAME, "rtbBtn")[0].click()
    # sleep(5)
    automator.browser.find_elements(By.CLASS_NAME, "rtbBtn")[1].click()
    sleep(1)
    try:
        alert = automator.browser.switch_to.alert
        alert.accept()
    except NoAlertPresentException:
        pass

    sleep(5)

    # download csv
    automator.browser.find_elements(By.CLASS_NAME, "rtbExpandDown")[0].click()
    automator.browser.find_elements(By.CLASS_NAME, "rtbItem")[1].click()
    sleep(5)
    automator.browser.quit()
