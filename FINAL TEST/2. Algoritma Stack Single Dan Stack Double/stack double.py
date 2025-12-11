#IBRAHIM
#D0425013
#UAS PEMROGRAMAN

nama_program="STACK DOUBLE"
print(nama_program)

class StackDouble:
    def __init__(self):
        self.stack = []

    def push(self, value: float):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack kosong!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack kosong!"

    def is_empty(self):
        return len(self.stack) == 0

stack = StackDouble()
stack.push(1.16)
stack.push(6.26)
stack.push(6.66)

print("TOP:", stack.peek())
print("POP:", stack.pop())
print("STACK sekarang:", stack.stack)