Feature: Creating account with valid credentials
  Scenario: User creating an account successfully with phone number
    Given I click "Create your Amazon account"
    When I type name
    When I type phone number
    When I type password
    When I type re-enter password
    When I click on "Verify mobile number"
    When I type OTP
    And I click "Verify"
    And I click "Create your Amazon account"
    Then I should be redirected to the dashboard

  Scenario: User creating an account successfully with email address
  Given I click "Create your Amazon account"
  When I type name
  When I type email address
  When I type password
  When I type re-enter password
  When I click on "Verify email"
  When I type OTP
  And i click "Verify"
  And I click "Create your Amazon account"
  Then I should be redirected to the dashboard
