#삼각수로 표현될 수 있는 숫자 : 1
# 아닌 것은 0 출력
# 입력되는 자연수는 3<= N <=1000

t = [n*(n+1)/2 for n in range(46)]
def isPossible(number) :
    for i in range(1,46):
        for j in range(i,46) :
            for k in range(j, 46) :
                if t[i]+t[j]+t[k] == number:
                    return 1
    return 0

for i in range(int(input())) :
    print(isPossible(int(input())))