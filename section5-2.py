# 접근 지정
# http://ehpub.co.kr/30-python%EC%97%90%EC%84%9C%EC%9D%98-%EC%BA%A1%EC%8A%90%ED%99%94-%EC%A0%95%EB%B3%B4-%EC%9D%80%EB%8B%89%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%A0%91%EA%B7%BC-%EC%A7%80%EC%A0%95/

class Unit:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100

    def GetHP(self):
        return self.__hp

    def GetName(self):
        return self.__name

    def __SetHP(self, hp):
        if (hp < 0):
            hp = 0
        if (hp > 100):
            hp = 100
        self.__hp = hp

    def Play(self, hour):
        print(hour, "시간 운동하다.")
        self.__SetHP(self.__hp + hour)

    def Drink(self, cups):
        print(cups, "잔 마시다.")
        self.__SetHP(self.__hp - cups)


unit = Unit("홍길동")
print("유닛 이름:{0} 체력:{1}".format(unit.GetName(), unit.GetHP()))
unit.Drink(3)
print("유닛 이름:{0} 체력:{1}".format(unit.GetName(), unit.GetHP()))
unit.Play(5)
print("유닛 이름:{0} 체력:{1}".format(unit.GetName(), unit.GetHP()))
