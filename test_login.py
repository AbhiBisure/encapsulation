import re
import time
from login_page_webelements import LoginPage


def test_login(setup):
    page=setup

    loginpage= LoginPage(page)
    loginpage.login("anshika@gmail.com","Iamking@000")

def test_two():
    print("test_two is executed")
    pass




