Feature: Calendar App

  @smoke
  Scenario: Select today's date
    Given the Calendar app is launched
    Then the Calendar interface should be displayed
    When I select today's date
    Then today's date should be selected

  @smoke
  Scenario: Open new calendar event
    Given the Calendar app is launched
    When I tap the Add button
    Then the new event screen should be displayed

  @smoke
  Scenario: Create a new calendar event
    Given the Calendar app is launched
    When I tap the Add button
    And I enter event title "QA Interview"
    And I save the calendar event
    Then the calendar event "QA Interview" should be displayed

  @regression
Scenario: Edit an existing calendar event
    Given the Calendar app is launched
    When I select the "QA Interview" event
    And I change the event title to "QA Automation Interview"
    And I save the calendar event
    Then the calendar event "QA Automation Interview" should be displayed