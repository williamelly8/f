l = []  # 빈 리스트이지만 2차 배열이 될 것
for i in range(9):
    t = list(map(int, input().split()))
    l.append(t)
# 인덱스로 순회한다.
m = 0  # 최댓값
행 = 0
열 = 0
for i in range(9):
    for j in range(9):
        if m < l[i][j]:
            # 새로운 최댓값!
            m = l[i][j]
            행 = i
            열 = j
print(m)
print(행+1, 열+1)
