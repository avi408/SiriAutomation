"""Step definitions for automation infrastructure scenarios."""

from behave import given, then


@given("the Appium session is available")
def step_appium_session_is_available(context):
    """Confirm the Behave hook created a driver before the scenario."""
    assert context.driver is not None, "The Appium driver was not created."


@then("the session should have an identifier")
def step_session_has_identifier(context):
    """Confirm Appium returned an active session identifier."""
    assert context.driver.session_id, "Appium did not return a session identifier."
