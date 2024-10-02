soz = input("Sozni kiriting: ")
harf = input("Harfni kiriting: ")

if harf in soz:
    natija = soz.replace(harf,harf.upper())
else:
    natija = soz
print(natija)
