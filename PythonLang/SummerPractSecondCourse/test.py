# D43FAF0ED9E66A9E
# 48656C6C6F
# 48656C6C6F20776F726C6421
import codecs

text = "Hello world!"
a = text.encode('utf-16').hex().upper()
a = "92A972653B"
print(a)
b = bytes.fromhex(a).decode('utf-16')
