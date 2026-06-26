import random as r
import json
import argparse

parser = argparse.ArgumentParser(
    prog="random key generator",
    description="Generates a random substitution cipher for CipherFont to use."
)

parser.add_argument("seed", type=int, nargs='?', default=12345, help="Seed value for random generator.")

args = parser.parse_args()

# Seed the random number generator
print(args.seed)
r.seed(args.seed)

# Start with the alphabet
alphabet = ["A", "B", "C", "D", "E",
            "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z"]

numbers = ["1", "2", "3", "4", "5",
           "6", "7", "8", "9", "0"]

# Randomly assign the code for letters
unselected = [l for l in alphabet]
selected = []

for i in range(len(alphabet)):
    letter = r.choice(unselected)
    unselected.remove(letter)
    selected.append(letter)

for old, new in zip(alphabet, selected):
    print(f"{old} -> {new}")

code_dict = {old: new for old, new in zip(alphabet, selected)}

# Randomly assign the code for numbers
unselected = [l for l in numbers]
selected = []

for i in range(len(numbers)):
    number = r.choice(unselected)
    unselected.remove(number)
    selected.append(number)

for old, new in zip(numbers, selected):
    print(f"{old} -> {new}")

for old, new in zip(numbers, selected):
    code_dict[old] = new

# Put the code in an output file
with open("key.json", "w") as f:
    json.dump(code_dict, f)
