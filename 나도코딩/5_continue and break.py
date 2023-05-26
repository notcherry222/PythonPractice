absent = [2, 5] #결석한 학생
noBook = [7]
for student in range(1,11):
    if student in absent :
        continue
    elif student in noBook :
        print("수업 안 해")
        break
    print("{}, 책 읽어봐".format(student))