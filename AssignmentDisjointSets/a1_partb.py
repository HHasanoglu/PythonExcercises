class SetList:
    class Node:
        def __init__(self, data, set_list, next_node, prev_node):
            self.data = data
            self.setList = set_list
            self.next_node = next_node
            self.prev_node = prev_node

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next_node

        def get_previous(self):
            return self.prev_node

        def get_set(self):
            return self.setList

    def __init__(self):
        self.head = None
        self.tail = None

    def get_front(self):
        # return first element
        return self.head

    def get_back(self):
        # return last element
        return self.tail

    def make_set(self, data):
        if self.head is None:
            new_node = self.Node(data, self, None, None)
            self.head = new_node
            self.tail = new_node
            return new_node
        return None

    def find_data(self, data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return cur
            # move cursor
            cur = cur.next_node
        return None

    def representative_node(self):
        if self.head is None:
            return None
        else:
            return self.head

    def representative(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    # push back and pop front
    def union_set(self, other_set):

        # check if other list is empty
        if other_set.head is None:
            return None

        new_node = other_set.head
        # check if current list is empty
        if self.head is None:
            # assign other list head and tail to current list
            self.head = other_set.head
            self.tail = other_set.tail
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
            self.tail = other_set.tail

        new_nodes = 0
        while other_set.head is not None:
            # change list in node
            other_set.head.setList = self

            # change head of other_set
            other_set.head = other_set.head.next_node

            # increment counter
            new_nodes = new_nodes + 1

        # clean other set
        other_set.head = None
        other_set.tail = None
        other_set = None

        temp = self.head
        while temp is not None:
            # change list in node
            temp.set_list = self

            # change head of other_set
            temp = temp.next_node

        return new_nodes

    def __len__(self):
        # return len(self.setList)
        count = 0
        # take first node
        curr_node = self.head
        # loop until end of list
        while curr_node is not None:
            count = count + 1
            curr_node = curr_node.next_node
        return count