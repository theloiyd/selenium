from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import load_workbook
from selenium.webdriver.common.keys import Keys

wb = load_workbook(r"C:\users\leoce\Desktop\Mappe1.xlsx")
sheet_obj = wb.active
m_row = sheet_obj.max_row
browser = webdriver.Firefox()
cell_obj = sheet_obj.cell(row=2, column=1)

browser.get(
    "https://www.amazon.de/ring-video-doorbell-wired/dp/B08LR3G17D/ref=sr_1_2?keywords=ring&qid=1652445690&sr=8-2")

cookieButton = browser.find_element(By.XPATH, '//*[@id="sp-cc-accept"]')
buyButton = browser.find_element(By.XPATH, '//*[@id="buy-now-button"]')

cookieButton.click()
buyButton.click()

emailField = browser.find_element(By.XPATH, '//*[@id="ap_email"]')
emailField.send_keys(cell_obj.value + Keys.ENTER)

for i in range(2, m_row + 1):
    browser.switch_to.new_window('tab')
    browser.get(
        "https://www.amazon.de/ring-video-doorbell-wired/dp/B08LR3G17D/ref=sr_1_2?keywords=ring&qid=1652445690&sr=8-2")
    buyButton2 = browser.find_element(By.XPATH, '//*[@id="buy-now-button"]')
    buyButton2.click()
    emailField = browser.find_element(By.XPATH, '//*[@id="ap_email"]')
    emailObject = sheet_obj.cell(row=i + 1, column=1)
    emailField.send_keys(emailObject.value + Keys.ENTER)
