from behave import given, then, when


@given("Open Cureskin")
def open_cureskin_page(context):
    context.app.base_page.open_url('https://shop.cureskin.com/')


@when("Open Product Details page")
def verify_product_details_page(context):
    context.app.header.click_shop_all()
    context.app.all_products.verify_all_products()


@then("Add product to cart")
def add_product_to_cart(context):
    context.app.all_products.add_to_cart()
    context.app.all_products.verify_item_added()


@then("Click View cart")
def click_on_view_cart(context):
    context.app.all_products.click_view_cart()


@then("Verify user is taken to the cart page")
def verify_user_is_taken_to_cart_page(context):
    context.app.cart_page.verify_cart_page()