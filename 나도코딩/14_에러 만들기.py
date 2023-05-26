#raise
# class BigNumError(ValueError)
# def __init__(self, msg):
# self.msg = msg
# def __str__(self):
# return self.msg
try :
    print("한 자리수 계산기 입니다.")
    num1 = int(input("first num :"))
    num2 = int(input("second num :"))
    if num1 >=10 or num2 >=10 :
        raise ValueError
    print("{0}/{1}={2}".format(num1, num2, int(num1/num2)))

except ZeroDivisionError as err:
    print("Only one"+err)

finally: print("Thankyou") #무조건 실행되는.