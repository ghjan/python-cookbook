# example.py
#
# Example of some tricky sanitization problems

# A tricky string
s = 'p\xfdt\u0125\xf6\xf1\x0cis\tawesome\r\n'
print(s)

# (a) Remapping whitespace
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}

a = s.translate(remap)
print('whitespace remapped:', a)

# (b) Remove all combining characters/marks
import unicodedata
import sys

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

# 然后使用 unicodedata.normalize() 将原始输入标准化为分解形式字符。
# 然后再调用 translate 函数删除所有重音符。 同样的技术也可以被用来删除其他类型的字符(比如控制字符等)。
b = unicodedata.normalize('NFD', a)
c = b.translate(cmb_chrs)
print('accents removed:', c)

# (c) Accent removal using I/O decoding
d = b.encode('ascii', 'ignore').decode('ascii')
print('accents removed via I/O:', d)

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}

print(len(digitmap))

# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

# 对于简单的替换操作， str.replace() 方法通常是最快的
def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', ' ')
    s = s.replace('\f', ' ')
    return s
