class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        if not self.head or not self.head.next:
            return
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            sorted_list.sorted_insert(current.data)
            current = next_node
        self.head = sorted_list.head

    def sorted_insert(self, data):
        new_node = Node(data)
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def merge_sorted(self, other_list):
        dummy = Node()
        tail = dummy
        a, b = self.head, other_list.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a or b
        self.head = dummy.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Демонстрація роботи:

# Створюємо перший список
a = LinkedList()
a.insert_at_end(1)
a.insert_at_end(3)
a.insert_at_end(5)

# Створюємо другий список
b = LinkedList()
b.insert_at_end(2)
b.insert_at_end(4)
b.insert_at_end(6)

print("Список A перед реверсом:")
a.print_list()
a.reverse()
print("Список A після реверсу:")
a.print_list()

print("Список A перед сортуванням:")
a.insert_at_beginning(7)
a.insert_at_beginning(0)
a.print_list()
a.sort()
print("Список A після сортування:")
a.print_list()

print("Об'єднання списків A і B:")
a.merge_sorted(b)
a.print_list()