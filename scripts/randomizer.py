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
print("Seed: ", args.seed)
r.seed(args.seed)

# Start with the alphabets used - all in unicode
latin_alphabet_upper = [0x41 + i for i in range(26)] # 26
latin_alphabet_lower = [0x61 + i for i in range(26)] # 26
numbers = [0x30 + i for i in range(10)] # 10
frequencies = [8, 2, 3, 4, 13,
               2, 2, 6, 7, 1,
               1, 4, 2, 7, 8,
               2, 1, 6, 6, 9,
               3, 1, 2, 1, 2, 1] # 104 * 2 = 208

# 218 total unicode are needed to have enough glyphs to 
# cover the numbers and the upper and lowercase versions of each
# frequency substitution of each latin letter

# We'll reuse the 52 latin characters and 10 numbers

# We'll also use Canadian syllabics for the excess characters
canadian_syllabics = [0x1400 + i for i in range(156)] 

# Totalling 218 as well


# Construct the pool of plaintext letters (letters to encode)
plaintext_pool = []
for letter, freq in zip(latin_alphabet_upper, frequencies):
    for i in range(freq):
        plaintext_pool.append(letter)

for letter, freq in zip(latin_alphabet_lower, frequencies):
    for i in range(freq):
        plaintext_pool.append(letter)

for num in numbers:
    plaintext_pool.append(num)

# Construct the pool of unicodes to encode the letters as
unicode_pool = []
for code_list in ([latin_alphabet_upper, latin_alphabet_lower,
                   numbers, canadian_syllabics]):
    for uc in code_list:
        unicode_pool.append(uc)

# Ensure that they are the same size
assert len(plaintext_pool) == len(unicode_pool), f"Plaintext: {len(plaintext_pool)}, Unicode: {len(unicode_pool)}"

# Construct the pool of indexes to link the two lists
indexes = [i for i in range(len(plaintext_pool))]

# Make the code dictionary
encode_dict = {} # Keys are true letters, values are lists of encoded unicode
decode_dict = {} # Keys are encoded unicode, values are true letters

for i_plain in range(len(plaintext_pool)):
    i_uni = r.choice(indexes)
    decode_dict[unicode_pool[i_uni]] = plaintext_pool[i_plain]

    # Either start a new list
    if plaintext_pool[i_plain] not in encode_dict.keys():
        encode_dict[plaintext_pool[i_plain]] = [unicode_pool[i_uni]]
    # Or add the unicode option to the current list
    else:
        encode_dict[plaintext_pool[i_plain]].append(unicode_pool[i_uni])

    indexes.remove(i_uni)

# Print out the code
alphabetized_keys = sorted(encode_dict.keys())
for key in alphabetized_keys:
    print(f"{chr(key)} -> {[chr(uc) for uc in encode_dict[key]]}")

# Put the code in an output file
with open("decode_key.json", "w") as f:
    json.dump(decode_dict, f)

with open("encode_key.json", "w") as f:
    json.dump(encode_dict, f)
