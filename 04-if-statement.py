# 참과 거짓 boolean
# if
# True, False
# and, or, not

# a = True
# b = False
# # A가 참이고 그리고 B가 참이라면 (A와 B가 둘다 참이여야 된다)
# print(a and b)
# # A가 참이거나 혹은 B가 참이라면 (A나 B 둘 중에 하나라도 참이면 된다)
# print(a or b)
#
# # # = & ==
# # a = true a라는 값에 true를 넣어준다는 의미
# # a == ture a 와 true가 동일하냐 라는 뜻 equal의 의미
# c = True
# print(a == True)
# print(a is True)

# if (<= 작거나 같다의 순서가 헛갈리면 입으로 해보면 된다.  )

d = int(input("숫자를 입력해주세요."))

if d > 10:
    print("숫자는 10보다 큽니다.")
elif d > 5 and d <= 10: #구간을 나누고 싶을 때, 예외사항으로 조건을 넣고 싶을때
    print("숫자는 10보다 작거나 같고, 5보다는 큽니다.")
else: # else는 조건을 넣지 못한다.
    print("숫자는 5보다 작거나 같습니다.")
