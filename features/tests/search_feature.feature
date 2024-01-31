Feature: Search content by keyword and Date
  Background:
    Given User can enter to the https://www.canvas8.com/login
    And User can login
    Then Verify Home link is present

  Scenario: User will search content by Keyword and Date
    Given User can enter to the https://www.canvas8.com/search
    Then User will input search generations
    Then Scroll down 5 times
    Then Test all articles have content

  Scenario: User will search through date
    Given User can enter to the https://www.canvas8.com/search
    Then User will enter From Date Nov 2022
    Then User will enter To Date Jun 2023
    Then Scroll down 5 times
    Then Test all articles have content

  Scenario: On the all article page content is available
    Given User can enter to the https://www.canvas8.com/search
    Then User click on the Signal
    Then Scroll down 5 times
    Then Test all articles have content
