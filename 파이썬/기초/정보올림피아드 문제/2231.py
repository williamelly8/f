n = int(input())

ans = 0
for i in range(1, n):
    if i + sum(map(int, str(i))) == n:
        ans = i
        break
print(ans)
