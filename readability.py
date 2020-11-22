"""

ReadAbility
A tool that determines the corresponding US school grade for a text.

"""

from cs50 import get_string
import re

text = get_string("Text: ")
words_split = re.split("\s", text)
words = len(words_split)
sentences = 0
letters = 0

for i in range(len(text)):
    if text[i].isalpha() == True:
        letters += 1
    if text[i] == "." or text[i] == "!" or text[i] == "?":
        sentences += 1

L = letters / words * 100
S = sentences / words * 100

grade = round(0.0588 * L - 0.296 * S - 15.8)

if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print(f"Grade {grade}")

