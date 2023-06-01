def weeklyPay(rate,hour) :
    global pay
    if hour > 30 : 
        pay = rate*30 + rate*(hour-30)*1.5
        return pay
    else :
        pay=rate*hour
        return pay

pay = 0
rate=int(input("시급 : "))
hour=int(input("근무시간 : "))

weeklyPay(rate,hour)

print("주급은 %d입니다"%(pay))
