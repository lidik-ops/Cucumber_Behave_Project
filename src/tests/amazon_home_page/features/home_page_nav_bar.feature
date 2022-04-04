Feature: Navigation bars in the home page
  Scenario: Verify the navigation bars on the homepage are visible
    Given I go to the site "https://www.amazon.com/
    Then the "main navigation" should be visible
    And the "top navigation" should be visible
    And the "side bar hamburger" should be visible