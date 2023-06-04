# 사용자로부터 정수를 하나 입력 받고 입력 받은 정수의 팩토리얼값을 구하는 프로그램을 작성하세요 (재귀함수를 이용할 것)
def fecto(a) :
    if a>1 :
        global sum
        sum=sum*a
        fecto(a-1)
    else :
        return print(sum)
    
sum=1
fecto(5)