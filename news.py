import requests
from bs4 import BeautifulSoup

# URL = "https://www.bbc.com/news"
# URL = "https://www.livemint.com/news"
URL = "https://indianexpress.com/section/india/"

response = requests.get(URL)
response.raise_for_status() 

soup = BeautifulSoup(response.text, "html.parser")

headlines = []
for h2 in soup.find_all("h2"):
    text = h2.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for idx, headline in enumerate(headlines, 1):
        file.write(f"{idx}. {headline}\n")

print("✅ Headlines scraped and saved to headlines.txt\n")

with open("headlines.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)