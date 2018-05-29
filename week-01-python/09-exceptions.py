# exceptions = bug 예외가 났다. 예외처리를 한다.
#예외, 버그라는 것은 계발자를 괴롭히는 것이 아니라, 도와주는 것이다.

# ZeroDivisionErro -> 0으로 나누는 에러.
# 1 / 0
def divide_by(first, second):
    try:
        return first / second
    # except:
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."

# 4 / 2 = 0
print(divide_by(4, 2))
print(divide_by(4, 0))

# 예외 만들기
# Exception
class EvenNumberDevisionError(Exception): #class는 대문자로 연결 파이썬 커뮤니티에서 주로 사용(케멀케이스)
    pass

def divide_by_odd_number(first, second): #함수나 변수는 _언더바를 이용해서 연결
    if second % 2 == 0:
        raise EvenNumberDevisionError
    else:
        return first / second

print(divide_by_odd_number(6,3))
print(divide_by_odd_number(6,2))
