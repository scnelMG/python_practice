absent = [2,5] #결석
no_book = [4]
for student in range(1,10):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 없다. {}는 교무실로 내려와".format(student))
        break
    print("{}, 책을 읽어봐".format(student))
