import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as fire_for_options

# Toggle to turn on/off headless function
options_chrome = Options()
options_chrome.headless = False

# Toggle to turn on/off headless function
options_fire_fox = fire_for_options()
options_fire_fox.headless = False

@pytest.fixture(params=['chrome', "firefox"], scope='function')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options_chrome)
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH, options=options_fire_fox)
    request.cls.driver = web_driver
    yield
    web_driver.close()