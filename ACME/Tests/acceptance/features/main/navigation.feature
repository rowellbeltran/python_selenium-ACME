Feature: Test navigation from Main Page

  Scenario: User can logout from the Main Page
    Given I am on the Main Page
    When I click "Log Out" link from navigation bar
    Then I am on the login page

  Scenario: User can navigate to Work Items from the Main Page
    Given I am on the Main Page
    When I click "Work Items" button
    Then I am on the workitems page
