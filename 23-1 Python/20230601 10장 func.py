"""
myList = [1,2,3,4,5]
def add10(num):
    return num + 10

for i in range(len(myList)) :
    myList[i] = add10(myList[i])

print(myList)
"""

"""
myList = [1,2,3,4,5]
add10=lambda num : num + 10
myList = list(map(add10, myList))
print(myList)
"""
"""
myList = [1,2,3,4,5]
myList = list(map(lambda num : num + 10, myList))
print(myList)
"""
"""
ist1 = [1,2,3,4]
list2 = [10,20,30,40]
hapList = list(map(lambda n1, n2 : n1 + n2, list1,list2))
print(hapList)
"""
"""
def count(num) :
     if num >= 1:
          print(num,end=" ")
          count(num-1)
     else :
          return
     
count(10)
print("")
count(20)"""

