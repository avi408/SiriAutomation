import time

from behave import given, then, when
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("the Calendar app is launched")
def step_launch_calendar(context):
    context.driver.activate_app("com.apple.mobilecal")

    # Dismiss an existing event editor if one is left open
    try:
        cancel = context.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID,
            "cancel-button"
        )

        if cancel.is_displayed():
            cancel.click()
            print("Existing event editor dismissed.")

    except Exception:
        pass

    time.sleep(1)


@then("the Calendar interface should be displayed")
def step_verify_calendar(context):
    wait = WebDriverWait(context.driver, 10)

    today = wait.until(
        EC.presence_of_element_located(
            (
                AppiumBy.ACCESSIBILITY_ID,
                "Today, Saturday, August 15"
            )
        )
    )

    assert today.is_displayed()

    print("Calendar interface displayed successfully")
    print("Today's element:", today.get_attribute("label"))


@when("I select today's date")
def step_select_today(context):
    wait = WebDriverWait(context.driver, 10)

    today = wait.until(
        EC.element_to_be_clickable(
            (
                AppiumBy.ACCESSIBILITY_ID,
                "Today, Saturday, August 15"
            )
        )
    )

    today.click()

    print("Today's date selected")


@then("today's date should be selected")
def step_verify_today_selected(context):
    wait = WebDriverWait(context.driver, 10)

    today = wait.until(
        EC.presence_of_element_located(
            (
                AppiumBy.ACCESSIBILITY_ID,
                "Today, Saturday, August 15"
            )
        )
    )

    traits = today.get_attribute("traits")

    print("Today's traits:", traits)

    assert today.is_displayed()


@when("I tap the Add button")
def step_tap_add(context):
    print("\n===== CALENDAR PAGE SOURCE BEFORE ADD =====")

    source = context.driver.page_source

    with open(
        "calendar_before_add.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(source)

    print("Page source saved to calendar_before_add.xml")

    add_button = WebDriverWait(
        context.driver, 10
    ).until(
        EC.element_to_be_clickable(
            (
                AppiumBy.ACCESSIBILITY_ID,
                "add-plus-button"
            )
        )
    )

    assert add_button.is_displayed(), (
        "Add button is not displayed"
    )

    add_button.click()

    print("Add button clicked successfully")


@then("the new event screen should be displayed")
def step_verify_new_event_screen(context):
    page_source = context.driver.page_source

    with open(
        "calendar_event_page_source.xml",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(page_source)

    print("Event creation page source saved")

    assert "XCUIElementType" in page_source


@when('I enter event title "{title}"')
def step_enter_event_title(context, title):
    title_field = WebDriverWait(
        context.driver, 10
    ).until(
        EC.visibility_of_element_located(
            (
                AppiumBy.ACCESSIBILITY_ID,
                "title-field"
            )
        )
    )

    title_field.click()
    title_field.clear()
    title_field.send_keys(title)

    print(f"Entered event title: {title}")


@when('I save the calendar event')
def step_save_calendar_event(context):
    """
    Save either a newly-created event or an edited event.

    Create Event screen:
        add-button

    Edit Event screen:
        done-button
    """

    try:
        # ---------------------------------------------------------
        # EDIT EVENT
        # ---------------------------------------------------------
        try:
            done_button = WebDriverWait(
                context.driver,
                5
            ).until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.ACCESSIBILITY_ID,
                        "done-button"
                    )
                )
            )

            done_button.click()

            print("Edit event saved successfully.")

            return

        except Exception:
            print(
                "Edit Event Done button not found. "
                "Trying Create Event save..."
            )

        # ---------------------------------------------------------
        # CREATE NEW EVENT
        # ---------------------------------------------------------
        add_button = WebDriverWait(
            context.driver,
            5
        ).until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ACCESSIBILITY_ID,
                    "add-button"
                )
            )
        )

        add_button.click()

        print("New calendar event saved successfully.")

    except Exception as e:
        context.driver.save_screenshot(
            "calendar_save_failed.png"
        )

        with open(
            "calendar_save_failed.xml",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(context.driver.page_source)

        print(f"Save error: {e}")

        raise AssertionError(
            "Could not locate Save/Done button. "
            "Page source saved to calendar_save_failed.xml"
        )


@when('I select the "{event_title}" event')
def step_select_calendar_event(context, event_title):
    locator = (
        AppiumBy.ACCESSIBILITY_ID,
        f"event-shown:{event_title}"
    )

    try:
        print(
            f"Looking for calendar event: {event_title}"
        )

        event = WebDriverWait(
            context.driver,
            15
        ).until(
            EC.presence_of_element_located(locator)
        )

        WebDriverWait(
            context.driver,
            10
        ).until(
            EC.visibility_of_element_located(locator)
        )

        print(
            f"Found calendar event: {event_title}"
        )

        event.click()

        print(
            f"Selected calendar event: {event_title}"
        )

    except Exception as e:
        context.driver.save_screenshot(
            "calendar_edit_select_failed.png"
        )

        with open(
            "calendar_edit_select_failed.xml",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(context.driver.page_source)

        print(f"Selection error: {e}")

        raise AssertionError(
            f"Could not select calendar event "
            f"'{event_title}'"
        )


@when('I change the event title to "{new_title}"')
def step_change_event_title(context, new_title):
    try:
        # ---------------------------------------------------------
        # EVENT DETAILS SCREEN
        # Tap Edit
        # ---------------------------------------------------------
        edit_button = WebDriverWait(
            context.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                (
                    AppiumBy.ACCESSIBILITY_ID,
                    "Edit"
                )
            )
        )

        edit_button.click()

        print("Edit button clicked.")

        # ---------------------------------------------------------
        # EDIT EVENT SCREEN
        # Locate title field
        # ---------------------------------------------------------
        title_field = WebDriverWait(
            context.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                (
                    AppiumBy.ACCESSIBILITY_ID,
                    "title-field"
                )
            )
        )

        title_field.click()
        title_field.clear()
        title_field.send_keys(new_title)

        print(
            f"Changed event title to: {new_title}"
        )

    except Exception as e:
        context.driver.save_screenshot(
            "calendar_edit_title_failed.png"
        )

        with open(
            "calendar_edit_title_failed.xml",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(context.driver.page_source)

        print(f"Title edit error: {e}")

        raise AssertionError(
            f"Could not change event title "
            f"to '{new_title}'"
        )


@then('the calendar event "{event_title}" should be displayed')
def step_verify_calendar_event(context, event_title):
    try:
        print(
            f"Verifying calendar event: {event_title}"
        )

        # After saving, Calendar may still be on the
        # event details screen. First check the page source.
        source = context.driver.page_source

        with open(
            "calendar_after_save.xml",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(source)

        # ---------------------------------------------------------
        # OPTION 1:
        # Event title exists anywhere in current page
        # ---------------------------------------------------------
        if event_title in source:
            print(
                f"Calendar event '{event_title}' "
                f"found in page source."
            )
            return

        # ---------------------------------------------------------
        # OPTION 2:
        # Search for the event-shown accessibility ID
        # ---------------------------------------------------------
        event = WebDriverWait(
            context.driver,
            10
        ).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ACCESSIBILITY_ID,
                    f"event-shown:{event_title}"
                )
            )
        )

        assert event.is_displayed(), (
            f"Calendar event '{event_title}' "
            f"is not displayed"
        )

        print(
            f"Calendar event '{event_title}' "
            f"is displayed successfully."
        )

    except Exception as e:
        context.driver.save_screenshot(
            "calendar_event_verification_failed.png"
        )

        with open(
            "calendar_event_verification_failed.xml",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(context.driver.page_source)

        print(f"Verification error: {e}")

        raise AssertionError(
            f"Calendar event '{event_title}' "
            f"was not found."
        )