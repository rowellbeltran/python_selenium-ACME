Feature: Test navigation from Login Page

  Scenario: User can log into ACME using valid email and password
    Given I am on login page
    When I enter "valid_value" in "email" field
    And I enter "valid_value" in "password" field
    And I click "Log In" button
    And I wait for the main page to load
    Then I am on the main page

  Scenario Outline: Alert displays correct error message
    Given I am on login page
    When I enter "<email>" in "email" field
    And I enter "<password>" in "password" field
    And I click "Log In" button
    And I wait for the alert
    Then Alert message "<message>" is displayed
    Examples:
    |test case            | email | password | message                              |
    |email is null        |       | pwd      | Plase fill in your email address     |
    |password is null     | email |          | Please fill in your password         |
    |invalid combination  | email | pwd      | Email/Password combo is not correct  |