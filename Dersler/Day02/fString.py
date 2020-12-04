# f string

isim = 'Buğra'
yas = 18
print(f'Onun adı {isim} ve o {yas} yaşında.')
print('Adiniz {1} ve yasiniz {0}.'.format(yas, isim ))

kisi={'name':isim,'age':yas}
print('Adiniz {name} ve yasiniz {age}.'.format(**kisi))




country = input("Your country: ")
city = input("Your city: ")
year = int(input("Birth year: "))
address = city +", " + country
person ={"country":country, "city":city, "year":year, "address": address}

print(f'You are from {address}')
print('You are from {address}'.format(**person))

