# Minifig-Price-Check-Python
This is fun script I've created to scrape the price of a minifigure from BrickLink based on user given arguments. This is not meant to be used as a tool. It's mostly just practice in translating code between different languages. 

## Prerequisites
### Imports/Packages
``` python
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sys
```

## How to Use
The script takes 4 positional arguments: BrickLink item number (e.g., njo0047), price type (min, avg, max), condition (new, used), and period (current, last_6). Unfortunately, you do need to know the item number of the minifig. Or, you could just guess random IDs for fun. 

### Searching for a Price
Let's say I want to find the average used price of Jay ZX - Shoulder Armor (my all-time favorite minifig) over the last 6 months (one of BrickLink's categories for prices). This is the syntax I would use to find it:
``` bash
tdjones22@f0:~/scripts/python/brick_link$ python3 minifig_price_check.py njo0047 avg used last_6
Avg price of a Used Jay ZX - Shoulder Armor (njo0047) minifig during the last 6 months: $3.47
```

This works for all minifigure item numbers:
Using a Star Wars Minifig
``` bash
tdjones22@f0:~/scripts/python/brick_link$ python3 minifig_price_check.py sw0120 max new current
Max price of a New Anakin Skywalker - Black Right Hand (sw0120) minifig during current time period: $73.20
```

Using a DC Minifig
``` bash
tdjones22@f0:~/scripts/python/brick_link$ python3 minifig_price_check.py bat004 avg used current
Avg price of a Used Two-Face - Black Stripe Hips (bat004) minifig during current time period: $54.19
```

Using an LIJ Minifig
``` bash
tdjones22@f0:~/scripts/python/brick_link$ python3 minifig_price_check.py iaj024 avg used current
Avg price of a Used Indiana Jones - White Tuxedo Jacket (iaj024) minifig during current time period: $19.28
```

Anyway, you get the gist. If anything, this is just a sad reminder of how expensive Legos are ;(.
