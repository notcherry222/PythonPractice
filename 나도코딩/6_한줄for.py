student = ["cherry", "melon", "apple"]
#
# #학생 이름 길이로 변환
studentlength = [len(i) for i in student]
#
# #학생 이름 대문자로 변환
students = [i.upper() for i in student]
print(students)

#50명의 승객과 기사가 매칭할 때 탑승 승객 수를 구하는 프로그램.
# 조건 : 승객별 운행 소요 시간은 5~50분. 5~15분 사이의 승객만 매칭가능
# 출력문 예제 :
# [0] 1번째 손님 (소요시간 : 15분)
# [] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 :5분)
# .....
# 총 탑승 승객 : 2분

from random import *

cnt = 0 #총 탑승객

for i in range(1,51) :
    time = randrange(0, 51)
    if 5<= time <= 15 :
        print("[o] {0}번째 손님 (소요시간 : {1}분)".format(i,time) )
        cnt +=1
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
print("총 탑승 승객 : {0}".format(cnt))