"""tt=((1,2,3),
    (4,5,6),
    (7,8,9))

for i in tt :
    print('')
    for k in i:
        print(k, end =' ')"""

"""myTuple = (10,20,30)
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
print(myTuple)"""
"""a=set('acfjieliowof')
b=set('dfiohwoefwoi')

print(a-b) # 차집합
print(a|b) # 합집합
print(a&b) # 교집합
print(a^b) # 여집합"""
 
"""dic1={'수' : 2000, '이름' : '홍길동', '학과' : '파이썬학과'}
print(dic1)
print(dic1.keys())
print(list(dic1.keys()))
print(dic1.values())
print(list(dic1.values()))"""

"""singer={}

singer['이름'] = '트와이스'
singer['구성원 수'] = '9'
singer['데뷔'] = '서바이벌 식스틴'
singer['대표곡'] = 'SIGNAL'

for i in singer.keys() :
    print("%s --> %s"%((i),(singer[i])))"""

"""dic1={'one':'하나', 'two':'둘', 'three':'셋', 'four':'넷'}

enWord=input('단어를 입력하세요 : ')
if enWord in dic1.keys() :
    print(dic1[enWord])
else :
    print("없는 단어 입니다.")"""

"""menu={
    'Americano' : 3000, 'Ice Americano' : 3500, 'Cappuccino' : 4000, 'Caffe Latte' : 4500, 'Espresso' : 3600
}

for i in menu.keys() :
    print("%s %d"%(i,menu[i]))

choice = input("위의 메뉴 중 하나를 선택하세요 : ")
print("%s는 %d입니다. 결재를 부탁합니다."%(choice,menu[choice]))
"""

"""pro_list = [('Python',7), ('Java',2)]
print(pro_list)
pro_dict = dict(pro_list)
print(type(pro_dict))
print(pro_dict)"""

'''list1 = [1,2,2,4,4,3]
print(list1)
print("중복제거")
list1 = set(list1)
print(list1)'''

"""list1 = [1,2,2,4,4,3]
list2 = []
for i in list1 :
    if i not in list2 :
        list2.append(i)
    else :
        pass
print(list2)
"""
"""langs = 'python', 'Java', 'C++'
for index in range(len(langs)):
	print(index,langs[index])"""
"""
A = ['blue', 'yellow', 'red']
B = ['red','green', 'blue']
new_pairs =[(a,b) for a in A for b in B if a != b]
print(new_pairs)"""
"""a = {x for x in 'abaracadabra' if x not in 'abc'}

kor_foods = ['kimchi', 'bibimbab', 'tteok-bokki']
kor_foods_enum = enumerate(kor_foods)

for index, food in kor_foods_enum :
	print(index, food)
"""

"""evens = [even*2 for even in range(10) ]
print(evens)"""

"""
A=[1,2,3]
B=[2,3,4]

pairs = []
for a in A :
    for b in B:
        if a!= b:
            pairs.append((a,b))

pairs=[(a,b) for a in A for b in B if a != b]
print (pairs)"""

"""triple_dic = {x:x**3 for x in (2,3,4)}
print(triple_dic)"""

"""
print('지금부터 달리기 시합을 시작하겠습니다.')
nums = int(input("달리기 선수가 몇 명인가요? :"))
dic_name={}
for names in range(nums):
    name=input('지금 들어온 선수 이름을 입력하세요 : ')
    dic_name[names]=name
print('달리기 시합 결과 !!')
for i in dic_name.keys() :
    print('%s 등 %s'%(i+1,dic_name[i]))"""

"""a_list = [44,66,34,24,144,98,38,568,234,345]
A_list = [x for x in a_list if x%12 == 0]
print(A_list)"""

"""b_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
B_list = [x for x in b_list if x>0 == True x=(x//1)]
print(B_list) # 컴프리헨션 왜 안될까?

b_list = [-22.3, 29.44, 902.2, 45.7, -887.1, -56.3]
B_list = []

for x in b_list :
    if x > 0 :
        x=x//1
        B_list.append(x)
    else :
        pass

print(B_list)
"""

"""ss = '파이썬짱!'

sslen = len(ss)
for i in range(0,sslen):
    print(ss[i]+'$', end='')"""

"""str1 = input('문자열을 입력하세요 : ')
len1 = len(str1)
for i in range(len1) :
    print(str1[(len1-i-1)], end='')"""

"""ss = input("날짜(연/월/일) 입력 ==> ")

ssList = ss.split('/')

print("입력한 날짜의 10년 후 ==> ", end = '')
print(str((int(ssList[0]) + 10)) +"년", end='')
print(ssList[1] + "월", end='')
print(ssList[2] + "일")"""