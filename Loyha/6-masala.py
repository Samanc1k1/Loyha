n = int(input("Sonni kiriting: "))

yigindi = 0
natija = []

for i in range(1, n+1):
    yigindi += i
    if i == 1:
        natija.append(f"1={yigindi}")
    else:
        sonlar = '+'.join(str(x) for x in range(1, i+1))
        natija.append(f"{sonlar}={yigindi}")

for list in natija:
    print(list)
