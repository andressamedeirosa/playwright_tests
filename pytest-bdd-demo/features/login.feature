Feature: Login

  Scenario: Successful login
    Given the user is on the login page
    When the user enters valid credentials
    And the user submits the login form
    Then the user should be redirected to the homepage
