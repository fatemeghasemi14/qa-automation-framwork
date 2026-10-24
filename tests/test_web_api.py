from playwright.sync_api import Playwright, expect
from utils.api_base import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create order -> order_id
    api_utils = APIUtils()
    order_id = api_utils.create_order(playwright)

    # Login
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.locator("#userEmail").fill("dummy123456dummy@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("dummy1D!")
    page.get_by_role("button", name="Login").click()

    # Orders History page -> order is present.
    page.get_by_role("button", name="  ORDERS").click()
    order_row = page.locator("tr").filter(has_text=order_id)
    order_row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
