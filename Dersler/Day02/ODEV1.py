s = int(input("Enter a digit (1~9): "))     # default olarak string kabul eder
ss = 10*s+s
sss = (100*s) + ss
print(s + ss +sss)



n = int(input("Bir sayi giriniz :"))
if((n <= 10)and(n >= 0)):
    print("n is between 0~10")
elif ((n <= 100) and (n > 10)):
    print("n is between 11~100")
elif ((n <= 1000) and (n > 100)):
    print("n is between 111~1000")
elif ((n <= 10000) and (n > 1000)):
    print("n is between 1001~10000")
else:
    print("n is bigger than 10.000")