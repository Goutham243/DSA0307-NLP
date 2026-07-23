#PROGRAM 1#
import re

text = input("Enter a text: ")
pattern = input("Enter a pattern to search: ")

# Search for the pattern
match = re.search(pattern, text)

# Display the result
if match:
    print("Pattern found!")
    print("Matched text:", match.group())
    print("Found at position:", match.start())
else:
    print("Pattern not found.")
