a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a == b == c:
    "계산하세요"

elif a == b or a == c:
    "계산하세요.. 같은눈 찾기가 어려워.."

else:
    print(max(a, b, c)*100)
