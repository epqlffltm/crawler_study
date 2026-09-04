import requests
from bs4 import BeautifulSoup


def main():
    res = requests.get(
        "http://www.pythonscraping.com/pages/page3.html"
    )

    bs = BeautifulSoup(res.text, "html.parser")

    for child in bs.find("table", {"id": "giftList"}).children:
        print(child)


if __name__ == "__main__":
    main()