import time

from behave import given, when, then, use_step_matcher, step

use_step_matcher("re")

pause = 1


@given("I am on the home page")
def step_impl(context):
    context.browser.get('http://localhost:' + str(context.port) )
    time.sleep(pause)


@when("I click welcome menu")
def step_impl(context):
    context.browser.find_element_by_id('welcome-link').click()


@given("I am on the welcome page")
def step_impl(context):
    context.browser.get('http://localhost:' + str(context.port)+ '/welcome.html')

@then("I expect to see the welcome message")
def step_impl(context):
    message = context.browser.find_element_by_xpath('(//h2)[2]').text

    assert message == "Welcome to the best site for information on scuba diving and snorkling in Portugal!"







