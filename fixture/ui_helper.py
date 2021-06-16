from selenium.webdriver import Firefox, Chrome, Opera

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

    def destroy(self):
        self.wd.quit()




        # for ff
        # elif browser == 'firefox':
        #     self.ff_browser = Firefox()
        #     self.ff_browser.implicitly_wait(10)
        # # for opera
        # elif browser == 'opera':
        #     self.opera_driver = Opera()
        #     self.opera_driver.implicitly_wait(10)


    #def quit_browser_chrome(self):
        #self.chrome_driver = chrome_driver.quit()





