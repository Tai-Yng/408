N = 100005
M = 200005

n, m = map(int, input().split())

h = [-1] * N
e = [0] * M
ne = [0] * M
idx = 0

color = [0] * N
flag = True


def add(u, v):
    global idx
    e[idx] = v
    ne[idx] = h[u]
    h[u] = idx
    idx += 1


def dfs(u, c):
    global flag
    color[u] = c
    i = h[u]
    while i != -1:
        v = e[i]
        if not color[v]:
            dfs(v, -c)
        elif color[v] == c:
            flag = False
        i = ne[i]


for i in range(m):
    u, v = map(int, input().split())
    add(u, v)
    add(v, u)

for i in range(1, n + 1):
    if not color[i]:
        dfs(i, 1)

if flag:
    print("Yes")
else:
    print("No")
