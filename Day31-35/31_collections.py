"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common())
"""
找出序列中出现次数最少的元素
"""
counter = Counter(words)
print(counter.most_common()[:-4:-1])
"""
找出序列中出现次数最频繁的元素
"""
counter = Counter(words)
print(counter.most_common(1)[0][0])
"""
找出序列中出现次数最不频繁的元素
"""
counter = Counter(words)
print(counter.most_common()[-1][0])
