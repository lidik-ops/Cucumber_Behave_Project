import logging
from behave import given, when, then
from Utilities.CommonFuncs import webcommon
from Utilities.CommonConfigs import urlconfig

# configuring the logging
logging.basicConfig(level='INFO')


@given(u'I go to the site {site}')
def go_to_url(context, site):
    """Step definition to got to a specific url"""
    url = urlconfig.URLCONFIG.get(site)
    logging.info("Navigating to the site: {}".format(site))
    context.driver = webcommon.go_to(url)


@then(u'the page title should be "{expected_title}"')
def verify_home_page_title(context, expected_title):
    webcommon.assert_page_title(context, expected_title)


@then(u'current url should be "{expected_url}"')
def verify_current_url(context, expected_url):
    webcommon.assert_current_url(context, expected_url)
