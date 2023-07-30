import string

print("-----------------------------------")
print(">>>>>>>>>>.Decoder 1.0.<<<<<<<<<<<<")
print("-----------------------------------")

print("Insert number")

alphabet = string.ascii_lowercase
original_letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))
 

offset = 1




modified_letter_to_index = {}
for letter, index in original_letter_to_index.items():
    modified_index = (index + offset) % len(alphabet)
    modified_letter_to_index[letter] = modified_index
modified_index_to_letter = dict(zip(modified_letter_to_index.values(), modified_letter_to_index.keys()))


encoded_text = input()

def codifica_posizionale(text):
    decoded_text = ''
    text = text.split()
    for index in text:
        letter = modified_index_to_letter[int(index)]
        decoded_text += letter
    return decoded_text

def decodifica_posizionale(decoded_text):
    encoded_text = []
    for letter in decoded_text:
        index = modified_letter_to_index[letter]
        encoded_text.append(str(index))
    return ' '.join(encoded_text)

print("Encoded:")
decoded_text = codifica_posizionale(encoded_text)
print(decoded_text)

print("---------------------------")
print("-------By Tronco2018-------")
print("---------------------------")