input_list = eval(input("Listni kiriting (masalan: [1,2,3,4]): "))
input_string = input("Stringni kiriting: ")

natija = [input_string + str(item) for item in input_list]

print(natija)
