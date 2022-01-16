# import sys
# print("python", "Java", file=sys.stdout)
# print("python", "Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #subject는 왼쪽 정렬 후 8칸, score는 오른쪽 정렬 후 4칸


#은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호:" +str(num).zfill(3))

answer = input("아무 값이나 입력하세요 :") #받을땐 항상 문자열 형태로
print(type(answer))
print("입력하신 값은 "+ answer + "입니다.")