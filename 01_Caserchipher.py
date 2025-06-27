def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char  
    
    return result

# Encryption
encrypted = caesar_cipher("Hello, World!", 3)
print("Encrypted:", encrypted)   # Khoor, Zruog!

# Decryption
decrypted = caesar_cipher(encrypted, 3, mode='decrypt')
print("Decrypted:", decrypted)   # Hello, World!
