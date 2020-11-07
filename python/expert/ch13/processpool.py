from multiprocessing import Pool
import time


import requests

URLs = (
    "https://amazon.co.jp",
    "https://paypaymall.yahoo.co.jp/",
    "https://www.rakuten.co.jp/",
    "https://shopping.yahoo.co.jp/",
    "https://p-bandai.jp/",
    "https://www.apple.com",
    "https://youtube.com/",
    "https://atcoder.jp/",
)


def fetch(url):
    r = requests.get(url)
    return "{} : {}".format(url, r.status_code)


POOL_SIZE = 4


def present_result(result):
    print(result)


def main():
    with Pool(POOL_SIZE) as pool:
        results = pool.map(fetch, URLs)
    for result in results:
        present_result(result)


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print("time elapsed: {:.2f}s".format(elapsed))
