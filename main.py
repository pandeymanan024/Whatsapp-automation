from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome("/Users/Manc/Downloads/chromedriver_win32/chromedriver")
browser.get("https://web.whatsapp.com/")
wait = WebDriverWait(browser,600)

target = '"Golu"'
file_path = input("Enter the file path ")
string = input("Enetr the msg")
x_arg = '//span[contains(@title, ' + target +')]'
target = wait.until(ec.presence_of_element_located((By.XPATH,x_arg)))
target.click()

input_box = browser.find_element_by_class_name('_1Plpp')

for i in range(5):
    input_box.send_keys(string + Keys.ENTER)
    
    
attachment_section = browser.find_element_by_xpath('//div[@title = "Attach"]')
attachment_section.click()

image_box = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image_box.send_keys(file_path)

sleep(3)

send_button = browser.find_element_by_xpath('//span[@data-icon="send-light"]')
send_button.click()
