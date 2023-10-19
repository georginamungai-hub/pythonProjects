import requests , re
import csv
from bs4 import BeautifulSoup

city = input("Enter City of Choice: ")
url = "https://www.businesslist.co.ke/companies/churches/city:${city}"
response = requests.get(url)

content = BeautifulSoup(response.content, 'html.parser')

headings = content.find_all("h4")
# for heading in headings:
#     print(heading.text)
allHeadings = headings.text.strip()


with open("ChurchInventory","w+") as ChurchList:
    writer = csv.writer(ChurchList)
    writer.writerow(['NAMES OF THE CHURCHES'])
    for heading in headings:
        writer.writerow([heading.text])

# Momburl = "https://www.businesslist.co.ke/companies/churches/city:mombasa"
# Mombresponse = requests.get(url)

# Mombcontent = BeautifulSoup(response.content, 'html.parser')

# print(content)

# Nakurl = "https://www.businesslist.co.ke/companies/churches/city:nakuru"
# Nakresponse = requests.get(url)

# Nakcontent = BeautifulSoup(response.content, 'html.parser')

# print(content)

# Eldurl = "https://www.businesslist.co.ke/companies/churches/city:eldoret"
# Eldresponse = requests.get(url)

# Eldcontent = BeautifulSoup(response.content, 'html.parser')

# print(content)

# Kisurl = "https://www.businesslist.co.ke/companies/churches/city:kisumu"
# Kisresponse = requests.get(url)

# Kiscontent = BeautifulSoup(response.content, 'html.parser')

# print(content)

