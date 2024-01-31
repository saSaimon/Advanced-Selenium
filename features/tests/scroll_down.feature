Feature: Testing content pages
  Background:
    Given User can enter to the https://www.canvas8.com/login
    And User can login
    Then Verify Home link is present

  Scenario: On the all article page content is available
    Given User can enter to the https://www.canvas8.com/search
#    Then scroll down
    Then User click on the Behaviour