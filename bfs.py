__author__ = 'Qi_He'

class Queue:
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        self.items = []

    def push(self, x):
        self.items.insert(0, x)

    def pull(self):
        self.items.pop()


class stack:
    def __init__(self):
        self.items = []

    def push(self, x):