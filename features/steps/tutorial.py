from behave import *


@given('we have behave installed')
def step_impl(context):
    print("Start the test")
    pass


@when('we implement a test')
def step_impl(context):
    print("Implement")
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    print("Assert")
    assert context.failed is False
