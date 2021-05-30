# Q1 . Aapko max function ka use krke di hue list me se sbse 
# bada value print krvani hai. Input
num = [3, 5, 7, 34, 2, 89, 2, 5] 
def MAX(num):
    i=0
    k=num[i]
    while i<len(num):
        b=num[i]
        if b>k:
            k=b
        i=i+1
    print(k)
MAX(num)

