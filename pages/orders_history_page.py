from pages.order_detail_page import OrdersDetailPage


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

        # Define page elements
    def order_id_row(self, order_id):
            return self.page.locator("tr").filter(has_text=order_id)


    def view_order_detail(self, order_id):
            self.order_id_row(order_id).get_by_role("button", name="View").click()
            order_detail_page = OrdersDetailPage(self.page)
            return order_detail_page
