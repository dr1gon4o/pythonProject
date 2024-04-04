from collections import deque


class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.deq = deque(x for x in self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        word = ""

        if self.number == 0:
            raise StopIteration

        word = self.deq.popleft()
        self.deq.append(word)
        self.number -= 1

        return word

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
