import requests
from bs4 import BeautifulSoup
import re

response = requests.get( # 此處原本括弧前多一個空格
	"https://www.cdc.gov.tw/Category/NewsPage/EmXemht4IT-IRAPrAnyG9A")
soup = BeautifulSoup(response.text, "html.parser")

#print (soup.prettify())

# Find da table
the_table = soup.find("table", class_="m-b-20")

# Get da rows
all_rows = the_table.find_all('tr')

# 不要第一行，他只有 <th>=table headder and no <td> table cells
all_rows.pop(0)

for row in all_rows:
  link, date = row.find_all('td') # 每行有兩格
  link_match = re.match(r"^\s+([^\n]+)\s+$", link.find('a').text) # Regular expression妖術，抓取以下模式括弧內容：開頭多個連續空格 - (連續多個非換行字元) - 結尾多個連續空格
  link_href = link.find('a')['href'] # 抓連結
  print(date.text) # 印
  if link_match:
    print(link_match.group(1)) # 印印剛剛抓的括弧內容
    print(link_href) # 連結印印印