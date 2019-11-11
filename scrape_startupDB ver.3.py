import requests
from bs4 import BeautifulSoup
import pandas as pd

companies = []

for pageNumber in range(1, 2):

    pageURL = requests.get("https://startup-db.com/ja/companies?_x_headless=true&format=html&p=" + str(pageNumber))
    soup1 = BeautifulSoup(pageURL.content, "html.parser")
    items = soup1.find_all("h1", "p-corporate__name")

    for item in items:
        company = ['-'] * 6

        linkURL = item.a.get('href')
        url = requests.get('https://startup-db.com' + linkURL)

        soup = BeautifulSoup(url.content, "html.parser")

        # scrape company name
        name = soup.find("h1", "p-name").text
        company[0] = name

        # scrape base information
        baseInfoClass = soup.find(class_="p-outline__baseInfo")
        baseInfos = baseInfoClass.find_all(class_='p-outline__col')
        for baseInfo in baseInfos:
            if baseInfo.find('dt', 'p-col__label').text == '住所':
                address = baseInfo.find('dd', 'p-col__body').text
                company[1] = address

            elif baseInfo.find('dt', 'p-col__label').text == '企業ホームページ・SNS':
                homepage = baseInfo.find('dd', 'p-col__body').text
                company[2] = homepage

            elif baseInfo.find('dt', 'p-col__label').text == '従業員数':
                employee = baseInfo.find('dd', 'p-col__body').text
                company[3] = employee

            elif baseInfo.find('dt', 'p-col__label').text == '設立年月':
                foundation = baseInfo.find('dd', 'p-col__body').text
                company[4] = foundation

        # Scrape Finance information
        finances = soup.find_all(class_="p-table__area")
        for finance in finances:
            if finance.find('th', 'u-text__left').text == '合計資金調達額':
                fundraising = finance.find('td', 'p-summary__number p-nowrap').text
                company[5] = fundraising

        companies.append(company)

df = pd.DataFrame(companies, columns=['name', 'address', 'URL', 'employee', 'foundation', 'Total Fundraising'])
df.to_csv("companies.csv", encoding='utf_8_sig')
