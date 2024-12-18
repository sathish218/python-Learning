a = 10
b = 20
if(a+b>10):
    print("yes this in added content")
else:
    print("This is not added not avialable")


    
# Inbuild method 

name = "Sathish"
lastname="kumar"
print(name.upper()) #Upper 
print(name.lower()) #Lower
print(name.title()) #Title 
print(name+" "+lastname) 

#escape sequence
   
print("hello \n world" )  #\n
print("Hello \t world")   #\t

#Length

message = "Sathish Karuvachi 218"
print(len(message))  #21

fullName = "Sathishkaruvachi 218"
print(fullName.find("s")) #(find)  #Index value
print(fullName.count("s"))  #(Count) "s"-count
print(fullName.replace("218","23"))  #(replace) 218 - 23
print(fullName.isalpha()) #(Is alpha) false all are alphates
print(fullName*10)

################
#variables - interprete

firstname,lastname,age = "Sathish","Karuvachi",20
print(age)


# Data type - str,int,float,boolean

otp = "1234567"
print("your number is "+str(otp))
print(int(otp)+8)
print(int(float(otp))+2)

# Excercise

char="Sathish"
days=15
year=2024
print(f"Dear {char}, \n you have {days} of leave balance for this \n year({year})")

# Input types 

firstname = input("What is your name:")
print("I am"+firstname)
height = float(input("What is your heigth: ")) 
height_inches = "{:.2f}".format(height/2.54)
print(type(height))
print("My heigth is: "+str(height_inches))

# Math - Module

import math 
a = 4.56
print(math.ceil(a))
print(math.floor(a)) 
print(math.factorial(math.ceil(a))) 

#Boolean logic

password = True

if password:
    print("The pass word is correct")
else:
    print("Incorrect password")

num = int(input("Enter the number: ")) 
if num < 20:
    print(str(num) + " This number is lesser than 20")
else:
    print(str(num) + " This number is greater than or equal to 20")



# Bitwise opertors

# Slice 

name = "Sathish"
x = slice(2,-2)
print(name[x])


# Python  dictionaryes

#Python dictionay

Bike = {
    "BikeName":"Mt 15",
    "Brand":"Yamaha",
    "Lanch Year":"2022",
    "Users":"Youngsters"
}
print(Bike)
x = Bike["BikeName"]
print(x)




#Join Function (Keys)

student_details = {
    "Name":"SathishKumar",
    "DOB":"15-05-2004",
    "ROle":"FullStackDeveloper",
    "Company Name":"FreshWorks"
}
x = student_details.keys()
student_details["Village"] = ["Tiruvanamalai"]
print(x)







    












