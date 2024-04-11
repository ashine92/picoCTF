# Nice netcat

```python
$ nc mercury.picoctf.net 22342
112
105
99
111
67
84
70
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
53
102
98
53
101
53
49
100
125
10
```

# solve.py

```python
char = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 53, 102, 98, 53, 101, 53, 49, 100, 125, 10]
for i in char:
  print(chr(i), end='')
```

```python
$ python3 nice.py
picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}
```