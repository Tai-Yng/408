from collections import deque, defaultdict, Counter
from itertools import accumulate, permutations
from math import *
import sys

input = lambda: sys.stdin.readline().strip()

INF = 0x3F3F3F3F
# g = [[0] * (n + 1) for _ in range(n + 1)]
# dist = [0] * (n + 1)
# st = [False] * (n + 1)
# N=50010

t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    s = []
    # for i in range(n):
    #     s.append([h[i], a[i], t[i]])
    # s.sort(key=lambda x: (x[2]))
    rank=[-1]*(n)
    for i in range(n):
        rank[t[i]]=i
    flag = True
    ansL=0
    ansR=INF
    for i in range(n-1):
        # v=s[i+1][1]
        # u=s[i+1][0]
        # y=s[i][1]
        # x=s[i][0]
        x = h[rank[i]]
        y = a[rank[i]]
        u = h[rank[i + 1]]
        v = a[rank[i + 1]]
        if v == y:
            if x <= u:
                flag = False
                break
            else:
                continue
        if y > v:
            ansL=max(ansL,floor((u - x) // (y - v))+1)
        else:
            ansR=min(ansR,ceil((u - x) // (y - v))-1)
    if flag and ansL<=ansR:
        print(ansL)
    else:
        print(-1)
