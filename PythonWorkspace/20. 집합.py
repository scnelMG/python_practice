# 집합(set)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"오병민", "오혜린", "오삼록"}
python = set({"오병민", "이우주"})

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 못하는 개발자)
print(java - python)
print(java.difference(python))

# python 할 수 있는 사람 늘어남
python.add("이미애")
print(python)

# java를 잊음
java.remove("오삼록")
print(java)