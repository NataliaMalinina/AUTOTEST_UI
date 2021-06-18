import time


def test_authorization_chrome(chrome_browser):
    chrome_browser.wd.set_window_size(1920, 1330)
    open_home_page = chrome_browser.open_home_page()
    assert 'Apteka.ru' in chrome_browser.wd.title
    time.sleep(1)
    authorization_user = chrome_browser.auth_user()
    assert '∗92-13' in chrome_browser.wd.page_source
    exit = chrome_browser.destroy()


def test_authorization_ff(ff_browser):
    ff_browser.wd.set_window_size(1920, 1330)
    open_home_page = ff_browser.open_home_page()
    assert 'Apteka.ru' in ff_browser.wd.title
    time.sleep(1)
    authorization_user = ff_browser.auth_user()
    assert '∗92-13' in ff_browser.wd.page_source
    exit = ff_browser.destroy()


def test_authorization_opera(opera_browser):
    opera_browser.wd.set_window_size(1024, 1330)
    open_home_page = opera_browser.open_home_page()
    assert 'Apteka.ru' in opera_browser.wd.title
    time.sleep(1)
    authorization_user = opera_browser.auth_user()
    assert '∗92-13' in opera_browser.wd.page_source
    exit = opera_browser.destroy()
