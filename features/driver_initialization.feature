Feature: Driver Initialization

  As a QA Automation Engineer
  I want the framework to establish an Appium session
  So that iOS automation scenarios can execute successfully

  @smoke @framework
  Scenario: Successfully initialize the Appium driver

    Given the iOS simulator is available
    When the automation framework initializes the driver
    Then an Appium session should be created
    And the session id should not be empty