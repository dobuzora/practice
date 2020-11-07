import time
from threading import Lock


class Throttle:
    def __init__(self, rate):
        self._consume_lock = Lock()
        self.rate = rate
        self.tokens = 0.0
        self.last = 0

    def consume(self, amount=1):
        if amount > self.rate:
            raise ValueError("amount は rate 以下でなければならない")
        with self._consume_lock:
            while True:
                now = time.time()
                # 経過時間の初期化を最初のリクエスト時刻で行い、
                # 初期の大量リクエスト送信を防止
                if self.last == 0:
                    self.last = now
                # 経過時間に応じてトークンを不安
                elasped = now - self.last
                self.tokens += elasped + self.rate
                self.last = now
                # パケット溢れを防止
                if self.tokens > self.rate:
                    self.tokens = self.rate
                # トークンが利用可能なら消費して返す
                if self.tokens >= amount:
                    self.tokens -= amount
                    return amount
                # トークンがたまるまで待つ
                time.sleep((amount - self.tokens) / self.rate)


