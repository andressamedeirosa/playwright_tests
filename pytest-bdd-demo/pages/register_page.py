from playwright.sync_api import Page

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, register_url: str):
        self.page.goto(register_url)

    def enter_first_name(self, first_name: str):
        self.page.fill('#basicBootstrapForm > section > div > div > div:nth-child(1) > div > div > input', first_name)

    def enter_last_name(self, last_name: str):
        self.page.fill('#basicBootstrapForm > section > div > div > div:nth-child(2) > div > div > input', last_name)

    def enter_address(self, address: str):
        self.page.fill('#EcomercePassword', address)

    def enter_email_address(self, email_address: str):
        self.page.fill('#basicBootstrapForm > section > div > div > div:nth-child(4) > div > div > input', email_address)

    def enter_phone_number(self, phone_number: str):
        self.page.fill('#basicBootstrapForm > section > div > div > div:nth-child(5) > div > div > input', phone_number)

    def enter_gender(self, gender: str):
        if gender.lower() == 'female':
            self.page.click('#basicBootstrapForm > section > div > div > div:nth-child(6) > div > label:nth-child(2) > input[type=radio]')
        elif gender.lower() == 'male':
            self.page.click('#basicBootstrapForm > section > div > div > div:nth-child(6) > div > label:nth-child(1) > input[type=radio]')

    def enter_hobbies(self, hobbies: str):
        if hobbies.lower() == 'cricket':
            self.page.click('#checkbox1')
        elif hobbies.lower() == 'movies':
            self.page.click('#checkbox2')
        elif hobbies.lower() == 'hockey':
            self.page.click('#checkbox3')

    def enter_languages(self, languages: str):
        self.page.select_option('#msdd', languages)

    def enter_skills(self, skills: str):
        self.page.select_option('#Skills', skills)

    def enter_country(self, country: str):
        self.page.select_option('#countries', country)

    def enter_date(self, year: str, month: str, day: str):
        self.page.select_option('#yearbox', year)
        self.page.select_option('select[placeholder="Month"]', month)
        self.page.select_option('#daybox', day)

    def enter_password(self, password: str):
        self.page.fill('#firstpassword', password)

    def enter_confirm_password(self, confirm_password: str):
        self.page.fill('#secondpassword', confirm_password)

    def click_submit_button(self):
        self.page.click('#submitbtn')
