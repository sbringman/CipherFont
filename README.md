# CipherFont
A human readable machine obfuscated font. It works by swapping the letter images on a font so that a message written in the substitution cipher appears in plain text to a human reader. The purpose of this font is to be used in online text to prevent, or at least slow, web scrappers from using your online writing for training LLM training data.

CipherFont uses the design and base files of Liberation Font, which is copyrighted by Red Hat under an SIL Open Font License. That license is included here in `LICENSE`, in compliance with the license. No design changes have been made to the font other than swapping glyphs (letter images) to different unicode values.

## How It Works
A font gives a set of glyphs (letter images) to unicode characters. Normally, this means that the unicode character for "a", U+0061, is given a glyph that looks like a lowercase letter a. In the default settings for CipherFont, the unicode character U+0061 is given the glpyh that looks like the lowercase letter "c". So when the text's unicode values are in normal English spelling, the appearance of the text is jumbled up in a substitution cipher and unreadable by humans without decoding. This process goes the other way as well. A text whose unicode characters are in the substitution cipher will appear as plain English to a reader. 

Because encoded text can be written in cipher and viewed as plain English, a human reader using the font will have no problem reading the encrypted text. But a LLM model trying to use the encypted text as training data, or searching the web, will not recognize the content without decryption.

## Usage
CipherFont is included in this repository in the Fonts folder as `.ttf` files. To encrypt you text, simply run `python encoder.py input_file="path_to_text"` in a terminal, and your the encrypted text will be outputted to the file `encoded.txt`. Decryption works the opposite way, with `python decoder.py input_file="path_to_code_text"` outputting decoded text to `decoded.txt`. Information on each python programs can be found by running `python program_name.py --help`. Encrypted text can be read by reading it when it is displayed in CipherFont.

## Making Your Own CipherFont
The python script that generates CipherFont files is `font_maker.py`. It uses the `fontforge` library that can be installed with `pip install fontforge`. I recommend the fontforge docs at https://fontforge.org/docs/scripting/python.html. To make your own font, follow these steps:

1. Run `randomizer.py seed=SEED`, where `SEED` is an integer other than the default 12345. This will generate a new substitution cipher stored in `key.json`. A key could also be manually entered by writing your own `key.json` file.
2. Run `font_maker.py`, which should automatically read in the LiberationFont files and ouput new CipherFont `.ttf` files.

Any font could theoretically be used as the input glyphs, but you'll have to make a few changes in `font_maker.py` to read in the correct files. The code is not too complicated, and the changes should be straightforward.

## Caveats
A simple substitution cipher is not difficult to break. When testing on Claude Haiku 4.6, it decrypted an except from Tolkien's The Hobbit fairly easily. This font is not meant to make your writings impervious to LLMs, but rather to either make it more difficult for LLMs to train on your writings or to require an extra decryption step to read them. See below for more ideas on how to enhance the cryptographic security using the same basic ideas as above.

I don't know exactly how sites are indexed by search engines, but I'm fairly certain that encrypting an entire webpage in a substitution cipher will not make it easy for a website to be properly indexed and found by prospective readers. So, I recommend keeping headings and some summary text unencoded to allow your site a better chance at being correctly indexed by a search engine.

Greek letters get messed up CipherFont because a few of them, like captial alpha, get their glyphs from the Latin letters. 

## Future Plans
In the future, I plan to also shuffle numbers around, since by default they are not. Also, I plan to use some of the unused unicode values in Liberation to implement a frequency based substitution cipher for greater security.
