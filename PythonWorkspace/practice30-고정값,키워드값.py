# def profile(name, age, main_lang):
#     print("이름: {}\t나이: {}\t주 사용 언어: {}"\
#         .format(name, age, main_lang))

# profile("오킹", 29, "파이썬")
# profile("오퀸", 27, "자바")

#같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age=17, main_lang="파이썬"):
    print("이름: {}\t나이 : {}\t주 사용 언어: {} ".format(name,age, main_lang)) 

profile("오병민")
profile("오혜린")

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")