Feature: Attempt to login with invalid credentials
  Scenario: None existing user try to login
    Given I generate a random email address
    When I type random email
    When I click "Continue"
    Then i should see the text "We cannot find an account with that email address"

  Scenario: User try to login with wrong password
    Given I create a user
    When I type correct email
    When I click "Continue"
    When I type random password
    When I click on "Sign in"
    Then I should see the text "Your password is incorrect"

  Scenario: User try login without password
    Given I create a user
    When I type correct email
    When I click "Continue"
    When I click on "Sign in"
    Then I should see the text "Enter your password"

  Scenario: User try login with invalid email format
    When I type invalid email format
    When I click "Continue"
    Then I should see the text "We cannot find an account with that email address"