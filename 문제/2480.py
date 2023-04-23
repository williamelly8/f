a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a == b == c:  # 모든눈이 같으면 기본 10000원 + 같은 눈 * 1000원
    "계산하세요"
# 2개의 눈만 같다. 1000원 + 같은 눈 * 100원
elif a == b or a == c:
    "계산하세요.. 같은눈 찾기가 어려워.."

# 모든 눈이 다르다. 가장 큰 눈 * 100원
else:
    print(max(a, b, c)*100)
