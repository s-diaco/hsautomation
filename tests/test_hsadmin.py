from time import sleep

from hsautomation.automation import WebAutomation as wa


def test_play():
    from hsautomation.bandleader import BandLeader

    bandleader = BandLeader("db.csv")
    bandleader.play()
    sleep(10)
    assert bandleader.currently_playing()


def test_login():
    automator = wa()
