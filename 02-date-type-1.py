#정수 int = integer
print(1 + 1)
#소수 float
print(1.5 + 2.1)
#문자 str = string
print("hello")

#문자열 더하기 "?"<-따움표 안에 넣어야 문자라고 인식한다.
# "hello" + 1 은 에러가 난다. 문자와 숫자는 더할 수 없기 때문이다.
print("hello" + "1")

# 정수 소수 간 변경 (//),(int) = 숫자를 정수로 표시 ,(/) 그리고 float()는 소수점 까지 표시
print(4 / 2)
print(4 // 2)
print(int(4 / 2))
print(float(2))

#문자열 숫자 간 변경
print("1") #""을 사용했기 때문에 문자
print(int("1")) #int를 썼기때문에 숫자
print(int("1.5"))

#print(int(1.5)) <- 1.5를 정수로 표시하고나서 print 하라는 명령을 내렸을때 어떤 값이 나올까? 정답은 2번 오류가 난다.
# 1) 1이 나온다.
# 2) error
