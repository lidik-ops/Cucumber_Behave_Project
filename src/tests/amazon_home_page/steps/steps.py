from Utilities.CommonSteps.webstepscommon import *
from Utilities.CommonConfigs import locatorsconfig
from Utilities.CommonFuncs import webcommon


@then('the {nav_bar} should be visible')
def verify_nav_bars_visible(context, nav_bar):
    expected_bars = ['main navigation', 'top navigation', 'side bar hamburger']
    if nav_bar not in expected_bars:
        raise BaseException("The passed in nav_bar type is not one of expected."
                            "Actual: {}, Expected in: {}".format(nav_bar, expected_bars))

    locators_info = locatorsconfig.LOCATORS.get(nav_bar)
    locators_type = locators_info['type']
    locators_text = locators_info['locator']

    nav_element = webcommon.find_element(context, locators_type, locators_text)
    webcommon.assert_element_visible(nav_element)
