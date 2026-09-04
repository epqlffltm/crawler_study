import requests
from bs4 import BeautifulSoup

def main():
    url = "https://quotes.toscrape.com"

    res = requests.get(url)
    res.raise_for_status()
    
    soup = BeautifulSoup(res.text, "html.parser")
    
    for quote in soup.select("div.quote"):
        text = quote.select_one("span.text").get_text()
        author = quote.select_one("small.author").get_text()
        print(", ".join([text, author]))

if __name__ == "__main__":
    main()
