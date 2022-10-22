from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

driver = webdriver.Chrome() # You will be required to setup a chrome driver.

driver.get('https://uk.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=rocket')

try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "spin-results-wrap"))
    ) # You need to wait for the webpage to render the domains (its an asynchronous web request made).
except TimeoutException:
    raise

html = driver.page_source

soup = BeautifulSoup(html, "html.parser") # Also note I use the html.parser instead of lxml.

domain = soup.find_all('span', class_="domain-name-text h4 text-bold")

print(domain)
