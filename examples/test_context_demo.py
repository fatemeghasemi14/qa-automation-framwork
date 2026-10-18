from playwright.sync_api import Playwright
from pytest_playwright.pytest_playwright import browser


def test_context_demo(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=6000)

    # Creating 2 separate context
    ctx1 = browser.new_context()
    ctx2 = browser.new_context()

    # Log into context 1
    page1 = ctx1.new_page()
    page1.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page1.locator("#userEmail").fill("dummy123456dummy@gmail.com")
    page1.get_by_placeholder("enter your passsword").fill("dummy1D!")
    page1.get_by_role("button", name="Login").click()

    # Second tab in the same context: shares the session, so it should already be logged in
    page1b = ctx1.new_page()
    page1b.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")

    # Tab in a different context: separate session, so it should NOT be logged in
    page2 = ctx2.new_page()
    page2.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")

    page1.wait_for_timeout(3000)
    browser.close()