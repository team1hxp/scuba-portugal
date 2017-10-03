Feature: Welcome Page

  As a register user 
  Go to welcome page
  So that be welcome

  Scenario: Access to welcome page  
    Given I am on the home page
    When I click welcome menu
    Then I should see the welcome page

  Scenario: Welcome page register user 
    Given I am on the welcome page
    Then I expect to see the welcome message
    