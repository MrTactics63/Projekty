import math

a = input("Podaj parametr a:")
b = input("Podaj parametr b:")
c = input("Podaj parametr c:")

delta = int(b)**2 - 4*int(a) * int(c)
print("delta = ", delta)
if delta < 0:
    print("Funkcja nie ma miejsc zerowych")
elif delta == 0:
    print("Funkcja ma jedno miejsce zerowe")
    x0 = -int(b)/2*int(a)
    print(x0)
else:
    delta > 0 
    print("Funkcja ma dwa miejsca zerowe")
    pierwiastek_z_delty = math.sqrt(int(b)**2 - 4*int(a) * int(c))
    x1 = (-int(b) - math.sqrt(delta)) / (2* int(a))
    x2 = (-int(b) + math.sqrt(delta)) / (2* int(a))
    x1 = float
    x2 = float
    print(x1,x2)
