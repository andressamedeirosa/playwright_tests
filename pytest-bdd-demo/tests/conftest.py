import pytest
from playwright.sync_api import sync_playwright, Page, Browser

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser: Browser) -> Page:
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def base_url():
    return "https://demo.automationtesting.in/"

@pytest.fixture
def login_url(base_url):
    return f"{base_url}SignIn.html"