# n, m = list(map(int, input().split()))
# a, b = [], []
# for i in range(n):
#     a.append(list(map(int, input().split())))

# for i in range(n):
#     b.append(list(map(int, input().split())))

# for i in range(n):
#     for j in range(m):
#         print(a[i][j]+b[i][j], end=" ")
#     print()

# 입력 데이터 예시
# 3 3
# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100

n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in a:
    b = list(map(int, input().split()))
    for x1,x2 in zip(i,b):
        print(x1+x2, end=" ")
    print()
