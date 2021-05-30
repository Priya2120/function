# Ek function banaiye jo 3 numbers ka sum aur average print 
# kare.Hum user se 3 number input karwayenge aur fir unn 3 
# numbers ka sum aur average print karwayenge jaisa ki niche output diya hua hain.


def sum_average(a,b,c):
    sum=a+b+c
    avg=sum/3
    print("sum",sum)
    print("avg",avg)
num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
num3=int(input("enter the number :"))
sum_average(num1,num2,num3)
