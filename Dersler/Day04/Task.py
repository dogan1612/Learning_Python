# 1-) abc değişkenine İngilizce alfabenin küçük haflerinden oluşan listeyi atayınız.
# 2-) myList'in son string değerinin harflerinin abc'deki indislerinin toplamını bulunuz.
# 3-) myList'te Python'ca, İngilizce ya da Türkçe doğruların ve yanlışların sayısını bulunuz.
# 4-) myList'teki tüm doğrular yanlışlardan fazla ise
# 	a-) Kesirli sayıların toplamı tam sayıların toplamından büyük ise listedeki son kesirli sayının ilk tam sayıya bölümünü bulunuz.
# 	b-) Tam sayıların toplamı kesirli sayıların toplamından büyük ise, en küçük tam sayı ile en büyük kesirli sayının çarpımını bulunuz.
# 5-) myList'teki yüm yanlışlar doğrulardan fazla ise
# 	a-) Tam sayıların toplamı kesirli sayıların toplamından büyük ise ilk kesirli sayının ilk tam sayıya bölümünü bulunuz.
# 	b-) Kesirli sayıların toplamı tam sayıların toplamından büyük ise, en küçük kesirli sayı ile en büyük tam sayının çarpımını bulunuz.
# 6-) Bir de, ikinci alt listedeki sayıların toplamını ilk alt listedeki sayıların toplamına bölebilir misiniz? (edited)

#1)
import string
abc = list(string.ascii_lowercase)
print (f'Görev1: {abc}')

# ​2)
myList = ["merhaba", "elma", "yanlış", 123, 7.89, 88.99, 99.88, ["patates", False, "true", "karınca", 95, 8.5, "floransa", 85, "cimbom", True], "armut", "doğru", "portakal", True, "false", "Albania", "kartal", False, "doğru", "sosyal mesafe", 33, 66, 99, 6.6, 333.333, "güneş", [1, "doğru", False, "yanlış", True], "true", 98.01, True]

a = []
for x in reversed (myList):
    if type (x) == str:
        for i in x:
            for harf in abc:
                if i == harf:
                    a.append(abc.index(harf))
        break
print (f'Görev2: {sum(a)}')

# for i in myList:
#     if type(i)==str:
#         son_str=i
# dongudeki atanan son deger degiskende kaldigi icin en son string degiskende kalmis oluyor.


#3)
dogru_yanlis_sayisi = 0

for i in myList:
    if ((type (i) == bool) and (i==True or i==False)) or (str (i) == 'true' or str (i) =='false' or str (i) == 'doğru' or str (i) == 'yanlış'):
        dogru_yanlis_sayisi += 1
    elif type (i) == list:
        for a in i:
            if ((type (a) == bool) and (a==True or a == False)) or (str (a) == 'true' or str (a) =='false' or str (a) == 'doğru' or str (a) == 'yanlış'):
                dogru_yanlis_sayisi += 1
print (f'Görev3: {dogru_yanlis_sayisi}')

#4)
dogrular = 0
yanlislar = 0
for i in myList:
    if ((type (i) == bool) and (i==True)) or (str (i) == 'true' or str (i) == 'doğru'):
        dogrular += 1
    if (type (i) == bool and i==False) or (str (i) == 'false' or str (i) == 'yanlış'):
        yanlislar += 1
    if type (i) == list:
        for a in i:
            if ((type (a) == bool) and (a==True)) or (str (a) == 'true' or str (a) == 'doğru'):
                dogrular += 1
            if ((type (a) == bool) and (a==False)) or (str (a) == 'false' or str (a) == 'yanlış'):
                yanlislar += 1

kesirli_sayilar = []
tam_sayilar = []

if dogrular>yanlislar:
    for i in myList:
        if type (i) == float:
            kesirli_sayilar.append (i)
        if type (i) == int:
            tam_sayilar.append (i)
        if type (i) == list:
            for list_oge in i:
                if type (list_oge) == float:
                    kesirli_sayilar.append (list_oge)
                if type (list_oge) == int:
                    tam_sayilar.append (list_oge)
    if sum(kesirli_sayilar)>sum(tam_sayilar):
        for kesirli in reversed (myList):
            if type (kesirli) == float:
                for tam in myList:
                    if type (tam) ==int:
                        print (f'Görev4: {kesirli/tam}')
                        break
                break
    if sum(tam_sayilar)>sum(kesirli_sayilar):
        print (f'Görev4: {min (tam_sayilar)*max(kesirli_sayilar)}')
#5)
if yanlislar>dogrular:
    if sum(tam_sayilar)>sum(kesirli_sayilar):
        for ilk_kesirli in (myList):
            if type (ilk_kesirli) == float:
                for ilk_tam in myList:
                    if type (ilk_tam) ==int:
                        print (f'Görev5: {ilk_kesirli/ilk_tam}')
                        break
                break
    if sum(kesirli_sayilar)>sum(tam_sayilar):
        print (f'Görev5: {min (kesirli_sayilar)*max(tam_sayilar)}')
#6)
ikinci_alt_kume = []
birinci_alt_kume = []

for alt in myList:
    if type (alt) == list:
        for sayilar in alt:
            if type (sayilar) == float or type (sayilar) == int:
                birinci_alt_kume.append (sayilar)
        break
for alt2 in myList:
    if type (alt2) == list:
        a = myList.index(alt2)
        for alt3 in myList:
            if type (alt3) == list and myList.index(alt3)>a:
                for sayilar2 in alt3:
                    if type (sayilar2) == float or type (sayilar2) == int:
                        ikinci_alt_kume.append (sayilar2)
                break
        break
print(f'Görev6: {sum(ikinci_alt_kume)/sum(birinci_alt_kume)}')