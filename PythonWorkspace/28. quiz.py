# Quiz) 당신은 Kakao 서비스를 이용하는 택시 기사이다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1: 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해진다.
# 조건2: 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 한다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# ...
# [ ] 50번째 손님 (소요시간: 16분)

# 총 탑승 승객: 2분

from random import *
tnum = 0
for i in range(1,51):
    time = randrange(5,51)
    if time <= 15:
        #print("[O]" +str(i)+ "번쨰 손님 (소요시간:" + str(time)+"분)")
        print("[O]{}번째 손님 (소요시간: {}분".format(i, time))
        tnum +=1
    else:
        #print("[ ]" +str(i)+ "번쨰 손님 (소요시간:" + str(time)+"분)")
        print("[ ]{}번째 손님 (소요시간: {}분".format(i, time))

#print("총 탑승 승객:"+str(tnum)+"분")
print("총 탑승 승객:{}분".format(tnum))