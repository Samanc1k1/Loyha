n = int(input("n ni kiriting: "))

yigindi = 0

list = []

for i in range(1, n + 1):
    son = int('2' * i)
    yigindi += son
    list.append(str(son))

natija = '+'.join(list) + f'={yigindi}'
print(natija)
