matn = ['salom',123,True,'Hayr','world',3.14,'7214']
text = []
other = []

for string in matn:
    if type(string) == str:
        text.append(string)
    else:
        other.append(string)

text.sort()
other.sort(reverse=True)

print(f"text listta {text}")
print(f"other listta {other}")
