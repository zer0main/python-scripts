l = list(map(int, input().split()))
for i in range(0, len(l) - 1):
    while l[i] > l[i + 1] and i >= 0:
        g = l[i]
        l[i] = l[i + 1]
        l[i + 1] = g
        i -= 1
print(l)
