import os
from multiprocessing import Process

def work(identifier):
    print(
        'こんにちは、私はプロセス {}, pid {} です'
        ''.format(identifier, os.getpid())
    )


def main():
    processes = [
        Process(target=work, args=(number,))
        for number in range(5)
    ]

    for process in processes:
        process.start()

    while processes:
        processes.pop().join()


if __name__ == "__main__":
    main()
