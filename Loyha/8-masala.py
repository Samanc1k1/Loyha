n = int(input("N: ni kiriting: "))

binary_son = bin(n)[2:]
nollar = binary_son.count("0")

print(nollar)
