#입력 처리
n = int(input()) # 1이다
# 생성자 없는 경우 0출력
# 1부터 n까지 모두 시도해본다.
ans = 0
for i in range(1, n):
    # i와 i의 각 자리수를 더한다
    # 이게 n과 같은지 비교한다.
    # n과 같으면 성공!
    if i + sum(map(int, str(i))) == n:
        ans = i
        break
print(ans)
