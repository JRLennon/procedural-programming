# using a class so i can have a simple reusable strcuture, and can create new empty stacks.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("can't pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("cannot peek at an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# task: simple text editor
document = Stack()

for i in range(4): # user enter up to 4 words
    word = input(f"Enter word {i+1}: ")
    document.push(word)

print("\nCurrent document: ", " ".join(document.items))

# undo last 2 words like example
for _ in range(2):
    removed_word = document.pop()
    print(f"Undid: {removed_word}")

print("Updated document:", " ".join(document.items))

"""
the last word entered is at the top of the stack, so a pop() will remove the most recently entered word first. a peek() will return the top word without removing it
"""
