# 2023 05 18
# 1번
"""
def hello():
    name=input("이름을 입력하세요 : ")
    print("안녕", name)

hello()
"""
# 2번
"""
def hello(name):
    print("안녕!", name)

my_name=input("이름을 입력하세요! ")
hello(my_name)
"""
# 3번
"""
def sum(a,b):
    print(a+b)

sum(6,4)
"""
# 4번
"""
def change_name(name):
    return print(name + "님")
change_name('지희')
"""
# 5번
"""
coffee=0

def coffee_machine(num):
    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다.");
    print("#2. (자동으로) 종이컵을 준비한다.");

    if num ==1:
        print("#3. (자동으로) 보통커피를 마신다.")
    elif num ==2:
        print("#3. (자동으로) 설탕커피를 마신다.")
    elif num ==3:
        print("#3. (자동으로) 블랙커피를 마신다.")
    else :
        print("#3. (자동으로) 아무거나 탄다. \n")

    print("#4. (자동으로) 물을 붓는다.");
    print("#5. (자동으로) 스푼으로 젓는다.");
    print()

coffee=int(input("어떤 커피를 드릴까요? (1. 보통 2. 설탕 3. 블랙)"))
coffee_machine(coffee)
print("커피가 나왔습니다.")
"""
# 실습 1
"""
def happyBirthday(name):
    print("사랑하는",name,"님의 생일을 축하합니다 ! ")
name=input("생일을 축하합니다 ! : ")
happyBirthday(name)
"""
# 실습 2
"""
def gugudan(a):
    for i in range(9):
        print(a,"*",(i+1),"=",(a*(i+1)))
b=int(input("정수를 입력하세요 : "))
gugudan(b)
"""
# 사칙연산 예제

def cal(a,b,c):
    result=0
    if b=='+':
        result=a+c
    elif b=='-':
        result=a-c
    elif b=='*':
        result=a*c
    elif b=='/':
        result=a/c
    elif b=='**':
        result=a**c
    return result

res=0
a,b,c=0,"",0

b=input("계산 부호를 입력하세요 [선택가능] (+,-,*,/,**) : ")
a,c=int(input("첫 번째 수를 입력하세요 : ")),int(input("두 번째 수를 입력하세요 : "))
if b=='/' and c==0 :
    print("~")
else:
    res=cal(a,b,c)
    print(res)


