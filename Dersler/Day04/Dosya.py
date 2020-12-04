# eğer istersek print() fonksiyonunun, çıktılarını ekrana değil,
# bir dosyaya yazdırmasını da sağlayabiliriz. sağlayalım.

dosya = open("deneme.txt", "w")
print("Ben Python, Monty Python!", file=dosya)
dosya.close()


# 1. deneme.txt adlı bir dosya oluşturduk ve bu dosyayı dosya adlı bir değişkene atadık.
# 2. open methodunun 2. parametresi "w" = open in write mode

# Yeni dosyanin hangi folderda oldugunu ogrenmek icin:
import os
os.getcwd()

print("python")
# Python bu komutu şöyle algılar:
# print("python", sep=" ", end="\n", file=sys.stdout)