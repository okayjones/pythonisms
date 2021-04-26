class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [LinkedList() for _ in range(size)]

    def _hash(self, key):
        total = sum([ord(ch) for ch in key])
        return (total * 7) % self.size

    def add(self, key, value):
        idx = self._hash(key)
        self._buckets[idx].add((key, value))

    def get(self, key):
        bucket = self._buckets[self._hash(key)]
        current = bucket.head
        while current:
            if current.data[0] == key:
                return current.data[1]
            else:
                current = current.next

    def contains(self, key):
        bucket = self._buckets[self._hash(key)]
        current = bucket.head
        while current:
            if current.data[0] == key:
                return True
            else:
                current = current.next
        return False


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return values