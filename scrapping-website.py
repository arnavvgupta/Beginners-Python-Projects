from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

driver = webdriver.Safari() 

driver.get('https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=bjmtuc.club')

try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "spin-results-wrap"))
    ) 
except TimeoutException:
    raise

html = driver.page_source

soup = BeautifulSoup(html, "html.parser") 

domain = soup.find_all('span', class_="domain-name-text h4 text-bold")

print(domain)
