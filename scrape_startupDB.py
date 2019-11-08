import requests
from bs4 import BeautifulSoup
import pandas as pd

nameList = []
addressList = []
urlList = []
employeeNubmerList = []
foundationDataList = []
fundingAmountList = []

for pageNumber in range(2):
    url = requests.get("https://startup-db.com/ja/companies?_x_headless=true&format=html&p=" + str(pageNumber))

    soup = BeautifulSoup(url.content, "html.parser")
    names = soup.findAll("h1", "p-corporate__name")

    for name in names:
        nameList.append(name.text)

df = pd.DataFrame(nameList,
  columns=['name'])

df.to_csv("companies.csv", encoding='utf_8_sig')
