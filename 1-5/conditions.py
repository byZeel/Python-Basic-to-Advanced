name=input("Enter Name ")

age=int(input("Enter your age: "))
if age>=18:
    print("Hello",name, "You are Adult")
elif age<18 and age> 10:
    print("Hello",name, "You are Teen")
else:
    print("Hello",name, "You are kid")
