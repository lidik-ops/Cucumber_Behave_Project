Feature: Verifying the home page url goes to the right place

  Scenario: The amazon home page should have a correct page title
    Given I go to the site "amazon.com"
    Then the page title should be "Amazon.com. Spend less. Smile more."

  Scenario: The amazon home page should have a correct url
    Given I go to the site "https://www.amazon.com/"
    Then Current url should be "https://www.amazon.com/"