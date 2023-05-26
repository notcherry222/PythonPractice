import pickle
#피클에서는 따로 인코딩 안 해도됨
profile_file = open("profile.pickle", "wb")

#매주 1회 보고서 작성
# 보고서 양식 :
# - n주차 보고-
# 부서:
# 이름:
# 1주차부터 50주차까지 보고서 파일 만드는 프로그램 작성.
# 조건 : 파일명은 n주차.txt로 만들 것

for n in range(1, 51) :
    with open(str(n)+"주차.txt", "w", encoding = "utf8") as report_file :
        report_file.write("\n부서:")
        report_file.write("\n이름:")