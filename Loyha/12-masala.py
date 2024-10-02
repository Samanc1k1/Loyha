input_tuple = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

ozgargan_tuple = [t[:-1] + (100,) for t in input_tuple]

print(ozgargan_tuple)
