import random

# 2 <= n <= 200,000
# 1 <= R_t <= 1000000000

# 最大数を入力とした時のテストデータを生成

N = 200000
R = 1000000000

random.seed(0)

test_list = [random.randint(1, R) for i in range(N)]

print(N)
for i in test_list:
    print(i)
