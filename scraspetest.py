import requests

res = requests.get("http://pythonscraping.com/pages/page1.html")
print(res.text)      # 문자열 (decode 이미 된 상태)