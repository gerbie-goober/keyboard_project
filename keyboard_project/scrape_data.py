import requests
from bs4 import BeautifulSoup

result = requests.get("https://geekhack.org/index.php?board=31.0")
src = result.content

soup = BeautifulSoup(src, 'html.parser')
links = soup.find_all("a")
for link in links:
    if "keyboard" in link.text:
        print(link)
        print(link.attrs['href'])

