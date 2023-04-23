n = int(input())
# 중복을 제거하는
s = set()
for i in range(n):
    s.add(input())
# 중복 제거 완료
l = list(s)
# 정렬하는데... 1. 알파벳 순, 2. 길이 순
l.sort(key=lambda x: (len(x), x))
print(*l, sep='\n')
