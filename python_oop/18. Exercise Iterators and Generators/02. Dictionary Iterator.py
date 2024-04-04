from collections import deque


class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.haha = deque(dictionary.items())

        #votri variant
        # self.elements = list(dictionary.items())
        # self.idx = 0


    def __iter__(self):
        return self

    def __next__(self):

        if len(self.haha) == 0:
            raise StopIteration

        return self.haha.popleft()

        #vtoria variant
        # if self.idx == len(self.elements):
        #     raise StopIteration
        #
        # curr_idx = self.idx
        # self.idx += 1
        # return self.elements[curr_idx]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
