

import requests
from bs4 import BeautifulSoup
import pyodbc


# categories

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                'Server=KBRYAN;'
                      'Database=scrappingJ;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

url = "https://www.jumia.ci/index/allcategories/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

categorie = soup.find_all("a", class_="-gy5 -hov-m -hov-gy8")

base = "https://www.jumia.ci/"
urls =[]
for category_name in categorie :
    # cursor.execute("INSERT INTO categorie (category_name) VALUES (?)", category_name.text)
    b = base + category_name.text
    urls.append(b)
# conn.commit()

count = 0
I = 0
for url in urls:
    while True:
     link = requests.get(url)
     soup1 = BeautifulSoup(link.content, "html.parser")
     produits = soup1.find_all('a',class_ = "core")
     nextpage = soup1.find('a',class_ = 'pg', attrs= {"aria-label":"page suivante"})
    
     

     for produit in produits:
            name = produit.get("data-name")
            categorie = produit.get("data-category")
            cursor.execute("INSERT INTO articles (articleName,articleCateg) VALUES (?,?)",name,categorie)
            conn.commit()
            count = +1
            if count >= 100:
             break
     if nextpage :
        url = base + nextpage.get("href")
     else:
        break

