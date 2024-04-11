# Glitch Cat
```python
$  nc saturn.picoctf.net 55826
'picoCTF{gl17ch_m3_n07_' + chr(0x39) + chr(0x63) + chr(0x34) + chr(0x32) + chr(0x61) + chr(0x34) + chr(0x35) + chr(0x64) + '}'
```

```python
>>> lst = [0x39, 0x63, 0x34, 0x32, 0x61, 0x34, 0x35, 0x64]
>>> for i in lst:
...   print(chr(i), end='')
...
9c42a45d
```

⇒ Flag: picoCTF{gl17ch_m3_n07_9c42a45d}
