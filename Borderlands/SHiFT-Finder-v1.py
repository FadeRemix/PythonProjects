import requests
import re
import os
from bs4 import BeautifulSoup

file_name = "previous_code.txt"

URL = "https://mentalmars.com/game-news/borderlands-3-golden-keys/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
name_results = soup.find('strong')
#expires_results = soup.find("td")
code_results = soup.find('code')
ExpireDate = soup.find(string=re.compile("Expires:"))

#print(f"Reward: {name_results.string}")
#print(f"Code: {code_results.string}")
#print(ExpireDate)


if os.path.exists(file_name):
    with open("previous_code.txt", "r") as file:
        data = file.read()
    if code_results.string == data:
        print("No new codes found :(")
        input("\nPress Enter to exit...")
    else:
        print(f"Reward: {name_results.string}")
        print(f"Code: {code_results.string}")
        print(ExpireDate)
        input("\nPress Enter to exit...")
    
else:
    with open("previous_code.txt", "w") as file:
        file.write(code_results.string)
    print("!! NEW CODE !!\n")
    print(f"Reward: {name_results.string}")
    print(f"Code: {code_results.string}")
    print(ExpireDate)
    input("\nPress Enter to exit...")
