from behave import given, when, then
import login
import logging as logger

@given(u'I create a user')
def create_new_user(context):
    """Steps to create a new user"""
    print("I am a new user")
    logger.info("New user login")
    logger.debug("Failed")

@when(u'I type phone number')
def type_phone_number(context):
    """Steps to type aphone numberr"""
    print("Ttype phone number")

@when(u'I click "Continue"')
def click_continue(context):
    """Steps to click continue"""
    print("click on Continue")

@when(u'I type password')
def type_password(context):
    """Steps type password"""
    print("type password")

@when(u'I click on "Sign in"')
def click_signin(context):
    """Steps click sign in"""
    print("click sign in")

@then(u'I should be redirected to the dashboard')
def Should_redirect_to_dashboard(context):
    """Steps to redirect to dashboard"""
    print("redirect to dashboard")

@when(u'I type email')
def type_email(context):
    """Steps to type email"""
    print("type email")

@when(u'I type correct email')
def type_correct_email(context):
    """Steps to type email"""
    print("type email")

@given(u'I generate a random email address')
def generate_random_email(context):
    """Steps to generate random email"""
    print("generate random email")

@when(u'I type random email')
def type_random_email(context):
    """Steps to type random email"""
    print("type random emaill")

@then(u'i should see the text "We cannot find an account with that email address"')
def Should_account_not_found(context):
    """Steps to redirect to dashboard"""
    print("Account not found")

@when(u'I type random password')
def type_random_password(context):
    """Steps to type random password"""
    print("type random password")

@then(u'I should see the text "Your password is incorrect"')
def Should_see_incorrect_password(context):
    """Steps to redirect to dashboard"""
    print("incorrect_password")

@then(u'I should see the text "Enter your password"')
def Should_see_enter_password_error(context):
    """Steps to redirect to dashboard"""
    print("enter password")

@when(u'I type invalid email format')
def type_invalid_email_format(context):
    """Steps to type invalid email format"""
    print("type invalid password")
