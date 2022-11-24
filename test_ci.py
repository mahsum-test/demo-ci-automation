from selenium import webdriver
import time


def test_example():

    browser_options = webdriver.ChromeOptions()
    browser_options.add_argument("start-maximized")

    #driver = webdriver.Remote(command_executor="http:// 192.168.1.130:4444", options=browser_options)
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)


    driver.get("http://www.mahsumakbas.net")

    time.sleep(5)

    driver.quit()