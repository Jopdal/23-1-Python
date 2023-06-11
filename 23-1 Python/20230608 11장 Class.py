"""class Car :
    speed = 0
    def upSpeed(self, value) :
        self.speed += value

        print("현재 속도 ( 슈퍼 클래스 ) : %d "%self.speed)

class Sedan(Car) :
    def upSpeed(self, value) :
        self.speed += value

        if self.speed > 150 :
            self.speed = 150
        
        print("현재 속도 ( 서브 클래스 ) : %d"%self.speed)

class Truck(Car) :
    pass

sedan1, truck1 = None, None

truck1 = Truck()
sedan1 = Sedan()

print("트럭 --> ",end=" ")
truck1.upSpeed(200)

print("세단 --> ",end=" ")
sedan1.upSpeed(200)
"""


"""## 실습 1 ##
class Car :
    speed = 0
    def upSpeed(self, value) :
        self.speed += value

        print("현재 속도 ( 슈퍼 클래스 ) : %d "%self.speed)

class Sedan(Car) :
    def upSpeed(self, value) :
        self.speed += value

        if self.speed > 150 :
            self.speed = 150
        
        print("현재 속도 ( 서브 클래스 ) : %d"%self.speed)

class Truck(Car) :
    pass

class Sonata(Sedan) :
    pass

sedan1, truck1,sonata1 = None, None, None

truck1 = Truck()
sedan1 = Sedan()
sonata1 = Sonata()

print("트럭 --> ",end=" ")
truck1.upSpeed(200)

print("세단 --> ",end=" ")
sedan1.upSpeed(200)

print("세단 --> ",end=" ")
sedan1.upSpeed(200)"""

## 실습 2 [과제] ##

class Circle :
    def __init__ (self, radius) :
        self.radius = radius
    
    def area(self) :
        print("원의 넓이는 %0.1f"%((self.radius**2)*3.14))
    def round(self) :
        print("원의 둘레는 %0.1f"%(2*3.14*self.radius))

cir1 = None
print("원의 넓이와 둘레를 알려드립니다.")
r=int(input("반지름을 입력하세요: "))
cir1 = Circle(r)

cir1.area()
cir1.round()