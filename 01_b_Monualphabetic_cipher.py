def additive_cipher(text, key, mode='encrypt'):
    result = ''

    # For decryption, use negative key
    if mode == 'decrypt':
        key = -key

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26
            result += chr(base + shifted)
        else:
            result += char  # symbols, spaces as it is
    
    return result




message = "Attack at Dawn"
key = 7  # you can choose any key from 1 to 25

encrypted = additive_cipher(message, key)
print("Encrypted:", encrypted)

decrypted = additive_cipher(encrypted, key, mode='decrypt')
print("Decrypted:", decrypted)
