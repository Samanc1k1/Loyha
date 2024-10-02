matn = input("Gapni kiriting: ")

sozalr = matn.split()

natija_sozlar = []
for soz in sozalr:
    if len(soz) % 2 == 1:
        natija_sozlar.append(soz[::-1])
    else:
        natija_sozlar.append(soz)

natija = ' '.join(natija_sozlar)

print(natija)
