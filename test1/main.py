from collections import deque


class Node(object):
    def __init__(self, value, p=None):
        self.value = value
        self.p = p


class LinkList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, date):
        node = Node(date, self.head)
        self.head = node

    def delete_node(self):
        temp_node = self.head
        last_node = self.head
        while temp_node.p is not None:
            last_node = temp_node
            temp_node = temp_node.p
        last_node.p = None

    def print_value(self):
        temp_node = self.head
        while temp_node.p is not None:
            print(temp_node.value, end=" ")
            temp_node = temp_node.p
        print(temp_node.value)

    def change_node(self, value="a"):
        temp_node = self.head
        if temp_node.value == value:
            return True
        while temp_node.p is not None:
            temp_node2 = temp_node
            temp_node = temp_node.p
            if temp_node.value == value:
                temp_node2.p == temp_node.p
                self.insert(temp_node.value)
                self.delete_node()
                return True
            self.insert(value)
            self.delete_node()
            return False



if __name__ == '__main__':
    node_head = Node('b', None)
    cache = LinkList(node_head)
    cache.insert('a')
    cache.print_value()
    q = ['a', 'b', 'c', 'b', 'c', 'a', 'b']
    for q_item in q:
        result = cache.change_node(q_item)
        if not result:
            print("cache miss!", end=" ")
        cache.print_value()



