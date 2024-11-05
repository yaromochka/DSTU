n, t = map(int, input().split())
a = [int(i) for i in input().split()]
id = int(input())

for x in range(n - 1):
    ans = float('inf')
    h = a[x]
    ok = True
    dist = 0
    for y in range(x, n - 1):
        if id == y and dist > t:
            ok = False
            break
        if y != x:
            dist += a[y] - a[y - 1]
    for y in range(n - 2, -1, -1):
        dist += a[y + 1] - a[y]
        if id == y and dist > t and id < x:
            ok = False
            break
    if ok: ans = min(ans, dist)

    ok = True
    dist = 0
    for y in range(x - 1, -1, -1):
        if id == y and dist > t:
            ok = False
            break
        if y != x: dist += a[y + 1] - a[y]
    for y in range(n - 1):
        dist += a[y] - a[y - 1]
        if id == y and dist > t and id > x:
            ok = False
            break
    if ok: ans = min(ans, dist)
print(ans)