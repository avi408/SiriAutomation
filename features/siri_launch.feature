Feature: Siri Launch

  As an iPhone user
  I want to activate Siri
  So that I can interact with the voice assistant

  Background:
    Given the Appium driver is initialized

  @smoke @siri
  Scenario: Launch Siri

    When I activate Siri

    Then Siri interface should be available