import time


def test_authorization(chrome_browser):
    chrome_browser.wd.set_window_size(1920, 1329)
    open_home_page = chrome_browser.open_home_page()
    time.sleep(1)
    close_town_pop_up = chrome_browser.wd.find_element_by_css_selector('#app > div.overlay-wrapper > div > button').click()
    time.sleep(2)
    auth_button = chrome_browser.wd.find_element_by_css_selector('#app > div.body__header > header > div > div.SideToolbarContainer > div > div.SideToolbarItem.SideToolbarItem--login > div > div > a > span.HeaderButtonIcon').click()
    time.sleep(2)
    нужно найти элемент с инпутом а потом передать туда ключи.send_keys('79139519213')
    time.sleep(2)




