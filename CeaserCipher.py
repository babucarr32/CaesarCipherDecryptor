import string
from caesarBanner import style
import caesarBanner

print(caesarBanner.banner)
alphabets = ""
with open("Alphabets.txt", "a") as w:
    for letter in string.ascii_lowercase:
        alphabets += letter

    for letter in string.ascii_uppercase:
        alphabets += letter
    w.write(alphabets)
    w.close()

with open("Alphabets.txt", "r") as f:
    reader = f.read()
# char = alphabets.index("g")
# prev_char = char - 1
# # print(alphabets[prev_char])

print(style.GREEN)
cipher = input("Enter Caesar Cipher to decrypt: ")
cipherOutput = ""
for letter in cipher:
    if letter in reader:
        letterIndex = reader.index(letter)
        prevLetter = letterIndex - 1
        cipherOutput += reader[prevLetter]
print(f"{style.MAGENTA}[+]Your decrypted cipher is [{style.BLUE}{cipherOutput}{style.MAGENTA}]")
