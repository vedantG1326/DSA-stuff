class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def add(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            return
        t = self.head
        while t.next:
            t = t.next
        t.next = n

    def display(self):
        t = self.head
        while t:
            print(t.data, end=" -> ")
            t = t.next

l = LL()
l.add(10)
l.add(20)
l.add(30)
l.display()
