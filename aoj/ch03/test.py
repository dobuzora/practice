#!/usr/bin/env python

import sys

# 1 <= N <= 100
# 0 <= A <= 1000

N = 10000

def create_rev_numbers():
    print(N)
    for i in range(1,N):
        print(i, end=" ")
    print(N)

def create_numbers():
    print(N)
    for i in range(N,1,-1):
        print(i, end=" ")
    print(1)

def main():
    args = sys.argv
    if len(args) == 2 and args[1] == "-r":
        create_numbers()
    else :
        create_rev_numbers()

if __name__ == '__main__': main()

