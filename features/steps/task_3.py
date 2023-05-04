from behave import given, then, when


@then("Verify a product in cart")
def verify_a_product_in_cart(context):
    context.app.cart_page.verify_cart_product_name(product_name=name)


@then("Verify a product name and price in cart")
def verify_a_product_price_in_cart(context):
    context.app.cart_page.verify_name_and_price()


@then("Add product to the cart")
def step_impl(context):
    context.app.all_products.add_to_cart()
