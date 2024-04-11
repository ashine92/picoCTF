# 1_wanna_b3_a_r0ck5tar

mình vào trang https://web.archive.org/web/20190522020843/https://codewithrockstar.com/online để convert bài hát như đề bài đã cho. Tuy nhiên ở bài này ta sẽ phải nhập input. Khi nhập bất kì input random nào cũng không có manh mối gì, nên mình sẽ thử cách khác.

Theo solution của bài này https://github.com/Dvd848/CTFs/blob/master/2019_picoCTF/1_wanna_b3_a_r0ck5tar.md 

ta có thể chuyển đổi lyric thành đoạn code bằng [Python transpiler](https://github.com/yanorestes/rockstar-py). Sử dụng cách này có vẻ nhanh hơn:

```python
$ rockstar-py -i lyrics.txt -o lyrics.py
$ cat lyrics.py
Rocknroll = True
Silence = False
a_guitar = 10
Tommy = 44
Music = 170
the_music = input()
if the_music == a_guitar:
    print("Keep on rocking!")
    the_rhythm = input()
    if the_rhythm - Music == False:
        Tommy = 66
        print(Tommy!)
        Music = 79
        Jamming = 78
        print(Music!)
        print(Jamming!)
        Tommy = 74
        print(Tommy!)
        They are dazzled audiences
        print(it!)
        Rock = 86
        print(it!)
        Tommy = 73
        print(it!)
        break
        print("Bring on the rock!")
        Else print("That ain't it, Chief")
        break
```

Và khi chạy thử đoạn code ta thấy không thành công:

```python
$ python3 lyrics.py
  File "/home/ashine92/pico/lyrics.py", line 12
    print(Tommy!)
               ^
SyntaxError: invalid syntax
```

Đọc sơ qua bài code, mình đoán ta cần nhập input cho biến `the_music` làm sao để bằng `a_guitar`(đang có giá trị là 10). Mình thử nhập `10` vào bài, nhưng kết quả không khả quan lắm. Sau một hồi xem lại, mình thấy có vẻ lỗi là ở việc tool Python đã convert chưa sát với đề. Nên mình quyết định decode từng dòng một theo Docs của trang web: 

https://web.archive.org/web/20190521190259/https://codewithrockstar.com/docs

![image](https://github.com/ashine92/picoCTF/assets/62413378/6f26a17a-6af7-4c4a-83d7-6003167baa88)

```python
Rocknroll is right
Silence is wrong
```

```python
Rocknroll = True
Silence = False
```

![image](https://github.com/ashine92/picoCTF/assets/62413378/fc4a4c11-6aad-4452-a64c-cb2cf99f82de)

![image](https://github.com/ashine92/picoCTF/assets/62413378/79b4a272-9dd2-48a0-892f-bba663b11108)

```python
A guitar is a six-string
Tommy's been down
Music is a billboard-burning razzmatazz!
```

```python
a_guitar = 136
tommy = 44
music = 1970
```

Vậy đến đây ta đã nhận ra, `a_guitar` có giá trị thật là 136 chứ không phải `10` như tool trên đã convert. Vậy ta nhập `136` vào thử → trang web yêu cầu ta nhập thêm một input nữa, chứng tỏ ta đã đi đúng hướng. Vậy ta sẽ tìm input tiếp theo:

![image](https://github.com/ashine92/picoCTF/assets/62413378/e3d23ccb-3f20-4079-967c-776729858460)

![image](https://github.com/ashine92/picoCTF/assets/62413378/7cf426de-377b-4135-8c4e-a279af23e8cb)

```python
Listen to the rhythm
If the rhythm without Music is nothing
```

```python
the_rhythm = input()
if the_rhythm - Music == False
```

Mà như đã phân tích ở trên, ta có `music` = 1970. Vậy ta sẽ nhập 1970 là input tiếp theo.

![image](https://github.com/ashine92/picoCTF/assets/62413378/04e92af2-e67f-40d1-9410-c403ee047220)

Đề bài cho ta 7 con số, suy đoán có thể đây là những kí tự ASCII.

![image](https://github.com/ashine92/picoCTF/assets/62413378/fb780f93-d2e5-4401-a4dd-eb372d1be2a4)

⇒ Flag: picoCTF{BONJOVI}
