def dynamic_xor_decrypt(semi_text, text_key):
  plaintext = ""
  key_length = len(text_key)
  for i, char in enumerate(semi_text):
    key_char = text_key[i % key_length]
    decrypted_char = chr(ord(char) ^ ord(key_char))
    plaintext += decrypted_char
  return plaintext[::-1]

def decrypt(c, key):
  semi_text = ""
  for num in c:
    semi_text += chr(num // key // 311)
  return semi_text

def generator(g, x, p):
  return pow(g, x) % p

cipher = [131553, 993956, 964722, 1359381, 43851, 1169360, 950105, 321574, 1081658, 613914, 0, 1213211, 306957, 73085, 993956, 0, 321574, 1257062, 14617, 906254, 350808, 394659, 87702, 87702, 248489, 87702, 380042, 745467, 467744, 716233, 380042, 102319, 175404, 248489]
semi_text = decrypt(cipher, 47)
text_key = "trudeau"
print(dynamic_xor_decrypt(semi_text, text_key))
