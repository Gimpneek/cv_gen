""" Helpers for finding page elements """
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


LIST_ITEM_SELECTOR = (By.CSS_SELECTOR, '#listing a')
ADD_ELEMENT_BUTTON_SELECTOR = (By.ID, 'add_cv_element')
FORM_SUBMIT_BUTTON = (By.ID, 'form_submit')
ADD_DATA_ACTIONS = {
    'my name': {
        'key': 'name',
        'data': 'Test Name'
    },
    'my email address': {
        'key': 'email',
        'data': 'test@test.com'
    },
    'a link to my website': {
        'key': 'website',
        'data': 'http://test.com'
    },
    'a link to my portfolio': {
        'key': 'portfolio',
        'data': 'http://portfolio.test.com'
    },
    'a paragraph that describes me': {
        'key': 'personal_statement',
        'data': 'Now, this is a story all about how '
                'My life got flipped-turned upside down '
                'And I\'d like to take a minute '
                'Just sit right there '
                'I\'ll tell you how I became the prince of a town called '
                'Test'
    },
    'a name for the skill': {
        'key': 'name',
        'data': 'Test skill'
    }
}
SELECT_DATA_ACTIONS = {
    'the proficiency I have in that skill': {
        'key': 'proficiency',
        'data': 'No Proficiency'
    },
    'if the skill is current practice or not': {
        'key': 'freshness',
        'data': 'Not Current Practice'
    }
}


def insert_data(context, key, data):
    input_selector = (By.NAME, key)
    input_el = context.browser.find_element(*input_selector)
    input_el.send_keys(data)
    return input_el.get_attribute('value')


def select_data(context, key, data):
    input_selector = (By.NAME, key)
    input_el = context.browser.find_element(*input_selector)
    select = Select(input_el)
    select.select_by_visible_text(data)
    return select.first_selected_option.text
