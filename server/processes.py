from selenium import webdriver


def automate():
    driver = webdriver.Chrome()
    driver.get('https://www.python.org')
    driver.close()
