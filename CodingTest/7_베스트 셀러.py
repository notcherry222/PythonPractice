#가장 많이 팔린 책 출력하기
# 첫째줄에 오늘 팔린 책 권 수가 주어짐
# 책 제목의 길이는 50보다 작거나 같고 소문자로 이루어짐
# 만약 가장 많이 팔린 책이 여러 개일 경우 사전 순으로 앞서는 제목 출력

books = dict() #책 이름이 문자열이기 때문에 맵 사용

for i in range(int(input())) :
    name = input()
    if name in books :
        books[name] += 1
    else :
        books[name] = 1
max_value = max(books.values())
arr = []
for k, v in books.items(): #키값으로 책 제목을 ,밸류값을 등장 횟수
    if v == max_value :
        arr.append(k)

arr.sort() #오름차순 정렬
print(arr[0])

