# while
customer = "토르"
index = 5
while index >= 1:
    print("{}, 커피가 준비 되었습니다. {}번 남았습니다.". format(customer, index))
    index -=1
    if index == 0:
        print("커피는 폐기했습니다.")


# customer = "아이언맨"
# index = 1
# while True:
#     print("{}, 커피가 준비 되었습니다. 총 {}번 호출 했습니다.".format(customer,  index))
#     index += 1

customer = "토르"
person = "unknown"

while person != customer:
    print("{}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")