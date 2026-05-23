import time

class LoginPage():

    def __init__(self,page):
        self.email_input = page.get_by_placeholder("email@example.com")
        self.password_input = page.get_by_placeholder("enter your passsword")
        self.login_button = page.get_by_role("button", name="Login")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()
        time.sleep(4)
