from behave import given, when, then

@given("que estoy en la página de login")
def step_impl(context):
    base_url = context.config_data["base_url"]
    context.login_page.open_login_page(base_url)

@when('inicio sesión con usuario "{username}" y password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)

@then("debo ver la lista de productos")
def step_impl(context):
    assert context.inventory_page.get_products_count() > 0

@then("debo ver un mensaje de error de login")
def step_impl(context):
    assert "Epic sadface" in context.login_page.get_error_message()