from behave import given, when, then


@given("the iOS simulator is available")
def step_simulator_available(context):
    assert context.driver is not None


@when("the automation framework initializes the driver")
def step_initialize_driver(context):
    pass


@then("an Appium session should be created")
def step_session_created(context):
    assert context.driver.session_id is not None


@then("the session id should not be empty")
def step_session_not_empty(context):
    assert len(context.driver.session_id) > 0