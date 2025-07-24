
a = 1
b = 40

with open('input.txt', 'r') as file:
    content = file.readlines()

for n in range(a,b,2):
    print(content[n].strip())