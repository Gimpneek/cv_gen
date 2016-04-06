""" Implementation of steps in add-{element}.feature """
from behave import given, when, then
from django.core.urlresolvers import reverse_lazy
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as ec
import page_helpers


@when('I create a new {element}')
@given('I create a new {element}')
def go_to_add_profile(context, element):
    if element == 'personal profile':
        element = 'profile'
    context.element_section = element
    context.browser.get(
        context.base_url + str(reverse_lazy('{0}-new'.format(element))))


@then('I should be able to add {action}')
def add_data_to_form(context, action):
    action_data = page_helpers.ADD_DATA_ACTIONS.get(action)
    key = action_data.get('key')
    data = action_data.get('data')
    added_data = page_helpers.insert_data(context, key, data)
    assert(added_data == data)


@then('I should be able to submit the form by only adding')
def add_minimal_data_submit(context):
    for row in context.table:
        action_data = page_helpers.ADD_DATA_ACTIONS.get(row.get('information'))
        key = action_data.get('key')
        data = action_data.get('data')
        page_helpers.insert_data(context, key, data)
    submit = context.browser.find_element(*page_helpers.FORM_SUBMIT_BUTTON)
    submit.click()
    ui.WebDriverWait(context.browser, 5).until(
        ec.visibility_of_element_located(
            page_helpers.ADD_ELEMENT_BUTTON_SELECTOR
        )
    )
    element = context.element_section
    if element == 'profile' or element == 'skill':
        element = '{0}s'.format(element)
    assert(
        context.browser.current_url == context.base_url + str(
            reverse_lazy('{0}_list'.format(element))
        )
    )
