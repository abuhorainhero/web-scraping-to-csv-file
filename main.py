from bs4 import BeautifulSoup
from selenium import webdriver
from csv import writer
import re

url = "https://www.pararius.com/apartments/amsterdam?ac=1"
browser = webdriver.Chrome("./chromedriver.exe")

browser.get(url)
soup = BeautifulSoup(browser.page_source, "html.parser")
lists = soup.find_all('section', class_="listing-search-item")

with open('file.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_="listing-search-item__link--title").text.strip()
        location = list.find('div', class_="listing-search-item__location").text.strip()
        price = list.find('div', class_="listing-search-item__price").text.strip()
        price = re.sub('[€]', "Euro", price)
        area = list.find('li', class_="illustrated-features__item illustrated-features__item--surface-area").text.strip()

        info = [title, location, price, area]
        thewriter.writerow(info)


browser.close()










#
# url = "https://www.pararius.com/apartments/amsterdam?ac=1"
# page = requests.get(url)
#
# soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find_all("body"))


