from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time


browser = webdriver.Firefox(executable_path=r"C:\Users\eugen\OneDrive - McGill University\Desktop\Projects\whatsapp messages")
browser.maximize_window()
browser.get('https://web.whatsapp.com/')

with open('contacts.txt', encoding= 'utf8') as f:
    contacts = f.read().splitlines()


with open("msg.txt", encoding= 'utf8') as f:
    message = f.read()


for contact in contacts:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 500).until(
        EC.presence_of_element_located((By.XPATH, search_xpath)))

    search_box.clear()


    time.sleep(5)

    pyperclip.copy(contact)
    search_box.send_keys(Keys.CONTROL, 'v')

    time.sleep(5)

    send_xpath = f'//span[@title="{contact}"]'
    person_name = browser.find_element(By.XPATH, send_xpath)
    person_name.click()
    message_box_xpath = '//div[@contenteditable="true"][@data-tab="10"]'
    message_input = browser.find_element_by_xpath(message_box_xpath)

    time.sleep(5)

    pyperclip.copy(message)
    message_input.send_keys(Keys.CONTROL, 'v')
    message_input.send_keys(Keys.ENTER)


    time.sleep(5)
