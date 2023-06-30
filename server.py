# This is a webscraper whose main  aim is to collect data of all football players names and ages 
#in all champions league matches across time
#and get the average age

from selenium import webdriver #import the webdriver
from selenium.webdriver.common.by import By

url ='https://en.wikipedia.org/wiki/List_of_European_Cup_and_UEFA_Champions_League_finals'

browser = webdriver.Chrome()
#at this point i had to find my version of chrome and download a driver for it and put it inside this project folder because i will create a path for it later
browser.get(url)
element=browser.find_element(By.CLASS_NAME,"mw-page-title-main")
print(element)


