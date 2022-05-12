from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Firefox()
browser.get("https://www.amazon.de/DualSense-Wireless-Controller-Cosmic-PlayStation/dp/B094WRT8PD/ref=pd_sim_sccl_1_3/260-5777354-5953213?pd_rd_w=3ez3l&pf_rd_p=96527118-ae73-4a18-939d-14eb43bee5ae&pf_rd_r=P9AS1Q9ZY85CP5N24FBD&pd_rd_r=fa82c0f1-a036-4d86-8332-c2e00d6b71cd&pd_rd_wg=yDghL&pd_rd_i=B094WRT8PD&th=1")
cookieButton = browser.find_element_by_xpath('//*[@id="sp-cc-accept"]')

buyButton = browser.find_element_by_xpath('//*[@id="buy-now-button"]')
cookieButton.click()
buyButton.click()



