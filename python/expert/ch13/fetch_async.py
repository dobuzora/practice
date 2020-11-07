import time
import asyncio

from python.expert.ch13.asyncfetch import fetch, session

URLs = (
    "https://amazon.co.jp",
    "https://paypaymall.yahoo.co.jp/",
    "https://www.rakuten.co.jp/",
    "https://shopping.yahoo.co.jp/",
    "https://p-bandai.jp/",
    "https://www.apple.com",
    "https://youtube.com/",
    "https://atcoder.jp/"
)


async def fetch_url(url):
    r = await fetch(url)
    return "{} : {}".format(url, r)
    # return await fetch(url)


async def present_result(result):
    result = await result
    print(result)


async def main():
    await asyncio.wait([
        present_result(fetch_url(url))
        for url in URLs
    ])


if __name__ == "__main__":
    started = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # ClientSessionが閉じられていないとaiohttpが
    # 例外を送出するため、sessionを明示的に閉じる
    loop.run_until_complete(session.close())
    loop.close()
    elapsed = time.time() - started
    print()
    print("time elapsed: {:.2f}s".format(elapsed))
