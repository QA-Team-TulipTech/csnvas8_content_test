Feature: Testing content pages
  Background:
    Given User can enter to the https://www.canvas8.com/login
    And User can login
    Then Verify Home link is present

  Scenario: On the all article page content is available
    Given User can enter to the https://www.canvas8.com/searc
    Then scroll down 20 times
    Then Test all articles have content