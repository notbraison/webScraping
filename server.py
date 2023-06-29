# This is a webscraper whose main  aim is to collect data of all football players names and ages 
#in all champions league matches across time
#and get the average age

from selenium import webdriver#import the webdriver

url ='https://www.transfermarkt.co.uk/kaka/profil/spieler/3366'

browser=webdriver.Chrome()
#at this point i had to find my version of chrome and download a driver for it and put it inside this project folder because i will create a path for it later
browser.find_element("xpath",'//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div/div[1]/div/a').click()
