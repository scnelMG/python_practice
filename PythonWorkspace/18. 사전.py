# cabinet = {3:"오킹", 100:"오퀸"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5])
# print("hi") #실행안됨
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet) #True
# print(5 in cabinet) #False

cabinet = {"A-3":"오킹", "B-100":"오퀸"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "이우주"
cabinet["C=20"] = "오삼록"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

#key들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

#전부 삭제
cabinet.clear()
print(cabinet)