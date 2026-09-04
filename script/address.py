import requests


def fetch(url):
    """주소를 받아 응답 객체를 돌려준다. 실패하면 예외 발생."""
    res = requests.get(url)
    res.raise_for_status()
    return res