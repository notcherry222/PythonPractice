for i in range(0, int(input("입력할 데이터 수를 적으세요. "))) :
    stk = []
    ans = "YES"
    for c in input("데이터를 적으세요. "):
        #c에서 (를 stk에 삽입
        if c == '(':
            stk.append(c)

        else:
            if len(stk)>0:
                stk.pop()
            else: ans = 'NO'

    if len(stk)>0 :
        ans= 'NO'
    print(ans)


