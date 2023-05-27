#조건 1: 1보다 작거나 숫자가 아닌 값이 들어오면 valueerror
# 출력 메시지 : 잘못된 값을 입력하셨습니다.
# 조건2 : 대기손님이 주문할 수 있는 치킨량은 총 10마리.
# 치킨 소진 시 사용자정의에러 soldoutError 발생하고
# 프로그램 종료 메시지 출력 : 재고소진

class soldOutError(Exception):
     pass

chicken = 10
waiting = 1

while(True) :

    try :
        print("남은 치킨 : {0}".format(chicken))
        order = int(input("how many? "))
        if order > chicken :
            print("cannot cook")
        elif order<=0 :
            raise ValueError
        else :
            print("{0}손님, {1}마리 주문완료".format(waiting, chicken))
            chicken-=order
            waiting+=1
        if chicken == 0 :
            raise soldOutError
    except ValueError :
        print("wrong")
    except soldOutError :
        print("재료 소진")
        break
