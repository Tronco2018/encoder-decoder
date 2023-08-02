import string

print("-----------------------------------")
print(">>>>>>>>>>.Encoder 1.0.<<<<<<<<<<<<")
print("-----------------------------------")

original_letter_to_char = dict(zip(string.ascii_lowercase, ['!', '@', '#', '$', '%', '&', '*', '$', '(', ')', '-', '+', '=', '[', ']', '{', '}', '/', '|', '.', '~', '^', '_', '<', '>', '?', ':'] * len(string.ascii_lowercase)))

parola = input()

def codifica_preset(text):
    encoded_text = ''
    for letter in text:
        encoded_text += original_letter_to_char[letter]
    return encoded_text

print("Coded:")
encoded_text = codifica_preset(parola)
print(encoded_text)

print("---------------------------")
print("-------By Tronco2018-------")
print("---------------------------")
