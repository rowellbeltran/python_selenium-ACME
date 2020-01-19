Feature: Test navigation from Work Items Page

  Scenario: Navigated to Home Page when Home from breadcrumbs is clicked
    Given I am on the Workitems Page
    When I click on "Home" from breadcrumbs
    Then I am on the main page

  Scenario: Navigated to Home Page when Home from navigation bar
    Given I am on the Workitems Page
    When I click on "Home" from navigation bar
    Then I am on the main page

  Scenario: Next and Previous page buttons displayed when on the 2nd page
    Given I am on the Workitems Page
    When I click on ">" page button
    Then From page "1" I am on the "next" page
    And "1" page number is "displayed" and "enabled"
    And ">" page number is "displayed" and "enabled"
    And "<" page number is "displayed" and "enabled"

  Scenario: Next page button not displayed when on the last page
    Given I am on the Workitems Page
    When I click on "last" page button
    Then From page "1" I am on the "last" page
    And "1" page number is "displayed" and "enabled"
    And ">" page number is "not displayed" and "not enabled"
    And "<" page number is "displayed" and "enabled"

  Scenario: Navigated to Work Items Details when search icon is clicked
    Given I am on the Workitems Page
    When I click on "search" button of WIID: "960791"
    Then I am on work item details page of WIID: "960791"

