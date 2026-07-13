def caesar_encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char

    return encrypted


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


print("=" * 45)
print("      Caesar Cipher Encryption Tool")
print("=" * 45)

message = input("Enter Message: ")
shift = int(input("Enter Shift Value: "))

encrypted = caesar_encrypt(message, shift)
print("\nEncrypted Message :", encrypted)

decrypted = caesar_decrypt(encrypted, shift)
print("Decrypted Message :", decrypted)
