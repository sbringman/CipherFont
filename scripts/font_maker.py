import fontforge as ff
import json
import shutil
import pathlib
import os


font_classes = [
    "Mono",
    "Sans",
    "SansNarrow",
    "Serif"
]
emphases = [
    "Bold",
    "BoldItalic",
    "Italic",
    "Regular"
]

template_name = "Liberation"
target_name = "CipherFont"
template_dir = "../Fonts/Liberation/"
target_dir = "../Fonts/CipherFont/"

# Check if output directory exists
# Create it if not
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Get key 
with open("encode_key.json", "r") as f:
    key = json.load(f)

def create_cipher_font(template_dir, 
                        new_dir,
                        template_name,
                        new_name,
                        font_class,
                        emphasis,
                        key):

    font_type = f"{font_class}-{emphasis}"

    font_path = f"{template_dir}/{template_name}{font_type}.ttf"
    font_save_path = f"{new_dir}/{new_name}{font_type}.sfd"

    # Get the font to copy from
    old_font = ff.open(font_path)

    # Create the new font as an exact 
    # copy of the old font.
    # This way all symbols are copied and 
    # there is no starting fron scratch.
    shutil.copy2(font_path, font_save_path)

    # Change the names to the correct new names
    new_font = ff.open(font_save_path)
    new_font.fontname = f"{new_name}{font_type}"
    new_font.fullname = f"{new_name} {font_class} {emphasis}"
    new_font.familyname = f"{new_name} {font_class}"

    # XUIDs must not be extensively used much 
    #(from the fontforge docs), so I'll just set it to 0
    new_font.uniqueid = 0

    # Now select letters from the old 
    # font and copy them to the new font.
    # Iterate over the key value pairs in the dictionary
    for k in key.keys():
        old_font.selection.select(int(k))
        old_font.copy()
        for val in key[k]:
            new_font.selection.select(int(val))
            new_font.paste()

    new_font.save(font_save_path)
    new_font.generate(f"{new_dir}/{new_name}{font_class}-{emphasis}.ttf")
    
    # Remove the sfd file when we're done with it
    pathlib.Path.unlink(font_save_path)

for fc in font_classes:
    for e in emphases:
        if e != "Regular":
            f_type = f"{fc}-{e}"
        else:
            f_type = f"{fc}"
        print(f"Creating {target_name}{f_type}.sfd")
        create_cipher_font(template_dir,
                            target_dir,
                            template_name,
                            target_name,
                            fc,
                            e,
                            key,
                            )