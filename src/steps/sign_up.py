from behave import given, when, then
import sign_up

@given(u'I click "Create your Amazon account"')
def click_create_account(context):
    """Steps to create a new user"""
    print("click create user button")

@when(u'I type name')
def type_name(context):
    """Steps to create a new user"""
    print("type name")

@when(u'I type re-enter password')
def re_enter_password(context):
    """Steps to create a new user"""
    print("type re-enter password")

@when(u'I click on "Verify mobile number"')
def click_verify_mobile(context):
    """Steps to create a new user"""
    print("verify mobile number")

@when(u'I type OTP')
def type_otp(context):
    """Steps to create a new user"""
    print("type otp")

@when(u'I click "Verify"')
def click_verify(context):
    """Steps to create a new user"""
    print("verify btn")

@when(u'I click on "Verify email"')
def click_verify_email(context):
    """Steps to create a new user"""
    print("verify email")

@when(u'I type an already used email address')
def type_used_email(context):
    """Steps to create a new user"""
    print("used email")

@then(u'I should see the text "You indicated youre a new customer, but an account already exists with the email address')
def already_used_email(context):
    """Steps to create a new user"""
    print("already used email")

@then(u'You indicated youre a new customer, but an account already exists with the phone number')
def already_used_number(context):
    """Steps to create a new user"""
    print("already used number")

@when(u'I type password with less than 6 character')
def type_password_less_characters(context):
    """Steps to create a new user"""
    print("less characters")

@then(u'I should see the text "Minimum 6 characters required"')
def minimum_characters(context):
    """Steps to create a new user"""
    print("minimum characters")

@then(u'I should see the text "Enter your email or mobile phone number"')
def email_password_required(context):
    """Steps to create a new user"""
    print("email and password required")
