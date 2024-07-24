import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
link = "https://hh.ru/search/vacancy?text=python+Django+flask&area=1&area=2"
vacations = []
try:
    response = requests.get(link, headers=headers)
except:
    print(f'Ошибка при запросе {response.status_code}')

html_data = response.text
soup = BeautifulSoup(html_data, features='lxml')
tags = soup.find_all("div", class_=
"vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter")

for item in tags:
    href_tag = item.find("a", class_="bloko-link")
    href = href_tag['href']

    vacation_name_tag = item.find("span",
                                  class_="vacancy-name--c1Lay3KouCl7XasYakLk "
                                         "serp-item__title-link")
    vacation_name = vacation_name_tag.text

    salary_tag = item.find("span",
                           class_="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni "
                                  "compensation-text--kTJ0_rp54B2vNeZ3CTt2 "
                                  "separate-line-on-xs--mtby5gO4J0ixtqzW38wh")
    salary = " ".join(salary_tag.text.split()) if salary_tag else 'Не указана'

    company_tag = item.find("span", class_="company-info-text--vgvZouLtf8jwBmaD1xgp")
    company = " ".join(company_tag.text.split()) if company_tag else "Не указана"

    citi_tag = item.find("div", class_="info-section--"
                                       "N695JG77kqwzxWAnSePt").find("span",
                                                                    class_="fake-magritte-primary-"
                                                                           "text--Hdw8FvkOzzOcoR4xXWni")
    city = citi_tag.text

    vacations.append({
        'title': vacation_name,
        'link': href,
        'salary': salary,
        'company': company,
        'city': city,
    })

with open('vacations.json', 'w', encoding='utf-8') as f:
    json.dump(vacations, f, ensure_ascii=False)
print(vacations)