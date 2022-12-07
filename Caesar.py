import string

# Creating a list of all alphanumeric characters
alphabet_chars = []
for num in string.digits:
    alphabet_chars.extend(num)
for char in string.ascii_letters:
    alphabet_chars.extend(char)

#################################

# Input to choose encryption or decryption
while True:
    print('------------------------------')
    encrypt_or_decrypt = input('Enter 1(Encrypt) or 2(Decrypt):\n')
    if encrypt_or_decrypt == '1' or encrypt_or_decrypt == '2':
        break
    else:
        print('#######################################################')
        print('-- Please enter either 1 to encrypt, or 2 to decrypt --')
        print('#######################################################')
        pass

# Input for key number
while True:
    try:
        print('-----------------')
        key_number = int(input('Enter Key Number:\n'))
        break
    except ValueError:
        print('#################################')
        print('-- Please enter a valid number --')
        print('#################################')
        continue

# Input for text
while True:
    try:
      print('-------------------------------------------')
      text = input('Enter the text to Encrypt/Decrypt:\n')
      for char in text:
        if char not in alphabet_chars:
          raise ValueError
      break
    except ValueError:
      print('******************************************************************')
      print('-- Please enter text that only contains alphanumeric characters --')
      print('******************************************************************')
      continue

output_text = ''


# the '% len (alphabet_chars)' makes sure that if the index goes beyond the list's length, it 'starts over' at index 0, as if it were a circle
# anything below the result of len(alphabet_chars) will return whatever number resulted from alphabet_chars[(alphabet_chars.index(c) + shift). but if, for example, the length is 26 and the other number is 27, the modulus is equal to 1, which is the index position that corresponds.
# Use a ternary operator to determine the shift direction (encrypt or decrypt)
shift = key_number if encrypt_or_decrypt == 1 else - key_number
encrypted_chars = [alphabet_chars[(alphabet_chars.index(c) + shift) % len(alphabet_chars)] for c in text]
output_text = "".join(encrypted_chars)

print("-----------------")
print("Your result text:")
print(output_text)