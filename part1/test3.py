import requests


def cra(post_id):
    res = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    data = res.json()

    # "a" = 이어쓰기. 파일이 없으면 만들고, 있으면 끝에 붙임
    with open("result.txt", "a", encoding="utf-8") as f:
        f.write(f"[{post_id}] {data['title']}\n")
        f.write(data["body"] + "\n\n")

    print(post_id, res.status_code)  # 진행 상황만 터미널에


def main():
    for i in range(1, 10):
        cra(i)


if __name__ == "__main__":
    main()