#Kalulator potęg#

a = float(input("Podaj podstawę potęgi:"))
n = int(input("Podaj wykładnik potęgi"))

def potega(a,n):
    if n>0:
        return potega(a,n-1)*a
    elif n<0:
        return potega(1/a, -n)
    else:
        return 1

print(pow(a,n))
