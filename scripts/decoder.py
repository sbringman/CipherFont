import json
import argparse

parser = argparse.ArgumentParser(
    prog="decoder",
    description="Decodes a text file for using CipherFont."
)

parser.add_argument("input_file", nargs="?", default="encoded.txt", help="Input file of encoded text.")
parser.add_argument("output_file", nargs="?", default="decoded.txt", help="Output file decoded text.")

args = parser.parse_args()

# Get key
with open("decode_key.json", "r") as f:
    key = json.load(f)

# Get text
with open(args.input_file, "r") as f:
    input_string = f.read()

# Decode text
output_string = ""
for c in input_string:
    if str(ord(c)) in key.keys():
        output_string += chr(key[str(ord(c))])
    else:
        output_string += c
    
# Write out text
with open(args.output_file, "w") as f:
    f.write(output_string)

print(f"Output written to: {args.output_file}")