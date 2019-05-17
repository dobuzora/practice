import random

# n <= 10,000
# 0 <= S <= 1000000000
# q <= 500
# 0 <= t <= 1000000000

N = 10000
#S = 100000000
S = 10000
Q = 500
T = 10000
#T = 100000000

random.seed(0)

S_list = [str(random.randint(1, S)) for i in range(N)]
T_list = [str(random.randint(1, T)) for i in range(Q)]

print(N)
print(" ".join(sorted(S_list)))
print(Q)
print(" ".join(T_list))



