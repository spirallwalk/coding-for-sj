#절대로 외울필요는 없고, 모르면 찾아보면 된다. 자주 쓰면 외워진다.
#목록 list, tuple
#사전 dict - dictionary
#집합 set
#type() = 파이썬 내장 명령어. 어떤 형태인지 파이썬의 이름에 맞게 알려준다.

# list []
print("list")
list_a = [1, 2, 3]
print(list_a)
print(type([1, 2, 3]))
# index는 0부터 시작합니다. [1, 2, 3] 이라고 했을때 1 = 0번째, 2 = 1번째 3 = 2번쨰.
print(list_a[0])
print(list_a[1])
print(list_a[2])

#slice [?:?] = list를 짜른다는 의미인데 마지막 인덱스는 포함하지 않는다. [0:2]이라면 0부터 2까지인데 2는 포함하지 않는다. 그래서 1,2만 화면에 표시된다.
print(list_a[0:2])

#a.append = append는 추가한다는 의미 (5)라고 하면 list_a 는 (1, 2, 3)인데 새로운 5가 추가된다.
list_a.append(5)
print(list_a)

# #remove(?) = append가 추가라면 remove는 제거
list_a.remove(2)
print(list_a)
#
# #clear = list의 모든 항목을 지운다. 화면에 아무것도 표시되지 않는다.
list_a.clear()
print(list_a)


#tuple (1, )
print("tuple")
tuple_a = (1, 2, 3)
print(tuple_a)
print(type(tuple_a))
#tuple은 한 번 생성 후 내부 값 변경 불가
# tuple_a.append(4) tuple은 변경이 되지 않는다. 즉 더하기 뺴기가 안 된다. 그럼 왜 수정이 안되는 걸 만들었나?
# 수정을 하지 말아야 즉 바뀌면 안되는 부분을 사용할때는 tuple을 사용하면 안전성을 보장해 줄 수 있다.

# dict (map) {}를 사용
# key & value ex) key = apple, value : a type of fruit
dict_a = {
        "apple" : "a type of fruit",
        "pen"   : "a thing to write"
        }
print(dict_a)
print(dict_a["apple"])

# edit value 값을 변경 할 수 있다.
dict_a["pen"] = "something to take a pic"
print(dict_a)

#set set([]) 간단하게 생각하면 집합 (다른 수업에는 없을 만큼 거의 사용되지 않는다.)
set_a = set([1, 2, 3, 3 , 3 , 2]) #<- 자동으로 중복 제거
set_b = set([2, 4, 6])
print(set_a)
print(set_b)

# 집합 - 교집합(&), 합집합(|), 차집합(-), 여집합 <거의 사용할 일은 없
# 중복 제거(set 중에 기억해야 할 부분)
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
