# def a(x):
#     return(10/x)

# print("Enter A num:")
# y=a(int(input()))
# print(y)

# try:
#     num=int(input("Enter Number:"))
#     print(10/num)
# except ZeroDivisionError:
#     print("You Cann't Divide By Zero:")
# except ValueError:
#     print("Invalid Number try again:")


# while True:
#     try:
#         num=int(input("Enter Number:"))
        
#         if num==0:
#             print("Zeo not allowed.")
#             continue
#         print(10/num)
#         break

#     except ValueError:
#         print("Invalid Number try again:")
# print("Run Succesfuly")

# try:
#     f=open("example.txt")
#     print(f.read())
# except FileNotFoundError:
#     print("File Not Found")
# finally:
#     print("Program Finished")
    
# try:
#     y=int(input("Enter A number:"))
#     print(100/y)
# except ZeroDivisionError:
#     print("No 0's")
# except ValueError:
#     print("Invalid Num")
# finally:
#     print("Done")

with open("file.txt","w") as f:
    f.write("Hey!!\n")
    f.write("Sup!!")

try:
    f=open("file.txt","r")
    print(f.read())
except FileNotFoundError:
    print("No File Found")