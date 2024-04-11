# plumbing

Sau khi kết nối với server bằng netcat thì ta thấy server trả về một loạt đoạn văn. Vì vậy ta sẽ lưu kết quả vào file output.txt và grep chúng:

```python
$ nc jupiter.challenges.picoctf.org 14291 > output.txt
$ strings output.txt | grep pico
picoCTF{digital_plumb3r_ea8bfec7}
```
