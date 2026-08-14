"""Behave lifecycle hooks for the Siri automation suite."""

import allure

from core.driver_manager import DriverManager
from utils.screenshots import Screenshot


def before_all(context):
    print("=== BEFORE ALL EXECUTED ===")


def before_scenario(context, scenario):
    print(f"\n=== Starting Scenario: {scenario.name} ===")

    context.driver = DriverManager.get_driver()


def after_step(context, step):

    if step.status == "failed" and hasattr(context, "driver"):

        screenshot = Screenshot.capture(
            context.driver,
            step.name.replace(" ", "_")
        )

        allure.attach.file(
            str(screenshot),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

        allure.attach(
            context.driver.page_source,
            name="Page Source",
            attachment_type=allure.attachment_type.XML
        )


def after_scenario(context, scenario):

    if hasattr(context, "driver"):

        DriverManager.quit_driver()

        print(f"=== Finished Scenario: {scenario.name} ===")