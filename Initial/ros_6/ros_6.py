import mdtraj

with open('input.txt', 'r') as file:
    content = file.read()

word_dict = {}
words = content.split()
for word in words:
    if word not in word_dict.keys():
        word_dict[word] = 1
    else:
        word_dict[word] += 1
word_dict

with open('output.txt', 'w') as file:
    for key, value in word_dict.items():
        file.write(f'{key} {value}\n')

print(word_dict)

