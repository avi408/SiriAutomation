@smoke @infrastructure
Feature: Appium session initialization
  As a test engineer
  I want the BDD suite to connect to the configured iOS simulator
  So that Siri scenarios can run on a valid automation session

  Scenario: Create an Appium session for the iPhone simulator
    Given the Appium session is available
    Then the session should have an identifier
