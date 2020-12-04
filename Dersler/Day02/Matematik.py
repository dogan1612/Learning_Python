import math

pi_sayisi = math.pi
print(type(pi_sayisi))          # <class 'float'>
print(pi_sayisi)                # 3.141592653589793
str_pi = str(pi_sayisi)


baska_birsey = "bu da başka bir cümledir.."
print(baska_birsey[3:12])               # da başka


print(f"{pi_sayisi:.4f}")
print(f"{pi_sayisi:.5f}")
print("{:.5f}".format(pi_sayisi))
print(format(pi_sayisi, ".6f"))

# 3.1416
# 3.14159
# 3.14159
# 3.141593


