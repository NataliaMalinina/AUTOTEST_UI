from fixture.ui_helper import User_helper
import pytest


@pytest.fixture()
def chrome_browser():
    fixture = User_helper(browser='chrome')
    return fixture


@pytest.fixture(scope="session")
def ff_browser():
    fixture = User_helper(browser='firefox')
    return fixture


@pytest.fixture()
def opera_browser():
    fixture = User_helper(browser='opera')
    return fixture





# #Fixture for FF
# @pytest.fixture(scope="class")
# def driver_init_ff():
#     ff_driver = Firefox()
#     ff_driver.get('https://guest:WelcomeToTest@apteka.tech')
#     yield
#     ff_driver.quit()
#
#
# #Fixture for Chrome
# @pytest.fixture(scope="class")
# def driver_init_chrome():
#     chrome_driver = Chrome()
#     #chrome_driver.get('https://guest:WelcomeToTest@apteka.tech')
#     yield
#     chrome_driver.quit()
#
#
# #Fixture for Opera
# @pytest.fixture(scope="class")
# def driver_init_opera():
#     opera_driver = Opera()
#     opera_driver.get('https://guest:WelcomeToTest@apteka.tech')
#     yield
#     opera_driver.quit()
#
#
#
#






# @pytest.fixture(scope='session')
# def config_browser(config):
#     if "browser" not in config:
#         raise Exception('The config file does not contain "browser"')
#     elif config['browser'] not in ['chrome', 'firefox', 'Opera']:
#         raise Exception(f'"{config["browser"]}" is not a supported browser')
#     return config['browser']
#
#
# @pytest.fixture(scope='session')
# def config_wait_time(config):
#     return config['wait_time'] if 'wait_time' in config else 10
