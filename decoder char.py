import string

print("-----------------------------------")
print(">>>>>>>>>>.Decoder 1.0.<<<<<<<<<<<<")
print("-----------------------------------")

print("Insert encoded text")

original_letter_to_char = dict(zip(string.ascii_lowercase, ['!', '@', '#', '$', '%', '&', '*', '$', '(', ')', '-', '+', '=', '[', ']', '{', '}', '/', '|', '.', '~', '^', '_', '<', '>', '?', ':'] * len(string.ascii_lowercase)))

char_to_original_letter = {}
for key, value in original_letter_to_char.items():
    char_to_original_letter[value] = key

encoded_text = input()

def decodifica_preset(encoded_text):
    decoded_text = ''
    for char in encoded_text:
        decoded_text += char_to_original_letter[char]
    return decoded_text

print("Decoded:")
decoded_text = decodifica_preset(encoded_text)
print(decoded_text)

print("-------------------------------")
print("--------By Tronco2018----------")
print("-------------------------------")