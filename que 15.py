# Ab ek check_numbers_list naam ka ek function 
# likho jo inetgers ki list ko arguments ki tarah 
# le aur fir check kare ki same index waale dono 
# integers even hain ya nahi. Yeh check karne ke l
# iye pichle Part 1 mein likhe check_numbers function 
# ka use karo. Agar aapne apne function ko [2, 6, 18, 10, 3, 75] 
# aur [6, 19, 24, 12, 3, 87] Toh usko yeh output deni chaiye:

def check_numbers(num1,num2):
    i=0
    while i<len(num1):
        if num1[i]%2==0 and num2[i]%2!=0:
            print(num1[i],num2[i],"Two number is even")
        else:
            print(num1[i],num2[i],"Two number is not even")
        i=i+1
check_numbers([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])