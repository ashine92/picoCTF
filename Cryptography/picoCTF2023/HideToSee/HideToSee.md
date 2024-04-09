# HideToSee

```sh
$ steghide extract sf atbash.jpg
Enter passphrase:
wrote extracted data to "encrypted.txt".
$ cat encrypted.txt
krxlXGU{zgyzhs_xizxp_xz00558y}
```

Sau đó vào trang https://www.dcode.fr/atbash-cipher để decode:
Flag: `picoCTF{atbash_crack_ca00558b}`
