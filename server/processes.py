import time
import pandas as pd
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def process_data(done_tasks):
    textStream = StringIO()
    df = pd.DataFrame(done_tasks)
    df.to_csv(textStream)
    return textStream


def automate():
    driver = webdriver.Chrome()
    driver.get('https://id.atlassian.com/login')

    input_elem = driver.find_element(
        by=By.CSS_SELECTOR, value='input[name="username"]')
    input_elem.clear()
    input_elem.send_keys('here_an_email hehe')
    input_elem.send_keys(Keys.RETURN)

    time.sleep(0.1)

    password_elem = driver.find_element(
        by=By.CSS_SELECTOR, value='input[name="password"]')
    password_elem.clear()
    password_elem.send_keys("here_a_password hehe")
    password_elem.send_keys(Keys.RETURN)

    time.sleep(5)

    trello_button = driver.find_element(
        by=By.XPATH, value='//div[contains(text(), "Trello")]')
    trello_button.click()

    time.sleep(5)

    driver.get('https://trello.com/path/to/trello/board')

    time.sleep(5)

    done_text = driver.find_element(
        by=By.XPATH, value='//h2[contains(text(), "done")]')
    done_card = done_text.find_element(
        by=By.XPATH, value='./ancestor::div[contains(@class, "js-list-content")]')
    done_tasks = done_card.find_elements(
        by=By.CLASS_NAME, value="js-card-name")

    done_texts = list(map(lambda el: el.text, done_tasks))

    driver.close()

    return process_data(done_texts)


if __name__ == '__main__':
    automate()
