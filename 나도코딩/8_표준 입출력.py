print("Python", "Java")
print("Python", "Java", sep=", ")

import sys
print("Python", "Java", file =sys.stdout) #표준출력

scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
#딕셔너리를 사용할 때, items 사용하면 키와 밸류 값울 튜플로 보내줌
for subject, score in scores.items():
    # print(subject, score)
    #과목은 8칸 확보 왼쪽 정렬, 점수는 4칸 확보 오른쪽 정렬
    print(subject.ljust(8),str(score).rjust(4), sep =":")

#은행 대기 순번표
#빈 공간 영으로 채우기 zfill

for num in range(1,21) :
    print("대기번호 : ", str(num).zfill(3))