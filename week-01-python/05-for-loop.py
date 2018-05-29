#컴퓨터가 제일 잘하는 반복!
# for(~동안), range
# while(~동안)
#num = number

# # for 반복을 표현한다. range와는 땔 수 없는 사이.
for num in range(1, 10): # cf. 10이 화면에 표시 되지 않는 이뉴는 slice를 참고 하자 [1, 2, 3][0:2]
    print(num)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in num_list:
    print(num)

# while
while True: # 무한루프
    print(1)

a = 1
while a < 10:
    print(a)
    a = a + 1
