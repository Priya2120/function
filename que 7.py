# Q5. Aapko min function ka use krke di hue list me se sbse chhoti value print krvani hai.
# list = [8, 6, 4, 8, 4, 50, 2, 7] 
# def var_function(list):
#     print(min(list))
# var_function(list)

def smaller(list):
    b=list[0]
    i=0
    while i<len(list):
        if list[i]<b:
            b=list[i]
        i=i+1
    print(b)
priya = [8, 6, 4, 8, 4, 50, 2, 7]
smaller(priya)