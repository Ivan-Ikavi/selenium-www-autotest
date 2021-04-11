import pytest
from selenium import webdriver
from time import sleep

def pytest_addoption(parser):
    parser.addoption('--language', default= 'ru')


@pytest.fixture(scope='session')
def browser(request):
    lan=request.config.getoption('language')
    url="http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(lan)
    browser=webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()