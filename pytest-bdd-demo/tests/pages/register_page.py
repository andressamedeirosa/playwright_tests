class RegisterPage:
    # ...existing code...

    def fill_first_name(self, first_name: str):
        first_name_input = self.page.locator('input[ng-model="FirstName"]')
        first_name_input.fill(first_name)
        first_name_input.press('Tab')

    def fill_last_name(self, last_name: str):
        last_name_input = self.page.locator('input[ng-model="LastName"]')
        last_name_input.fill(last_name)
        last_name_input.press('Tab')
