# 입력 처리 n=5
n, m = map(int, input().split())
l = list(map(int, input().split()))
# 알고리즘! #인덱스 0 1 2 3 4
c = 0  # 가장 가까운수
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if l[i]+l[j]+l[k] <= m:
                c = max(c, l[i]+l[j]+l[k])
print(c)
