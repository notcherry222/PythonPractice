def profile(name, age, main_lang):
    print("이름 : {0}\t나이:{1}\t주 사용 언어 : {2}".format(name,age,main_lang)) #\t = tab


profile("유재석",20,"파이썬")

#같은 학년 반 수업인 경우?->기본값
def profile1(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이:{1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile1("유재석")

#전역 변수를 지역 변수로 사용하기
#방법1_비추
gun = 10 #전역 변수

def checkpoint(soldier) :
    global gun #전역에 있는 건 사용
    gun = gun-soldier
    print("남은 총 : {0}".format(gun))

checkpoint(2)


#방법2

def checkpoint_return(gun, soldier) :
    gun = gun-soldier
    print("남은 총 : {0}".format(gun))
    return gun

checkpoint_return(gun, 2)

#성별에 따른 표준체중 공식을 통해 출력하라
# 조건 : 표준 체중은 별도 함수 내에서 계산.
# 표준 체중은 소수점 둘재자리까지 표시

def std_weight(gender, high) :
    if gender == "female":
        return high*high*21
    else :
        return high*high*22
#
# high = 175
# gender = "male"

gender = input("성별을 입력하세요 : ")
high = int(input("키를 입력하세요 : "))
weight = round(std_weight(gender,high/100),2)
print("키 {0}인 {1}의 표준 체중은 {2}이다.".format(high, gender, weight))


