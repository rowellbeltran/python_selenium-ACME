Feature: Test Contents of the Workitems Page

  Scenario: ACME Workitems Page displays page title
    Given I am on the Workitems Page
    Then There is a title shown on the page
    And The title tag contains "Work Items"

  Scenario: Workitems page displays navigation bar
    Given I am on the Workitems Page
    Then The navigation bar header "ACME System 1" is displayed
    And The navigation link "Home" is displayed
    And The navigation link "Log Out" is displayed

  Scenario: Workitems page displays breadcrumbs
    Given I am on the Workitems Page
    Then The breadcrumb "Home" is displayed
    And The breadcrumb "Work Items" is displayed

  Scenario: Workitems page displays footer
    Given I am on the Workitems Page
    Then There is a footer shown on the page
    And The text displayed is "Copyright © 2020 ACME Systems"

  Scenario: Workitems page displays Work Items Panel
    Given I am on the Workitems Page
    Then The panel header displays "Search Results"
    And The panel text displays "Please find below your work items. They need to be completed in the order specified by your manager."

  Scenario: Workitems page displays Work Items Table
    Given I am on the Workitems Page
    Then The table displays row headers
    And The table displays max of 10 rows
    And Each row contains "search" icon
    And Each row contains "trash" icon

  Scenario: Workitems page displays page numbers
    Given I am on the Workitems Page
    Then The page numbers are displayed
    And "1" page number is "displayed" and "not enabled"
    And ">" page number is "displayed" and "enabled"
    And "<" page number is "not displayed" and "not enabled"

  Scenario: Work items from DB are all displayed
    Given I am on the Workitems Page
    Then Count of work items is the same as database

  Scenario Outline: Workitem details displayed correctly
    Given I am on the Workitems Page
    Then The correct "Description" is displayed for WIID: "<work_item>"
    And The correct "Type" is displayed for WIID: "<work_item>"
    And The correct "Status" is displayed for WIID: "<work_item>"
    And The correct "Date" is displayed for WIID: "<work_item>"

    Examples:
    | type | work_item |
    | WI1  | 531381    |
    | WI2  | 190992    |
    | WI3  | 444603    |
    | WI4  | 429494    |
    | WI5  | 476135    |

  Scenario Outline: Details are displayed  in Work Item Details Page
    Given I am on the Workitems Page
    When I click on "search" button of WIID: "<work_item>"
    Then The panel header displays "<description>"
    And The "Work Item Details" section header is displayed
    And The correct "WIID" is displayed for WIID: "<work_item>" in Work Item Details Section
    And The correct "Type" is displayed for WIID: "<work_item>" in Work Item Details Section
    And The correct "Status" is displayed for WIID: "<work_item>" in Work Item Details Section
    And The correct "Date" is displayed for WIID: "<work_item>" in Work Item Details Section

    Examples:
    | type | description                       | work_item |
    | WI1  | Verify Account Positions          | 531381    |
    | WI2  | Research Client Check Copy        | 190992    |
    | WI3  | Process Vendor Invoice            | 444603    |
    | WI4  | Generate Yearly Report for Vendor | 429494    |
    | WI5  | Calculate Client Security Hash    | 476135    |

