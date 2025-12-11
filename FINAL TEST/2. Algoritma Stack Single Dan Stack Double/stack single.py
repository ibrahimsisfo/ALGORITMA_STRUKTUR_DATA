#IBRAHIM
#D0425013
#UAS PEMROGRAMAN

nama_program="STACK SINGLE"
print(nama_program)

class Stack:
    def __init__(self):
        self.stack = []

    # Menambah elemen ke stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} ditambahkan ke stack")

    # Menghapus elemen paling atas
    def pop(self):
        if self.is_empty():
            print("Stack kosong, tidak bisa POP")
            return None
        return self.stack.pop()

    # Melihat elemen paling atas tanpa menghapus
    def peek(self):
        if self.is_empty():
            print("Stack kosong")
            return None
        return self.stack[-1]

    # Cek apakah stack kosong
    def is_empty(self):
        return len(self.stack) == 0

    # Menampilkan isi stack
    def display(self):
        print("Isi stack:", self.stack)


# Contoh penggunaan
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Elemen paling atas:", s.peek())

print("Melakukan POP:", s.pop())
s.display()