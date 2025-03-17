n = int(input())
s = [0] + [0 if x == 'G' else 1 for x in input()]
e = [0] + list(map(int, input().split()))

l = [-1, -1]  # 第一次出现的位置  
r = [-1, -1]  # 最后一次出现的位置  

for i in range(1, n + 1):
    x = s[i]
    if x == 0 and l[0] == -1:
        l[0] = i
    elif x == 1 and l[1] == -1:
        l[1] = i
    if l[0] != -1 and l[1] != -1:
        break

for i in range(n, 0, -1):
    x = s[i]
    if x == 0 and r[0] == -1:
        r[0] = i
    elif x == 1 and r[1] == -1:
        r[1] = i
    if r[0] != -1 and r[1] != -1:
        break

ans = k=kk=0
for i in range(1, n + 1):
    if s[i] == 0:
        if i<=l[1] and e[i]>=l[1] and e[l[1]]>=r[1]:
            ans+=1
            if i==l[0]:
                k=1
    if s[i]==1:
        if i<=l[0] and e[i]>=l[0] and e[l[0]]>=r[0]:
            ans+=1
            if i==l[1]:
                kk=1
if e[l[0]]>=r[0] and e[l[1]]>=r[1] and k==0 and kk==0:
    ans+=1
print(ans)