# Collabative Development

```
$ git branch
  feature/part-1
  feature/part-2
  feature/part-3
* main
```
Part 1:
```
$ git checkout feature/part-1
Switched to branch 'feature/part-1'
$ cat flag.py
print("Printing the flag...")
print("picoCTF{t3@mw0rk_", end='')
```
Part 2:
```
$ git checkout feature/part-2
Switched to branch 'feature/part-2'
$ cat flag.py
print("Printing the flag...")

print("m@k3s_th3_dr3@m_", end='')
```
Part 3:
```
$ git checkout feature/part-3
Switched to branch 'feature/part-3'
$ cat flag.py
print("Printing the flag...")

print("w0rk_e4b79efb}")
```
picoCTF{t3@mw0rk_m@k3s_th3_dr3@m_w0rk_e4b79efb}
