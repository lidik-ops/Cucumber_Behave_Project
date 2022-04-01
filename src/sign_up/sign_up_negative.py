Feature: Attempt to sign up with invalid credentials
  Scenario: Creating an account with an already used email address
    Given I click "Create your Amazon account"
    When I type name
    When I type an already used email address
    When I type password
    When I type re-enter password
    When I click on "Verify email"
    Then I should see the text "You indicated youre a new customer, but an account already exists with the email address"

  Scenario: Creating an account with an already used phone number
     Given I click "Create your Amazon account"
     When I type name
     When I type phone number
     When I type password
     When I type re-enter password
     When I click on "Verify mobile number"
     Then I should see the text "You indicated youre a new customer, but an account already exists with the phone number"

  Scenario: Creating an account with a password less that 6 characters
    Given I click "Create your Amazon account"
    When I type name
    When I type phone number
    When I type password with less than 6 character
    When I click on "Verify mobile number"
    Then I should see the text "Minimum 6 characters required"

  Scenario: Creating an account without a password
    Given I click "Create your Amazon account"
    When I type name
    When I type phone number
    When I click "Continue"
    Then I should see the text "Minimum 6 characters required"

  Scenario: Creating an account without a email or password
    Given I click "Create your Amazon account"
    When I type name
    When I type password
    When I type re-enter password
    When I click "Continue"
    Then I should see the text "Enter your email or mobile phone number"