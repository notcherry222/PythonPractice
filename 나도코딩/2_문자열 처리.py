python = "Python is Amazing"

python.lower() #소문자
python.upper() #대문자
python.replace("Python", "Java") #자바로 변경

#요소 찾기
index = python.index("n") # 5출력
index = python.index("n", index+1) #15출력


python.find("n") #5, 15 출력
python.count("n") #2출력

type(python) #변수의 타입 알기