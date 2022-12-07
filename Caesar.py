alphabet_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z']


def split_characters(text):
    split_text = text.split()
    characters = []
    for word in split_text:
        characters += [c for c in word]
    return characters


while True:
    try:
        print('--------------------------------')
        encrypt_or_decrypt = input('Enter 1(Encrypt) or 2(Decrypt):\n')
        if encrypt_or_decrypt == '1' or encrypt_or_decrypt == '2':
            break
        else:
            pass
    except ValueError:
        continue
while True:
    try:
        print('-------------------')
        key_number = int(input('Enter Key Number:\n'))
        break
    except ValueError:
        continue
print('--------------------------')
text = input('Text to Encrypt/Decrypt:\n')
encrypted_text = ''
decrypted_text = ''
text_characters = split_characters(text)
for character in text_characters:
    if character in alphabet_list:
        ch_index = alphabet_list.index(character)
        if '1' in encrypt_or_decrypt:
            new_ch_index = ch_index + key_number
            new_character = alphabet_list[new_ch_index]
            encrypted_text += new_character
        else:
            new_ch_index = ch_index - key_number
            new_character = alphabet_list[new_ch_index]
            decrypted_text += new_character

print("--------------------")
if '1' in encrypt_or_decrypt:
    print("Your encrypted text:")
    print(encrypted_text)
else:
    print("Your decrypted text:")
    print(decrypted_text)