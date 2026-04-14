# f = open("example.txt","r")
# cont = f.read()
# print(cont)
# f.close()

# f = open("example.txt","r")
# print(f.read())
# f.close()

# f = open("example.txt","w")
# f.write("Hello Zeel\n")
# f.write("python\n")
# f.write("Learn Python\n")
# f.close()

# f = open("example.txt","a")
# f.write("Add New line\n")
# f.close()

# with open("example.txt","r") as file:
#     c=file.read()
#     print(c)
#using with close it as defauly

# open("file.txt","x")

# open("image.png","rb")

# with open("image.png", "rb") as f:
#     data=f.read()
#     print(len(data))

# with open("example.txt","r") as file:
    # for l in file:
    #     print(l.strip())
    # f=list(file)
    # print(f)
# [give each line one by one when reading large data]
#.strip use for removing space otherit will give default /n
# Hello Zeel
# python
# Learn Python
# Add New line

# import csv
# with open ("data.csv","r") as file:
#     r = csv.reader(file)
#     for row in r:
#         print(row)