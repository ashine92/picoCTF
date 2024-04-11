# Based.md

Ở thử thách này đòi hỏi ta phải có sự hiểu biết về nhiều loại encodings. Kết hợp với [kt.gy](http://kt.gy) tool ta sẽ có được flag:

```python
$ nc jupiter.challenges.picoctf.org 15130
Let us see how data is stored
falcon
Please give the 01100110 01100001 01101100 01100011 01101111 01101110 as a word.
...
you have 45 seconds.....

Input:
falcon
Please give me the  163 164 162 145 145 164 as a word.
Input:
street
Please give me the 636f6e7461696e6572 as a word.
Input:
container
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_02167de8}
```
