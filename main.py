from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import load_workbook
from selenium.webdriver.common.keys import Keys

wb = load_workbook(r"C:\users\Leo\Desktop\Mappe1.xlsx")
sheet_obj = wb.active
m_row = sheet_obj.max_row
browser = webdriver.Firefox()

for i in range(2, m_row + 1):
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
    browser.get("https://www.amazon.de/ring-video-doorbell-wired/dp/B08LR3G17D/ref=sr_1_2?keywords=ring&qid=1652445690&sr=8-2")
    cookieButton = browser.find_element(By.XPATH, '//*[@id="sp-cc-accept"]')
    buyButton = browser.find_element(By.XPATH, '//*[@id="buy-now-button"]')
    cookieButton.click()
    buyButton.click()
    browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 'w')



    email_obj = sheet_obj.cell(row=i, column=1)
    password_obj = sheet_obj.cell(row=i, column=2)









