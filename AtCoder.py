# 整形：cmd + option + L
import numpy as np
import math
import itertools
from math import comb
import collections
from collections import Counter

# A=int(input())  # 1文字
# A,B=map(int,input().split())  # 1行に2文字
# A=list(map(int,input().split()))  # 1行に複数文字

# NxM行列
# N, M = map(int,input().split())
# a = [list(map(int, input().split())) for l in range(M)]
def main():
    M = 8
    S = [list(map(str,input().split())) for l in range(M)]

    for i, _ in enumerate(S):
        s=list(_[0])
        if "*" in s:
            print(chr(97+s.index("*"))+str(8-i))
            break
        else:
            continue





if __name__ == '__main__':
    main()

# nCr
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
