input_tuple = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

natija = sorted(input_tuple, key=lambda x: float(x[1]), reverse=True)

print(natija)
