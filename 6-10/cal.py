import math_unit as mu
# print(mu.s(12,15))

# from math_unit import a
# print(a(13,17))

# print(mu.a(15,30))

y=input("Write What you want\n Add=a\n sub=s\n mul=m\n div=d\n integer div=id\n remainder=r\n")
p=int(input("Enter 2 Num you want to Cal:\n"))
q=int(input())

if y=="a":
    print(mu.a(p,q))

elif y=="s":
    print(mu.s(p,q))

elif y=="m":
    print(mu.m(p,q))

elif y=="d":
    print(mu.d(p,q))

elif y=="id":
    print(mu.id(p,q))

elif y=="r":
    print(mu.r(p,q))
