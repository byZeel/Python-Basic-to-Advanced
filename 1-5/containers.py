# List [] = mutable (append/remove), most flexible
# Tuple () = immutable, faster
# set {} = mutable (add/remove), unordered, No duplicates, best for membership testing

# fruits = ["apple", "orange", "banana", "coconut"]
fruits = {"apple", "orange", "banana", "coconut", "coconut", "coconut"}

#? for list
# for fruit in fruits:
#     print(fruit)
# apple
# orange
# banana
# coconut

#? for list
# fruits[0] = "mango"
# fruits.append("mango")
# fruits.remove("banana")
# fruits.pop(0)
# fruits.clear()

#! for set
# fruits.add("mango")
# fruits.remove("banana")
# fruits.pop()
# fruits.clear()

# for fruit in fruits:
    # print(fruit, end=" ")
# apple orange banana coconut

if "apple" in fruits:
    print("apple was found")
else:
    print("apple was not found")
