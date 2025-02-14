Feature: User Registration

  Scenario: Successful user registration
    Given the user is on the registration page
    When the user enters valid registration details
    And the user submits the registration form
    Then the user should see a registration success message
