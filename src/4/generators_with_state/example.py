# Example of a generator with extra state that can be
# accessed.   Simply define as a class!

from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines):
            self.history.append((lineno, line))
            # if lineno == 1:
            #     print(lineno, line)
            #     for lineno, hline in self.history:
            #         print('{}:{}'.format(lineno, hline), end='')
            yield line

    def clear(self):
        self.history.clear()


with open('somefile.txt') as f:
    lines = linehistory(f, 4)
    for line in lines:
        if 'python' in line:
            print("find python")
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')
