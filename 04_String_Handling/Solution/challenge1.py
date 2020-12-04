title = "Caesar Cipher"
print("=" * 30, title, "-" * len(title), sep="\n")

message = input("Enter a message:")
encrypted_message = ""
for c in message:
    encrypted_message += chr(ord(c) + 1)
print(f"{title}=>Encrypt In:{message}, Out:{encrypted_message}")

decrypted_message = ""
for c in encrypted_message:
    decrypted_message += chr(ord(c) - 1)

print(f"{title}=>Decrypt In:{encrypted_message}, Out:{decrypted_message}")

title = "Vignère Cipher"
print("=" * 30, title, "-" * len(title), sep="\n")
key = input("Enter a cipher key:")
message = input("Enter the message for encryption:")
encrypted_message = ""

key_len = len(key)
key_codes =[ord(c) for c in key]
message_codes =[ord(c) for c in message]
for count, code in enumerate(message_codes):
    encrypted_message += chr(code + key_codes[count % key_len])
print(f"{title}=>Encrypt In:{message}, Out:{encrypted_message}")

message_codes = [ord(c) for c in encrypted_message]
decrypted_message =""
for count, code in enumerate(message_codes):
    decrypted_message += chr(code - key_codes[count % key_len])

print(f"{title}=>Decrypt In:{encrypted_message}, Out:{decrypted_message}")
