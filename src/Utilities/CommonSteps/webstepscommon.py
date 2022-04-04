import logging
from behave import given, when, then
from Utilities.CommonFuncs import webcommon

# configuring the logging
logging.basicConfig(level='INFO')


@given(u'I go to the site {url}')
def go_to_url(context, url):
    """Step definition to got to a specific url"""
    logging.info("Navigating to the site: {}".format(url))
    context.driver = webcommon.go_to(url)


@then(u'the page title should be "{expected_title}"')
def verify_home_page_title(context, expected_title):
    webcommon.assert_page_title(context, expected_title)


@then(u'current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    webcommon.assert_current_url(context, expected_url)
