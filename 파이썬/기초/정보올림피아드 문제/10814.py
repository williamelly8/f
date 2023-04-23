n = int(input())
l = []

for i in range(n):
    age, name = input().split()
    age = int(age)  # 문자 나이를 숫자 나이로 교체
    l.append((age, i, name))  # 리스트에 튜플로 추가?????

l.sort()
for age, _, name in l:
    print(age, name)
