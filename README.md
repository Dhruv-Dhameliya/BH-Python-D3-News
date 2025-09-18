# 📰 Web Scraper for News Headlines

A simple **Python web scraper** that extracts **top news headlines** from a chosen news website using `requests` and `BeautifulSoup`.  
The headlines are saved into a `.txt` file and also printed in the terminal.  

---

## 🔧 Tools & Libraries
- **Python 3**
- **requests** → Fetches HTML content from the web
- **BeautifulSoup (bs4)** → Parses HTML and extracts headlines

---

## ✨ Features
- Fetches live HTML content from a news website URL.
- Parses the HTML to find all `<h2>` tags, which typically contain main headlines.
- Extracts and cleans the text from these tags.
- Ensures that only unique headlines are collected.
- Saves the list of numbered headlines to headlines.txt.
- Prints the content of the file to the console after a successful scrape.
