import pytest
from playwright.sync_api import sync_playwright, Page, Browser
import json
from typing import Generator
import os

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser: Browser) -> Generator[Page, None, None]:
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def base_url():
    return "https://demo.automationtesting.in/"

@pytest.fixture
def login_url(base_url):
    return f"{base_url}SignIn.html"

@pytest.fixture(scope='session')
def test_data():
    data_path = os.path.join(os.path.dirname(__file__), '../data/test_data.json')
    with open(data_path) as f:
        return json.load(f)