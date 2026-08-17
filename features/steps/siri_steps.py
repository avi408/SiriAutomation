from behave import given, when, then
from services.siri_service import SiriService


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

    print(f"Siri response: {context.response}")


@then("Siri interface should be available")
def step_verify_siri(context):
    assert context.siri is not None


@then("Siri should display today's weather")
def step_today(context):
    assert context.response is not None
    assert len(context.response.strip()) > 0

    response = context.response.lower()

    weather_keywords = [
        "weather",
        "temperature",
        "degrees",
        "forecast",
        "today",
        "°",
    ]

    assert any(
        keyword in response
        for keyword in weather_keywords
    ), f"Expected weather information, but Siri returned: {context.response}"


@then("Siri should display tomorrow's forecast")
def step_tomorrow(context):
    assert context.response is not None
    assert len(context.response.strip()) > 0

    response = context.response.lower()

    forecast_keywords = [
        "weather",
        "temperature",
        "degrees",
        "forecast",
        "tomorrow",
        "°",
    ]

    assert any(
        keyword in response
        for keyword in forecast_keywords
    ), f"Expected tomorrow's forecast, but Siri returned: {context.response}"