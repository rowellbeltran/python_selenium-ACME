Feature: Test Contents of the Main Page

  Scenario: ACME Main Page displays page title
    Given I am on the Main Page
    Then There is a title shown on the page
    And The title tag contains "Dashboard"

  Scenario: Main page displays navigation bar
    Given I am on the Main Page
    Then The navigation bar header "ACME System 1" is displayed
    And The navigation link "Home" is displayed
    And The navigation link "Log Out" is displayed

  Scenario: Main page displays breadcrumbs
    Given I am on the Main Page
    Then The breadcrumb "Home" is displayed
    And The breadcrumb "Dashboard" is displayed

  Scenario: Main page displays container header and note
    Given I am on the Main Page
    Then Main Page displays container header
    And Main Page container header tag contains "Welcome, " "valid_email"" to System 1."
    And Container note displays "If this is your first time logging in, please make sure to go to User Options -> Reset Test Data"


  Scenario: Main page displays footer
    Given I am on the Main Page
    Then There is a footer shown on the page
    And The text displayed is "Copyright © 2020 ACME Systems"

  Scenario: Main page displays buttons
    Given I am on the Main Page
    Then There is a "User options" button displayed
    And There is a "Work Items" button displayed
    And There is a "Accounts" button displayed
    And There is a "Checks" button displayed
    And There is a "Vendors" button displayed
    And There is a "Invoices" button displayed
    And There is a "Internal Invoices" button displayed
    And There is a "Reports" button displayed

  Scenario: Dropdown menu displayed when Accounts is clicked
    Given I am on the Main Page
    When I click "Accounts" button
    Then "Add account modification" is available from the dropdown menu
    And "View account history" is available from the dropdown menu

  Scenario: Dropdown menu displayed when Checks is clicked
    Given I am on the Main Page
    When I click "Checks" button
    Then "Search for Check" is available from the dropdown menu
    And "Submit Check Copy" is available from the dropdown menu

  Scenario: Dropdown menu displayed when Vendors is clicked
    Given I am on the Main Page
    When I click "Vendors" button
    Then "Search for Vendor" is available from the dropdown menu
    And "Add Vendor" is available from the dropdown menu

  Scenario: Dropdown menu displayed when Invoices is clicked
    Given I am on the Main Page
    When I click "Invoices" button
    Then "Search for Invoice" is available from the dropdown menu
    And "Add Invoice Details" is available from the dropdown menu
    And "Delete Invoice" is available from the dropdown menu

  Scenario: Dropdown menu displayed when Internal Invoices is clicked
    Given I am on the Main Page
    When I click "Internal Invoices" button
    Then "Download Monthly Invoices" is available from the dropdown menu
    And "Download Full Invoice Report" is available from the dropdown menu

  Scenario: Dropdown menu displayed when Internal Reports is clicked
    Given I am on the Main Page
    When I click "Reports" button
    Then "Download Monthly Report" is available from the dropdown menu
    And "Upload Yearly Report" is available from the dropdown menu