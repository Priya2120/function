#  Debug the Code .
# Ab hum function se related code ko debug karenge. Question 1

# def sum():
#     print(12+13)
# sum() 

# def welcome():
#     print("Welcome to function")
# welcome() 


# def Even():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number") 
# Even()

# def info(name, age="16" ):
#     print(name + " is " + age + " years old")

# info("Sonu","16")
# info("Sana", "17")
# info("Umesh", "18") 


# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
# studentDetails("Nilam","loop","sapana") 

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list)) 

# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = "134"
# name = "Rinki"
# add_numbers(num_x, name)

# def greet(*names):
#     for name in names:
#         print("Welcome", name)


# greet("Rinki", "Vishal", "Kartik", "Bijender") 

# def f1():
#     s = "I Love Navgurukul"
#     print(s)
# f1()

# def first_function():
#     s = 'I love India'
#     def second_function():
#         print(s)     
#     second_function()
# first_function() 

# def first_function():
#     s = 'I love India'
#     def second_function():
#         s = "MY NAME IS JACK"
#         print(s)     
#     second_function()
#     print(s)    
# first_function()
 
# def calculate_sum(a,b):
#     sum = a+b
#     print(sum)
# calculate_sum(4,5)


# def multiply(a,b):
#     c=a*b
#     print("mutiply",c)
# multiply(12,4)

# def avg(number1,number2,number3):
#     sum=number1+number2+number3
#     avg=number1+number2+number3/3
#     print("sum",sum)
#     print("avg",avg)
# avg(1,3,2)
 
# def voter(age):
#         if age > 18:
#             print("eligible")
#         else:
#             print("not eligible")
# voter(20)
 

def distance(kms):
        if kms < 20:
            print("close")
        elif kms < 50:
            print("median")
        else:
            Print("far")
distance(20)
distance(30) 