"""Module containing common functions used in several tests.
Functions that are not test or feature specific."""

from selenium import webdriver


def go_to(url, browser_type=None):
    """Function to start instance of a specific browser and navigate to a specific url"""
    if not browser_type:
        driver = webdriver.Chrome()
    elif browser_type.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception("The browser type '{}' is not supported")

    # Clean the url and got to url
    import pdb;
    pdb.set_trace()
    url = url.strip()
    url = 'https://' + url
    driver.get(url)

    return driver


def assert_page_title(context, expected_title):
    actual_title = context.driver.title
    assert expected_title == actual_title, "The title is not as expected." \
                                           "Expected: {}, Actual: {}".format(expected_title, actual_title)
    print("The page title is as expected")


def assert_current_url(context, expected_url):
    current_url = context.driver.current_url
    if not expected_url.startswith('http') or not expected_url.startswith('https'):
        expected_url = 'https://' + expected_url + '/'
    assert current_url == expected_url, "The current url is not as expected." \
                                        "Actual: {}, Expected: {}".format(current_url, expected_url)
    print("The page url is as expected")


def find_element(context, locator_attribute, locator_text):
    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name",
                         "css selector"]

    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes.' \
                        'The approved attributes are : %s' % possible_locators)
    try:
        element = context.driver.find_element(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)


def is_element_visible(element):
    if element.is_displayed():
        return True
    else:
        return False


def assert_element_visible(element):
    if not element.is_displayed():
        raise AssertionError('The element is not displayed')

