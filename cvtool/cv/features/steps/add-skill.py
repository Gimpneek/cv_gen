from behave import given, when, then


@when('I create a new skill')
@given('I create a new skill')
def go_to_add_skill(context):
    context.browser.get(context.base_url + '/skill/add/')


@then('I should be able to {action} the skill')
def add_data_to_skill(context, action):

    pass
