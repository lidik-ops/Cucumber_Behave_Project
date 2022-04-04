"""Module containing common functions used in several tests.
Functions that are not test or feature specific."""

from selenium import webdriver


def go_to(url, browser_type=None):
    """Function to start instance of a specific browser and navigate to a specific url"""
    print("already here")
    if not browser_type:
        driver = webdriver.Chrome()
    elif browser_type.lower() == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise Exception("The browser type '{}' is not supported")

    # Clean the url and got to url
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


def assert_text_visible(text):
    pass


def assert_element_visible(element):
    pass
