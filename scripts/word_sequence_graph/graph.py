# class Graph:
#     def __init__(self, word, index, prev, next):
#         self.index = index
#         self.prev = prev
#         self.next = next
#         self.word = word
#
#     def graph_info(self):
#         str = f'[{self.index}]: {self.prev.word} -> {self.word} -> {self.next.word}'
#         print(str)


class Graph:
    def __init__(self, word, index, prev):
        self.index = index
        self.prev = prev
        self.word = word

    def graph_info(self):
        str = f'[{self.index}]: {self.prev.word} -> {self.word}'
        print(str)
