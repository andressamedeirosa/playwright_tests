import pytest
from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

scenarios('../features/login.feature')

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@given('the user is on the login page')
def user_on_login_page(login_page):
    login_page.navigate('https://demo.automationtesting.in/Index.html')

@when('the user enters valid credentials')
def user_enters_valid_credentials(login_page, test_data):
    user = test_data['users'][0]
    login_page.enter_email(user['email'])

@when('the user submits the login form')
def user_submits_login_form(login_page):
    login_page.click_login_button()

@then('the user should be redirected to the homepage')
def user_redirected_to_homepage(page):
    assert page.url == 'https://demo.automationtesting.in/Register.html'
