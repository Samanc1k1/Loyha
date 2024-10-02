matn = input("Gapni kiriting: ")
gaplar = matn.split()

sort_gap = sorted(gaplar,key=lambda gap: gap.lower())

output = ' '.join(sort_gap)

print(output)
