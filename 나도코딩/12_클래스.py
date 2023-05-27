class Unit :
    #이닛함수는 생성자
    #멤버변수 : name, hp
    def __init__(self, name, hp):
        self.name =name
        self.hp = hp
        print("{0}유닛이 생성되었습니다. 공격력 : {1}".format(self.name, self.hp))

#클래스로 부터 만들어지 객체. 마린은 유닛의 '인스턴스'라고 함
marine = Unit("마린", 40)

#유닛 클래스 상속받기 -> 유닛 클래스가 부모, 어택 유닛은 자식
class AttackUnit(Unit) :
    def __init__(self,name, hp, damaged):
        Unit.__init__(self, name, hp)
        self.damaged = damaged

    def attack(self, location):
        print("{0} : {1} 방향으로 공격. 공격력 : {2}" \
            .format(self.name, location, self.hp))  # 위치는 정해진 위치에서 함. 나의 위치 아님

    def damage(self, damaged):
        print("{0} : {1} 데미지 입음".format(self.name, damaged))
        self.hp -= damaged
        print("{0} : 현재 체력은 {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("유닛 파괴")

fireRobot = AttackUnit("firebot", 50,25)
fireRobot.attack("5시 방향")
fireRobot.damage(25)

#다중 상속
class fly :
    def __int__(self, speed):
        self.speed = speed

    def flyhigh(self, name, location):
        print("{0} : {1}방향으로 날아갑니다. 속도는{2}"\
              .format(self.name, location, self.speed))

class flyAttack(AttackUnit, fly) :
    def __int__(self, name, hp, speed ):
        AttackUnit.__init__(self, name, hp)
        fly.__int__(self, speed)


#부동산 프로그램
# 출력 예제 : 강남 아파트 매매 10억

class House:
    def __init__(self, location, house_type, deal_type, price):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price =price

    def show(self):
        print(self.location, self.house_type, self.deal_type, self.price)

houses = []
House1 = House("강남", "아파트", "매매", "10억")
House2 = House("마포", "오피스텔", "전세", "5억")
houses.append(House1)
houses.append(House2)

for house in houses :
    house.show()