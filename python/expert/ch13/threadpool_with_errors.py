import time
from queue import Queue, Empty
from threading import Thread

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


THREAD_POOL_SIZE = 4


def fetch(url):
    r = requests.get(url)
    return "{} : {}".format(url, r.status_code)


def present_result(result):
    print(result)


def worker(work_queue, results_queue):
    while True:
        try:
            item = work_queue.get(block=False)
        except Empty:
            break
        else:
            try:
                result = fetch(item)
            except Exception as err:
                results_queue.put(err)
            else:
                results_queue.put(result)
            finally:
                work_queue.task_done()


def main():
    work_queue = Queue()
    results_queue = Queue()
    for url in URLs:
        work_queue.put(url)
    threads = [
        Thread(target=worker, args=(work_queue, results_queue))
        for _ in range(THREAD_POOL_SIZE)
    ]
    for thread in threads:
        thread.start()
    work_queue.join()
    while threads:
        threads.pop().join()
    while not results_queue.empty():
        result = results_queue.get()
        if isinstance(result, Exception):
            raise result
        present_result(result)


if __name__ == "__main__":
    started = time.time()
    main()
    elapsed = time.time() - started
    print()
    print("time elapsed: {:.2f}s".format(elapsed))
