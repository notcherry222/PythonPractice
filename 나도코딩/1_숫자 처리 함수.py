print(abs(-5)) #절댓값
print(pow(4,2)) #4^2
print(max(5,12)) #큰값
print(min(5,12)) #작은값
print(round(3.14)) # 반올림

from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱근

from random import * #랜덤함수
print(random()) # 0.0~1.0미만의 랜덤 값
print(int(random()*10)) #0~10미만의 정수값(int로 소수자리 제거)
randrange(1,46) # 1이상 46미만
randint(4,45) #1이상 45이하

#월 4회 스터디. 3회는 온라인 1회는 대면.
# 랜덤으로 날짜를 뽑는다. 최소 일수는 28. 매월 1~3일은 스터디 준비로 제외.
# 출력문 예제 : 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 ",str(date),"일로 선정되었습니다.") #str