import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect

from login_page_webelements import LoginPage


def test_login(setup):
    page=setup

    loginpage= LoginPage(page)
    page.get_by_placeholder("email@example.com").fill("anshika@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button",name="Login").click()
    time.sleep(4)


def test_two():
    print("test_two is executed")
    pass




