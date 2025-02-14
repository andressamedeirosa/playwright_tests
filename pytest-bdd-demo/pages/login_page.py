from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, login_url: str):
        self.page.goto(login_url)

    def enter_email(self, email: str):
        self.page.fill('input[ng-model="emailid"]', email)

    def click_login_button(self):
        self.page.click('img#enterimg')
