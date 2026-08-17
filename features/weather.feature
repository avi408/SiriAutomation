@wip
Feature: Weather using Siri

  As an iPhone user
  I want to ask Siri for the weather
  So that I receive accurate weather information

  Background:
    Given Siri is available

  @smoke
  Scenario: Ask today's weather
    When I activate Siri
    And I ask "What's the weather today?"
    Then Siri should display today's weather

  @regression
  Scenario: Ask tomorrow's weather
    When I activate Siri
    And I ask "What's the weather tomorrow?"
    Then Siri should display tomorrow's forecast

  @regression
  Scenario: Ask for the current temperature
    When I activate Siri
    And I ask "What's the temperature right now?"
    Then Siri should display the current temperature

  @regression
  Scenario: Ask if it will rain today
    When I activate Siri
    And I ask "Will it rain today?"
    Then Siri should display today's rain forecast

  @regression
  Scenario: Ask for weather in a specific location
    When I activate Siri
    And I ask "What's the weather in San Francisco?"
    Then Siri should display the weather for San Francisco