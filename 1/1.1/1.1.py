from Bio.Seq import Seq

with open("input.txt","r") as file:
    my_seq = file.read()

print(my_seq.count("A"))
print(my_seq.count("C"))
print(my_seq.count("G"))
print(my_seq.count("T"))