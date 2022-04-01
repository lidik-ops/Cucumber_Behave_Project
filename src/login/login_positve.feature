Feature: Logging in with valid credentials
  Scenario: User login successfully with phone number
    Given I create a user
    When I type phone number
    When I click "Continue"
    When I type password
    When I click on "Sign in"
    Then I should be redirected to the dashboard

  Scenario: User login successfully with email
    Given I create a user
    When I type email
    When I click "Continue"
    When i type password
    When i click on "Sign in"
    Then I should be redirected to the dashboard