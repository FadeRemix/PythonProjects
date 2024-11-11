import requests
from bs4 import BeautifulSoup
from datetime import date
today = date.today()

URL = "https://mentalmars.com/game-news/borderlands-3-golden-keys/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

print(today.strftime("%B %d"))
print("")

name_results = soup.find("tbody")
for child in name_results.children:
    print(child.get_text(" | ",strip = True))
    
input("\nPress Enter to exit...")
