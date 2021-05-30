# Question 5
# check_numbers naam ka ek function likhiye jo do numbers 
# le aur fir print kare "Dono even hain" agar dono numbers 
# even (2 se divide hote hain) nahi toh print kare "Dono numbers even nahi hai"

def check_numbers(num,num1):
    if num%2==0 and num1%2==0:
        print("Two number is even")
    else:
        print("Two number is not even")
check_numbers(12,2)