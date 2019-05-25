import random

# n <= 10,000
# 0 <= S <= 1000000000
# q <= 500
# 0 <= t <= 1000000000

N = 500000
S = 1000000000

random.seed(0)

S_list = [str(random.randint(0, S)) for i in range(N)]

print(N)
print(" ".join(S_list))



