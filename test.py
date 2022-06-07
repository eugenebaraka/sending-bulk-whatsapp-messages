from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox(executable_path=r"C:\Users\eugen\OneDrive - McGill University\Desktop\Projects\whatsapp messages")
browser.maximize_window()
browser.get('https://web.whatsapp.com/')

with open('contacts.txt', encoding= 'utf8') as f:
    contacts = f.read().splitlines()


with open("msg.txt", encoding= 'utf8') as f:
    message = f.read()


for contact in contacts:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 500).until(EC.presence_of_element_located((By.XPATH, search_xpath)))
    searchbox.send_keys(contact)


