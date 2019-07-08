# ---------- PROBLEM : CAESAR'S CIPHER ----------
# Receive a message and then encrypt it by shifting the
# characters by a requested amount to the right
# A becomes D, B becomes E for example
# Also decrypt the message back again

# Cycle through each character in the message
def cipher(befMessage, key):

	aftMessage = ''
	for char in befMessage:

		# if it is a letter
		if char.isalpha():

			# Get unicode and add the shift amount
			char_code = ord(char) + key

			# if uppercase
			if char.isupper():

				# if greater than 'Z'
				if char_code > ord('Z'):
					char_code -= 26

				# if less than 'A'
				if char_code < ord('A'):
					char_code += 26

			# if lowercase
			if char.islower():

				# if greater than 'z'
				if char_code > ord('z'):
					char_code -= 26

				# if less than 'a'
				if char_code < ord('a'):
					char_code += 26

			# Convert from code to letter and add to message
			aftMessage += chr(char_code)

		# if not a letter leave the character as is
		else:
			aftMessage += char
	return aftMessage

# Receive the message to encrypt and the number of characters to shift
message = input("Enter your message: ")
key = int(input("How many characters should we shift(-26 ~ 26) "))

secret_message = cipher(message, key)

# print the encrypted message
print("Encrypted message: ", secret_message)

# To decrypt the only thing that changes is the sign of the key
key = -key

orig_message = cipher(secret_message, -key)

print("Decrypted message: ", orig_message)