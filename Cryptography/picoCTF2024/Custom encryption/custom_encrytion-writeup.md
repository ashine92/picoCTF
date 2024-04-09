# Custom Encryption

Với hàm này ta sẽ phân tích từng hàm một từ hàm main trở lên:
```sh
if __name__ == "__main__":
    message = sys.argv[1]
    test(message, "trudeau")
```
Hàm main này sẽ dùng hàm test để làm gì đó với `message` ban đầu và chữ "trudeau".

```sh
def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')
```

Với cipher ta đã tải về như sau:
```sh
a = 94
b = 21
cipher is: [131553, 993956, 964722, 1359381, 43851, 1169360, 950105, 321574, 1081658, 613914, 0, 1213211, 306957, 73085, 993956, 0, 321574, 1257062, 14617, 906254, 350808, 394659, 87702, 87702, 248489, 87702, 380042, 745467, 467744, 716233, 380042, 102319, 175404, 248489]
```

Ta sẽ bắt đầu vào hàm encrypt tương ứng và dựng ngược lại thành hàm decrypt:
```sh
def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher
```
Dễ thấy rằng từng chữ cái trong plaintext sẽ chuyển đổi thành ký tự số và nhân với `key*311`. Vậy key ở đây là gì?
Nhìn lại dòng code ban đầu:
```sh
if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
```
và
```sh
 key = generator(v, a, p)
```
Ta lại truy ngược về hàm generator, để ý thấy rằng hàm này không ảnh hưởng trực tiếp đến kết quả chung. Nên ta sẽ dựng lại y hệt:
```sh
def generator(g, x, p):
    return pow(g, x) % p
```
Vậy nếu ta có `a = 94`, `b = 21` thì `u = 43`, `v = 8` => `key = b_key = shared_key = 47`. Vậy ta sẽ có key ở đây là 47. Ta sẽ dựng lại hàm decrypt như sau:
```sh
def decrypt(c, key):
  semi_text = ""
  for num in c:
    semi_text += chr(num // key // 311)
  return semi_text
```
Để tìm ra plaintext ta cần phân tích tiếp hàm dynamic_xor_encrypt:
```sh
def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text
```
Ta dựng lại như sau:
```sh
def dynamic_xor_decrypt(semi_text, text_key):
  plaintext = ""
  key_length = len(text_key)
  for i, char in enumerate(semi_text):
    key_char = text_key[i % key_length]
    decrypted_char = chr(ord(char) ^ ord(key_char))
    plaintext += decrypted_char
  return plaintext[::-1]
```
## decrypt_custom.py
```sh
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
```

Flag: `picoCTF{custom_d2cr0pt6d_8b41f976}`
