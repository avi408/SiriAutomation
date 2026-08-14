from behave import given, when, then
from services.siri_service import SiriService
from utils.siri_response_parser import SiriResponseParser


@given("the Appium driver is initialized")
def step_driver(context):
    context.siri = SiriService(context.driver)


@given("Siri is available")
def step_siri_available(context):
    context.siri = SiriService(context.driver)


@when("I activate Siri")
def step_activate(context):
    context.siri.activate()


@when('I ask "{question}"')
def step_ask(context, question):
    context.response = context.siri.ask_question(question)


@then("Siri interface should be available")
def step_verify_siri(context):
    assert context.siri is not None


@then("Siri should display today's weather")
def step_today(context):

    assert context.response is not None, \
        "Siri did not return a response."

    assert SiriResponseParser.contains_weather_response(
        context.response
    ), "Siri response does not contain weather information."


@then("Siri should display tomorrow's forecast")
def step_tomorrow(context):

    assert context.response is not None, \
        "Siri did not return a response."

    assert SiriResponseParser.contains_weather_response(
        context.response
    ), "Siri response does not contain weather information."




