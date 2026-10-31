from pages.orders_history_page import OrdersHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    # Define page elements
    def orders_link(self):
        return self.page.get_by_role("button", name="  ORDERS")

    # Define Operations
    def navigate_orders_page(self):
        self.orders_link().click()
        orders_history_page = OrdersHistoryPage(self.page)
        return orders_history_page