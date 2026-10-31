import json

import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from playwright.sync_api import Playwright, expect
from utils.api_base import APIUtils

# json file
with open("testdata/credentials.json") as f:
    test_data = json.load(f)
    user_credentials_list = test_data['valid_user']


@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, user_credentials):
    username = user_credentials["userEmail"]
    password = user_credentials["userPassword"]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create order -> order_id
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright, user_credentials)

    # Login
    login_page = LoginPage(page)
    login_page.navigate()
    dashboard_page = login_page.login_as(username, password)

    # Orders History page -> order is present.
    orders_history_page = dashboard_page.navigate_orders_page()
    order_detail_page = orders_history_page.view_order_detail(order_id)
    order_detail_page.verify_thank_you_message()
    context.close()

