# caeser cypher encrypts message, then decrypts 
# Author: Jatin Pandya
# Based off of: https://en.wikipedia.org/wiki/Caesar_cipher

# Get message from user
message = input("Enter your message:")
message = lower(message)
print("Your message was: ", message)

#Enter number to shift the message

temp = input("Number to shift by:")
n = int(temp)
print("Shifting by: ", message)

#https://stackoverflow.com/questions/36186762/how-can-i-use-the-chr-and-ord-command-to-decipher-a-message-that-a-user-has
list = [ord(ch) for ch in message]
encrypted_list = []

for num in list:
    num -= 97
    num = (num + n) % 26
    num += 97
    #https://stackoverflow.com/questions/40567103/attributeerror-list-object-has-no-attribute-add
    encrypted_list.append(num)
#https://stackoverflow.com/questions/180606/how-do-i-convert-a-list-of-ascii-values-to-a-string-in-python
encrypted_message = "".join([chr(c) for c in encrypted_list])
print("Encrypted Message:", encrypted_message)

decrypted_list = []
print("Original list: ",list)
print("Encrypted List", encrypted_list)
for num in encrypted_list:
    num -= 97
    print(num)
    num = (num - n) % 26
    num += 97
    decrypted_list.append(num)

decrypted_message = "".join([chr(c) for c in decrypted_list])
print("decrypted Message:", decrypted_message)