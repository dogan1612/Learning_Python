#bool ya da boolean veri tipleri True ya da False alabilir.

print(4 < 5) # True
print(4 == 5) # False
print(4 != 5) # True
print(4 <= 5) # True

b = 3 > 5
print(type(b))          # <class 'bool'>
print(b)                # false

string_false = "false"
print(type(string_false))
print(string_false)

print("-------------------------")
str1 = "a"
str2 = "a"
print(str1 == str2)     # true

# logical operators: and, or, not

# True and True -> True
# True and False -> False
# False and False -> False

# True or True -> True
# True or False -> True
# False or False -> False

print(((5 == 5) or (4==6)) or (4<1))        # true
print(not (4 == 4))     # false
print(8 > 5 or 8 == 5)  # true

print("-------------------------")
if (5 < 7 and (8 != 8)):
    print("Bu satır yazılmaz")
    print("Bu satır da yazılmaz")
print("Bu satır yazılır")

print("-------------------------")
if (5 < 7 and (8 == 8)):
    print("Bu satır da yazılır")
    pass
    print("Bu satır yazılmaz")

print("-------------------------")
deger1 = "hayat"
deger2 = "güzeldir"

if (5 < 6 or (3==3) and ((4==4) or (5 != 3))):
    print("İlk ifademiz doğru mu?")

    if (deger1 == deger2):
        print("Hayat güzeldir..")
    else:
        print("Hayat güzel değil mi?")
else:
    print("Maalesef")


# print("Burası hep yazdırılır! Hayat devam eder gider..") xxx
