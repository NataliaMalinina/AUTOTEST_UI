from selenium.webdriver import Firefox, Chrome, Opera
import selenium.common.exceptions as ex
import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC


#chrome_browser.wd.set_window_size(1024, 1329) - тест для разных разрешений экрана


class User_helper:

    def __init__(self, browser):
        self.browser = 'chrome' or 'firefox' or 'opera'
        if browser == "firefox":
            self.wd = Firefox()
        elif browser == "chrome":
            self.wd = Chrome()
        elif browser == "opera":
            self.wd = Opera()
        self.wd.implicitly_wait(6)


    def open_home_page(self):
        wd = self.wd
        home_page = wd.get('https://guest:WelcomeToTest@apteka.tech')

    def auth_user(self):
        wd = self.wd
        wd.delete_all_cookies()
        try:
            close_town_pop_up = wd.find_element_by_css_selector('#app > div.overlay-wrapper > div > button').click()  #закрываем поп-ап с городами
        except ex.NoSuchElementException:
            pass
        time.sleep(1)

        try:
            auth_button = wd.find_element_by_css_selector('.SideToolbarContainer > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)').click()

        except ex.ElementNotInteractableException or ex.NoSuchElementException:
            auth_button = wd.find_element_by_css_selector('#app > div.body__header > header > div > div.LowerPanelsContainer > '
                                                          'div > div.LowerPanelItem.LowerPanelItem--login > div > div > a > span.HeaderButtonIcon > svg').click()
        except ex.ElementNotVisibleException:
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            auth_button = wd.find_element_by_css_selector(
                '#app > div.body__header > header > div > div.LowerPanelsContainer > '
                'div > div.LowerPanelItem.LowerPanelItem--login > div > div > a > span.HeaderButtonIcon > svg').click()

        time.sleep(2)
        input_phone = wd.find_element_by_css_selector('input#authorizer-input-username') #ищем элемент, чтобы кликнуть
        input_phone.send_keys('79139519213')   #передаём номер телефона в поле
        input_password = wd.find_element_by_css_selector('input#authorizer-input-password') #ищем элемент, чтобы кликнуть
        input_password.send_keys('9213') #передаём пароль в поле
        time.sleep(2)
        press_auth_button = wd.find_element_by_class_name('AuthorizerForm__submit').click() # нажимаем на кнопку авторизации
        time.sleep(9)

    def destroy(self):
        self.wd.quit()

