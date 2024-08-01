from string import ascii_uppercase

text_file = open(r"C:\Users\arnav\OneDrive\Desktop\0022_names.txt", "r")

names = text_file.read().split(',')
names = [name.strip('"') for name in names]

names.sort()

def scores(word):
    return sum(ascii_uppercase.index(letter) + 1 for letter in word)

print(sum(i*scores(word) for i, word in enumerate(names, 1)))