import string

print("-----------------------------------")
print(">>>>>>>>>>.Encoder 1.0.<<<<<<<<<<<<")
print("-----------------------------------")

print("Insert letters")

alphabet = string.ascii_lowercase
original_letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

parola = input()


offset = 1



modified_letter_to_index = {}
for letter, index in original_letter_to_index.items():
    modified_index = (index + offset) % len(alphabet)
    modified_letter_to_index[letter] = modified_index

def codifica_posizionale(text):
    encoded_text = []
    for letter in text:
        index = modified_letter_to_index[letter]
        encoded_text.append(str(index))
    return ' '.join(encoded_text)

def decodifica_posizionale(encoded_text):
    encoded_text = encoded_text.split()
    decoded_text = []
    for index in encoded_text:
        letter = index_to_letter[int(index)]
        decoded_text.append(letter)
    return ''.join(decoded_text)

print("Coded:")
encoded_text = codifica_posizionale(parola)
print(encoded_text)

print("---------------------------")
print("-------By Tronco2018-------")
print("---------------------------")


