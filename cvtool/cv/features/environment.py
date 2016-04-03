from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Firefox()


def after_all(context):
    context.browser.close()


def before_feature(context, feature):
    if 'fixtures' in feature.tags:
        context.fixtures = ['demo-fixtures.json']


def before_scenario(context, scenario):
    context.browser.get(context.base_url)
