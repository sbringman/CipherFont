import json
import argparse
import random as r

parser = argparse.ArgumentParser(
    prog="encoder",
    description="Encodes a text file for using CipherFont."
)

parser.add_argument("input_file", nargs="?", default="decoded.txt", help="Input file of text to encode.")
parser.add_argument("output_file", nargs="?", default="encoded.txt", help="Output file of encoded text.")

args = parser.parse_args()

# Get key
with open("encode_key.json", "r") as f:
    key = json.load(f)

# Get text
with open(args.input_file, "r") as f:
    input_string = f.read()

# Encode text
output_string = ""
for c in input_string:
    if str(ord(c)) in key.keys():
        output_string += chr(r.choice(key[str(ord(c))]))
    else:
        output_string += c

# Write out text
with open(args.output_file, "w") as f:
    f.write(output_string)

print(f"Output written to: {args.output_file}")