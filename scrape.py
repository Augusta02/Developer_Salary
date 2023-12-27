import urllib
from urllib import request
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import re


# Opening the link using Webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://quotes.toscrape.com')

# Navigating to the next page 
click_count = 0 

while click_count < 11:
    try:
        next_page_button = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//li[@class="next"]/a')))

        #  click on the next button
        next_page_button.click()

        #  wait for the page to load
        # WebDriverWait(driver, 360).until(EC.url_changes(driver.current_url))
        # print current_url
        urls = driver.current_url
        print(f'Current Page Url: {urls}')

        # use Beautifulsoup to scrape data
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cards = soup.find_all('div', class_='quote')
        for card in cards:
            quotes = card.find('span', class_='text').get_text()
            print(quotes)


            # Identify the "Next" Button
        click_count += 1
    except:
        print('Next element not found')
        break

driver.quit()


    
    













