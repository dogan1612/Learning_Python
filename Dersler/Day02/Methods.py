print(type(12345))      # <class 'int'>
print(type("1234"))     # <class 'str'>

uzunluk = len("kubilay")
soyad = "Dogan"
print(len(soyad))       # 5
print(type(uzunluk))    # <class 'int'>

del soyad
# print(soyad)      # Error


# RULES
# 1. Değişken adları bir sayı ile başlayamaz.
# 2. Değişken adları aritmetik işleçlerle başlayamaz. +
# 3. Değişken adları ya bir alfabe harfiyle ya da _ işaretiyle başlamalıdır
# 4. Yasakli kelimelerle baslamamalidir

# To print out these words:
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del',
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# Kac kelime var?
print(len(keyword.kwlist))      # 35

yasaklı_kelimeler = keyword.kwlist
print(type(yasaklı_kelimeler))          # <class 'list'>'

# Listede olmasa da type ve len isimlerini vermeyin degiskenlere


