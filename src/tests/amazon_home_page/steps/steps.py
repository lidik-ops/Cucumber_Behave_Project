from Utilities.CommonSteps.webstepscommon import *


@then('the {nav_bar} should be visible')
def verify_nav_bars_visible(context, nav_bar):
    expected_bars = ['main navigation', 'top navigation', 'side bar hamburger']
    if nav_bar not in expected_bars:
        raise BaseException("The passed in nav_bar type is not one of expected."
                            "Actual: {}, Expected in: {}".format(nav_bar, expected_bars))

    if nav_bar == 'main navigation':
        element = "//div[@id='nav-xshop-container']"
        context.webdriver.find_element_by_xpath(element)
    elif nav_bar == 'top navigation':
        element = "//div[@id='nav-belt']"
        context.webdriver.find_element_by_xpath(element)
    else:
        element = "//a[@id='nav-hamburger-menu']"
        context.webdriver.find_element_by_xpath(element)
