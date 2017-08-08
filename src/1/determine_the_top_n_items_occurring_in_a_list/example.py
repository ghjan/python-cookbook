# example.py
#
# Determine the most common words in a list
"""
Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的工具。 在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现。
"""

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

<<<<<<< HEAD
if __name__ == '__main__':
    from collections import Counter

    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)
    # outputs [('eyes', 8), ('the', 5), ('look', 4)]

    # Example of merging in more words

    morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
    word_counts.update(morewords)
    print(word_counts.most_common(3))

    print("---------------")
    a = Counter(words)
    b = Counter(morewords)
    print("a:", a)
    print("b:", b)
    c = a + b
    print("a+b:", c)
    d = a - b
    print("a-b:", d)
=======
from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# outputs [('eyes', 8), ('the', 5), ('look', 4)]

# Example of merging in more words

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
word_counts.update(morewords)
print(word_counts.most_common(3))
>>>>>>> 171d85594813b31860a23f77a624d62fa52cbbb1
