# IN        : returns true if a value found
# NOT IN    : returns true if a value not found

fruits = ["grapes", "berries"]
my_fruits = ["grapes", "berries"]
fav_fruits = fruits

print("berries" in fruits)      # TRUE
print("apples" not in fruits)   # TRUE

print(fav_fruits in fruits)     # False
print(my_fruits in fruits)      # False

print (fav_fruits is fruits)    # True