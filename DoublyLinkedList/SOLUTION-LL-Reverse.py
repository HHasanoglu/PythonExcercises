class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push_back(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def push_front(self, value):
        if self.length == 0:
            self.push_back(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1

    def pop_front(self):
        value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return value

    def pop_back(self):
        value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return
        if self.length == 0:
            self.push_back(value)
        else:
            new_node = Node(value)
            indexcount = 0
            temp = self.head
            while indexcount < index - 1:
                temp = temp.next
                indexcount += 1
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1

    def erase(self, index):
        if index < 0 or index > self.length:
            return
        if self.length == 0:
            return
        else:
            indexcount = 0
            temp = self.head
            while indexcount < index - 1:
                temp = temp.next
                indexcount += 1
            temp.next = temp.next.next
            self.length -= 1

    def print_list(self):
        temp_node = self.head
        text = ""
        for i in range(0, self.length):
            text += str(temp_node.value) + "->"
            temp_node = temp_node.next
        print(text)

    def print_list_reverse(self):
        temp_node = self.tail
        text = ""
        for i in range(0, self.length):
            text += str(temp_node.value) + "->"
            temp_node = temp_node.prev
        print(text)


'''
    def sortedInsert(self, value):
        new_node = Node(value)
        # special case for the head end
        if self.head is None or self.head.value >= new_node.value:
            new_node.next = self.head
            self.head = new_node
        else:
            # Locate the node before the poof insertion
            current = self.head
            while current.next is not None and current.next.value < new_node.value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1
'''

my_linked_list = LinkedList()
my_linked_list.push_back(1)

my_linked_list.push_back(9)
my_linked_list.push_back(7)
my_linked_list.print_list()
my_linked_list.print_list_reverse()
my_linked_list.pop_back()
my_linked_list.print_list()
my_linked_list.print_list_reverse()
"""
class LinkedList:
    def __init__(self):
        # new_node = Node(value)
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
"""
