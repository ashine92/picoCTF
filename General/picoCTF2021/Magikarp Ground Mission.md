Kết nối SSH bằng lệnh `ssh [ctf-player@venus.picoctf.net](mailto:ctf-player@venus.picoctf.net) -p 55539` và nhập password: 481e7b14

```python
ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ strings 1of3.flag.txt
-bash: strings: command not found
ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_
ctf-player@pico-chall$ cat instructions-to-2of3.txt
Next, go to the root of all things, more succinctly `/`
ctf-player@pico-chall$ ls -a
.  ..  1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls
2of3.flag.txt  dev   instructions-to-3of3.txt  media  proc  sbin  tmp
bin            etc   lib                       mnt    root  srv   usr
boot           home  lib64                     opt    run   sys   var
ctf-player@pico-chall$ cat 2of3.flag.txt
0ut_0f_\/\/4t3r_
ctf-player@pico-chall$ cat instructions-to-3of3.txt
Lastly, ctf-player, go home... more succinctly `~`
ctf-player@pico-chall$ cd ~
ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt
1118a9a4}
```

⇒ Flag: picoCTF{xxsh_0ut_0f_\/\/4t3r_1118a9a4}
