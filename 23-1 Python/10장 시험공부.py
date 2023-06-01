def makedic(a,b) :
	aa={}
	aa[a]=b
	return aa
	

a1=input("키를 입력하세요 : ")
b1=input("값을 입력하세요 : ")
dic1=makedic(a1,b1)
print(dic1)