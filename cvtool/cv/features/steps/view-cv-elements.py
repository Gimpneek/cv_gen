from behave import given, when, then
from selenium.webdriver.common.by import By


@given('I view the listing of {listing}')
@when('I view the listing of {listing}')
def load_listing(context, listing):
    """
    Load up the specified listing
    """
    context.browser.get(context.base_url + '/' + listing)


@then('I should be able to see the {item_type} I\'ve added to the system')
def check_listing(context, item_type):
    """
    Check the listing has the data we expect
    """
    list_item_selector = (By.CSS_SELECTOR, '#listing a')
    items = {
        'skills': [
            'Continuous Delivery',
            'Continuous Integration'
        ],
        'experiences': [
            'Software Development Manager - NeovaHealth'
        ],
        'educations': [
            'Thames Valley University'
        ],
        'profiles': [
            'Colin Wren'
        ]
    }
    links = context.browser.find_elements(*list_item_selector)
    assert([link.text for link in links] == items[item_type])