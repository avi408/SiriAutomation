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
