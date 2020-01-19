Feature: Test contents of the login page

  Scenario: Login page title is displayed
    Given I am on login page
    Then There is a title shown on the page
    And The title tag contains "Account - Log In"

  Scenario: Login page displays navigation bar
    Given I am on login page
    Then The navigation bar header "ACME System 1" is displayed
    And The navigation link "Home" is displayed
    And The navigation link "Log In" is displayed

  Scenario: Login page displays breadcrumbs
    Given I am on login page
    Then The breadcrumb "Home" is displayed
    And The breadcrumb "Account - Log In" is displayed

  Scenario: Login page displays container header
    Given I am on login page
    Then Login Page displays container header
    And Login Page container header tag contains "To continue, please authenticate here1"

  Scenario: Login page displays email and password fields
    Given I am on login page
    Then There is a field label "Email:" displayed
    And There is a text field "email" displayed
    And There is a field label "Password:" displayed
    And There is a text field "password" displayed

  Scenario: Login page displays buttons
    Given I am on login page
    Then There is a "Log In" button displayed
    And There is a "Forgot Password" button displayed
    And There is a "Register" button displayed

  Scenario: Login page displays footer
    Given I am on login page
    Then There is a footer shown on the page
    And The text displayed is "Copyright © 2020 ACME Systems"
