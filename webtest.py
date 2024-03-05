from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

firefox_path = 'D:\\Drivers\\geckodriver.exe'
ie_path = 'D:\\Drivers\\IEDriverServer.exe'
edge_path = 'D:\\Drivers\\msedgedriver.exe'

slow_down = 1

website_url = 'https://youtube.com'

driver_paths = [firefox_path, edge_path]

for i, path in enumerate(driver_paths):
    match i:
        case 0:
            driver = webdriver.Firefox()
        case 1:
            driver = webdriver.Edge()

    driver.get(website_url)
    driver.get(website_url)
    # sleep(slow_down/2)
    driver.maximize_window()
    print(driver.title)
    wait = WebDriverWait(driver, timeout=3)

    sleep(slow_down)
    # click style-scope ytd-topbar-menu-button-renderer class
    result = wait.until(lambda d: d.find_element(by=By.CLASS_NAME, value='style-scope ytd-topbar-menu-button-renderer'))
    result.click()
    sleep(slow_down)
    # click ytd-toggle-theme-compact-link-renderer class
    result = wait.until(lambda d: d.find_element(by=By.CLASS_NAME, value='ytd-toggle-theme-compact-link-renderer'))
    result.click()
    sleep(slow_down)
    # click element with text "Light theme"
    result = wait.until(lambda d: d.find_element(by=By.XPATH, value='//*[text()="Light theme"]'))
    result.click()
    sleep(slow_down*2)

    # click Trending title text
    result = wait.until(lambda d: d.find_element(by=By.XPATH, value='//*[text()="Trending"]'))
    result.click()
    sleep(slow_down)

    # click guide-icon id
    result = wait.until(lambda d: d.find_element(by=By.ID, value='guide-icon'))
    result.click()

    # hover top video link /watch?v=FEG8m5pRIcs
    result = wait.until(lambda d: d.find_element(by=By.XPATH, value='//*[text()="He Bought A House On Amazon"]'))
    ActionChains(driver).move_to_element(result).perform()

    sleep(slow_down*4)

    driver.quit()
    sleep(1)
