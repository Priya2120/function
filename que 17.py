# Ek perfect() naam ka function define kijiye jo 
# ki ek parameter lega aur uss parameter ko hume check 
# karana hai ki vo perfect number hain ya nahi. 
# Iske baad uss function ko use karke ek program 
# likhiye jo ki 1 se 1000 tak sabhi perfect numbers 
# ko print kare.[ hum ek aise integer number ko perfect 
# number kahenge jo ki uske sabhi factors ( including 1 & excluding itself) 
# ka sum uss number ke barabar hota hai. Example:- Expected Output :-

def perfect(num):
    sum=0
    i=1
    while i<num:
        if num%i==0:
            print(i)
            sum=sum+i
        i=i+1
    if num==sum:
        print("it is perfect number")
    else:
        print("it is not perfect number")
perfect(int(input("enter the number")))
