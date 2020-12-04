print("http://", "www.", "google.", "com")
# Python yukarıdaki kodu aslında şöyle algılar:
#  print("http://", "www.", "google.", "com", sep=" ")

print("http://", "www.", "istihza.", "com", sep="")
print("T", "C", sep=".")
print("Adana", "Mersin", sep="-")
print("bir", "iki", "üç", "dört", "on dört", sep="mumdur")
print("bir", "iki", "üç", "dört", "on dört mumdur", sep=" mumdur, ")


print('a', 'b', sep='')
x =10
y=20
print(x, y, sep='')
print(x, y, sep="")

print("birinci satır\nikinci satır\nüçüncü satır")

print("birinci satır", "ikinci satır", "üçüncü satır", sep="\n")

print("Bugün günlerden Salı")
# Python yukarıdaki kodu aslında şöyle algılar:
# print("Bugün günlerden Salı", end="\n")

print("Bugün günlerden Salı", end=".")
print(" Ayni satira devam ediyoruz", end=".\n")
print("Yeni satir")


print("bir", "iki", "üç", "dört", "on dört", sep=" mumdur ", end=" mumdur\n")
