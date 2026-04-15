# Varisble = a resable container for a value (String, integer, flote, boolean)
#            The Variable behave as if it was the value that it contain

s = "Bro"
i = 22
cgpa = 7.98
student = True
rain = False
sun = False

print(f"Hey {s}")
print(f"Your Age is {i}")
print(f"Your cgpa is {cgpa}")
print(f"Are you a student? : {student}")

if rain == True and sun == True:
    print(f"It's Sunny And Rainy")
elif rain == True and sun == False:
    print(f"It's Rainy But not Sunny")
elif rain == False and sun == True:
    print(f"It's Not rainy but Sunny")
else:
    print(f"It's not rainy or sunny")

if rain == True and sun == True:
    print(f"Don't Go!!")
elif rain == False and sun == True or rain == True and sun == False:
    print(f"Might Go!!")
elif rain == False and sun == False:
    print(f"Let's Go!!")