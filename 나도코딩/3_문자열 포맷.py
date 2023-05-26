# print("A" + "B")
# print("A", "B")

print("나는 %d살입니다."%20)
print("나는 %s를 좋아해요" %"파이선")
print("apple은 %c와 %c가 들어가요"%("a", "e"))


print("나는 {}살 입니다.".format(20))
print("나는 {}살, {}살 입니다.".format("20","21"))

#사이트 별로 비밀번호를 만들어주는 프로그램
#1. http://와 처음 만나는 .이후 부분 제외.
# 남는 글자중 처음 세자리+글자 수+ 글자 내 'e'수+"!"로 구성

site = input("사이트를 입력하세요 : ")
my_site = site.replace("http://", "")
my_site = my_site[:my_site.index(".")]
passWord = my_site[: 3]+str(len(my_site))+str(site.count("e"))+"!"
print("{0}의 비밀번호는 {1}".format(site, passWord))
