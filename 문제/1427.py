# 방법 1
s = input()
l = list(s)
l.sort(reverse=True)
print(*l, sep="")

# 방법 2
# print(*sorted(input(),reverse=True),sep="")
