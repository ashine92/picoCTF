# Special

Connect SSH với server, ta được một chương trình Shell, tuy nhiên chương trình shell này sẽ thay đổi kí tự khi ta nhập bất kì lệnh nào, ví dụ:

```python
Special$ whoami
Whom
sh: 1: Whom: not found
Special$ pwd
Pod
sh: 1: Pod: not found
```

Tuy nhiên sau một hồi thử thì mình nhận thấy khi bọc quanh các câu lệnh với kí tự `""`, `''` hay `()` thì câu lệnh sẽ sử dụng được.

```python
Special$ 'whoami'
'whoami'
ctf-player

Special$ "whoami"
"whoami"
ctf-player

Special$ (whoami)
(whoami)
ctf-player
```

Mình sẽ dùng kí tự `""` để bao quanh lệnh:

```python
Special$ "pwd"
"pwd"
/home/ctf-player

Special$ "/bin/ls"
"/bin/ls"
blargh

Special$ "/bin/ls" "blargh"
"/bin/ls" "blargh"
flag.txt

Special$ "/bin/cat" "blargh/flag.txt"
"/bin/cat" "blargh/flag.txt"
picoCTF{5p311ch3ck_15_7h3_w0r57_3befb794}
```
