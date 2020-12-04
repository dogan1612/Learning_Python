
for i in range(0, 10):
    print(i)
    if i == 5:
        break

print("-----------------------")

a = [1,3,6, -9,-11]

for x in a[:]:
    if x < 0: a.remove(x)

print (a)           #  [1, 3, 5]

print("-----------------------")

for i in range(0, 10):
    if i != 5: print(i)         # it will skip 5
    if i %2==0 : print(i)       # cift sayilari yazar

print("-----------------------")

myList = [1, 2, 3, 5, 66, 888]

for each in myList:             # each yerine istedigini yazabilirsin
    print(each)

else:
    print("-----------------------")
    print("bu her zaman çalışır?")
