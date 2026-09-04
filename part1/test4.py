from bs4 import BeautifulSoup

from script.address import fetch


def get_title(res):
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.title.get_text()


def main():
    res = fetch("https://quotes.toscrape.com")
    print(get_title(res))


if __name__ == "__main__":
    main()