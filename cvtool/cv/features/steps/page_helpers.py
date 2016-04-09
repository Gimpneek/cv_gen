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
    },
    'the company I worked for': {
        'key': 'company',
        'data': 'Test Corp'
    },
    'the position I held in the job': {
        'key': 'role',
        'data': 'Senior Test Executor'
    },
    'the date I started the job': {
        'key': 'start_date',
        'data': '2013-11-05'
    },
    'the date I ended the job if applicable': {
        'key': 'end_date',
        'data': '2016-03-08'
    },
    'the name of the institution I studied at': {
        'key': 'institution',
        'data': 'Test University'
    },
    'the date I started the education': {
        'key': 'start_date',
        'data': '2006-09-01'
    },
    'the date I finished the education': {
        'key': 'end_date',
        'data': '2009-06-01'
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
MULTISELECT_DATA_ACTIONS = {
    'a tag to the skill': {
        'key': 'tags',
        'data': ['TDD', 'Quality']
    },
    'a responsibility I had in the job': {
        'key': 'responsibilities',
        'data': ['Running tests']
    },
    'a project I did at the job': {
        'key': 'projects',
        'data': ['Living Documentation']
    },
    'a course I took as part of the education': {
        'key': 'courses',
        'data': ['BA (Hons) Digital Arts']
    },
    'a project I did as part of my studies': {
        'key': 'projects',
        'data': ['Augmented Reality']
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


def select_multi(context, key, data):
    input_selector = (By.NAME, key)
    input_el = context.browser.find_element(*input_selector)
    select = Select(input_el)
    for item in data:
        select.select_by_visible_text(item)
    return [opt.text for opt in select.all_selected_options]
