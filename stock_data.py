from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

global stock_name, id, password

print("Enter email-id: ")
id = input()

print("Enter Password: ")
password = input()

print("Enter stock symbol: ")
stock_name = input()

path = "C:\\Users\\Jarvis\\PycharmProjects\\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://www.screener.in/login/?")

#driver.find_element_by_xpath("//body/nav//div[@class='layer-holder top-navigation']/div/div[3]//a[@href='/login/?']").click()   #login button of homepage
driver.find_element_by_xpath("/html//input[@id='id_username']").send_keys(id)   # email id
driver.find_element_by_xpath("/html//input[@id='id_password']").send_keys(password)     #password

driver.find_element_by_xpath("/html/body//form[@action='/login/']/button[@type='submit']").click()   # click login

stock_input = driver.find_element_by_css_selector("div#desktop-search  .u-full-width")
stock_input.send_keys(stock_name)
stock_input.send_keys(Keys.RETURN)

driver.find_element_by_css_selector("div#top  .flex > button").click()     #click download button




