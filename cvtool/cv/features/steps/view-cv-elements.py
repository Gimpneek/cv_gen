from behave import given, when, then
from selenium.webdriver.common.by import By
from cv.views import SkillUpdateView, ExperienceUpdateView
from cv.views import EducationUpdateView, ProfileUpdateView
import page_helpers


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
    links = context.browser.find_elements(*page_helpers.list_item_selector)
    assert([link.text for link in links] == items[item_type])


@when('I click on a {item} in the list')
def click_list_item(context, item):
    """
    Click on list item
    """
    links = context.browser.find_elements(*page_helpers.list_item_selector)
    links[0].click()


@when('I click on the "Add {item}" button')
def click_add_element_button(context, item):
    """
    Click on the button to add element
    """
    button = \
        context.browser.find_element(*page_helpers.add_element_button_selector)
    button.click()


@then('I should be able to edit the {item}')
@then('I should be taken to a form to add a {item}')
def view_edit_form(context, item):
    """
    Verify on edit form
    """
    switch = {
        'skill': SkillUpdateView.fields,
        'experience': ExperienceUpdateView.fields,
        'education': EducationUpdateView.fields,
        'profile': ProfileUpdateView.fields
    }
    form_elements = switch[item]
    for form_element in form_elements:
        locator = (By.NAME, form_element)
        context.browser.find_element(*locator)
