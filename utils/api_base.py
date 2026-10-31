from playwright.sync_api import Playwright

BASE_URL = "https://rahulshettyacademy.com"
LOGIN_PAYLOAD = {"userEmail": "dummy123456dummy@gmail.com", "userPassword": "dummy1D!"}
ORDERS_PAYLOAD = {"orders":[{"country": "Iran (Islamic Republic of)", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}



class APIUtils:
    def get_token(self, playwright: Playwright, user_credentials):
        user_email = user_credentials['userEmail']
        user_password = user_credentials['userPassword']
        login_payload = {"userEmail": user_email, "userPassword": user_password}
        # Create an API client without a browser
        get_token_context = playwright.request.new_context(base_url=BASE_URL,
                                                           ignore_https_errors=True)
        response = get_token_context.post(url="/api/ecom/auth/login",
                                          data=login_payload,
                                          headers={"Content-Type": "application/json"})
        assert response.ok

        # Return the token so other methods can use it
        return (response.json())["token"]


    def create_order(self, playwright: Playwright, user_credentials):
        token = self.get_token(playwright, user_credentials)
        create_order_context = playwright.request.new_context(base_url=BASE_URL,
                                                              ignore_https_errors=True)
        response = create_order_context.post(url="/api/ecom/order/create-order",
                                             data=ORDERS_PAYLOAD,
                                             headers={"Authorization": token,
                                          "Content-Type": "application/json"
                                          })

        order_id = response.json()["orders"][0]
        return order_id

