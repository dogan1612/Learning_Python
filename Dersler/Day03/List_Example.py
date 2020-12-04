myList = [1, 2, 3, 5, 66, 888]
print(myList)
myList.insert(2, 6)
otherList = [1, 2, True, "Portakal"]
print(otherList)
print(otherList[1])
myList.append(otherList)
myList.append("yoğurt")
print(myList)
myList.remove(2)
print(myList)
# myList.remove("Portakal")        ERROR
last = myList.pop()            # Remove and return item at index (default last).
print (last)
print(myList)
print(myList.pop(2))
print(myList.pop(-1))           # Son element -1'dir
print(len(myList))
myList.clear()
myList.insert(2, 6)
myList.insert(0, 3)
myList.append(9)
myList.insert(1, 5)
print(myList)

