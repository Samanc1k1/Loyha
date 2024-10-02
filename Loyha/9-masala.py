def tubmi(son):
    if son < 2:
        return False
    for i in range(2, int(son**0.5) + 1):
        if son % i == 0:
            return False
    return True

n = int(input("Sonni kiriting: "))

tub_sonlar = []
keyingi_son = n+1

while len(tub_sonlar) < 5:
    if tubmi(keyingi_son):
        tub_sonlar.append(keyingi_son)
    keyingi_son += 1

print(' '.join(map(str, tub_sonlar)))
