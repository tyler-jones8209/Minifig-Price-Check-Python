from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

identifier = sys.argv[1]
price_label = sys.argv[2]
condition = sys.argv[3]
period = sys.argv[4]

if len(sys.argv) != 5:
    print("Usage: python script.py <lego_id> <price_label> <condition> <time_period>")
    sys.exit(1)

url = f"https://www.bricklink.com/v2/catalog/catalogitem.page?M={identifier}#T=P"
driver.get(url)

time.sleep(.5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

def retrieve_price(soup, identifier, price_label, condition, period):

    tables = soup.find_all('table', class_='pcipgSummaryTable')
    table = None
    
    if period.lower() == "last_6":
        if condition.lower() == "new":
            table = tables[0]
        elif condition.lower() == "used":
            table = tables[1]
    elif period.lower() == "current":
        if condition.lower() == "new":
            table = tables[2]
        elif condition.lower() == "used":
            table = tables[3]
    else:
        raise ValueError("Please choose between 'current' or 'last_6'")

    if table is None:
        raise ValueError("Table is None")

    price = None
    rows = table.find('tbody').find_all('tr')
    price_label_map = {"min": 2, "avg": 3, "max": 5} 
    
    try:
        price_cell = rows[price_label_map[price_label]].find_all('td')[1]
        price = price_cell.text.strip().split('$')[1]
    except (IndexError, KeyError, AttributeError, ValueError):
        raise ValueError("Could not extract price. Page structure may have changed")

    price = f"{float(price):.2f}"

    if price is None:
        raise ValueError("Price is None")

    name = soup.find('h1', id='item-name-title')
    name = name.text

    if period.lower() == "current":
      print(f"{price_label.capitalize()} price of a {condition.capitalize()} {name} ({identifier}) minifig during {period} time period: ${price}")
    else:
      print(f"{price_label.capitalize()} price of a {condition.capitalize()} {name} ({identifier}) minifig during the last 6 months: ${price}")
    
retrieve_price(soup, identifier, price_label, condition, period)

driver.quit()
