from time import sleep

import pytest

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
    automator.download_csv(dl_url=CSVURL)
    sleep(10)
    automator.browser.quit()


@pytest.mark.vcr()
def test_report_page():
    automator = wa()
    automator.download_csv(dl_url=REPORTURL)
    sleep(10)
    automator.browser.quit()
