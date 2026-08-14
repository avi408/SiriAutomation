# Siri Automation Framework

A behavior-driven iOS automation framework for Siri-focused scenarios. It uses
Behave for business-readable tests, Appium with XCUITest for device automation,
and a layered design that keeps configuration, driver lifecycle, workflows, and
UI interactions separate.

## Run the implemented smoke scenario

1. Start Appium in a separate terminal:

   ```bash
   appium
   ```

2. From the project root, activate the virtual environment and run Behave:

   ```bash
   source .venv/bin/activate
   behave features/session_initialization.feature
   ```

   Or run all implemented scenarios:

   ```bash
   behave
   ```

The initial feature verifies that Behave can create an Appium session against
the iPhone 17 Pro iOS 26.5 simulator. Siri invocation and response scenarios
will be added through dedicated service and page layers.

## Architecture

```text
Feature file -> step definition -> service layer -> page object -> Appium driver
```

See `docs/` for the test strategy, test plan, quality strategy, and framework
architecture.
