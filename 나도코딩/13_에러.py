# try-catch
try :
    nums = []
    nums.append(int(input("first number : ")))
    nums.append(int(input("second number : ")))
    nums.append(int(nums[0]/ nums[1]))
    print("{0}/{1}={2}".format(nums[0], nums[1],nums[2]))
except ValueError :
    print("잘못 입력했습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err : #모든 에러 처리
    print("I don't know exactly"+ err)