list =  [1, 2, 33, 5, 6, 7, 7]
son = int(input("Sonni kiriting: "))

for i in range(len(list)):
    for j in range(1,len(list)):
        if list[i]+list[j]==son:
            print(i,j)
