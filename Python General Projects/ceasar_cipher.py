# Caesar cipher.

def encrypt(text, shift):
    cipher = ''
    for char in text:
        code = ord(char) + shift
        if code > ord('~'):
            code = ord(' ') + (code - ord('~'))
        cipher += chr(code)

    return cipher


def decrypt(cipher, shift):
    decipher = ''
    for char in cipher:
        code = ord(char) - shift
        if code < ord(' '):
            code = ord('~') - (ord(' ') - code)
        decipher += chr(code)

    return decipher


text = input("Enter your message: ")

invalid = True
while invalid: 
    shift = int(input("Enter Integer Shift (2-92): "))
    if shift < 2 or shift > 92:
        print("Invalid shift. Enter integer between 2-92.")
    else:
        invalid = False

cipher = encrypt(text, shift)
decrypted = decrypt(cipher, shift)

print(cipher)
print(decrypted)
