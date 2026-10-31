from pages.dashboard_page import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page

    # Define page elements
    def username_input(self):
        return self.page.locator("#userEmail")

    def password_input(self):
        return self.page.get_by_placeholder("enter your passsword")

    def submit_button(self):
        return self.page.get_by_role("button", name="Login")

    # Define Operations
    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client/#/auth/login")

    def login_as(self, username: str, password: str):
        self.username_input().fill(username)
        self.password_input().fill(password)
        self.submit_button().click()
        dashboard_page = DashboardPage(self.page)
        return dashboard_page