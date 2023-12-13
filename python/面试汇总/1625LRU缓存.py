class ListNode(object):
    def __init__(self, val=0, key=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_node_to_tail(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.insert_node_to_tail(node)
    
    def insert_node_to_tail(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            self.move_node_to_tail(self.dic[key])
            return self.dic[key].val
        else: return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = ListNode(value, key)
        if key in self.dic:
            self.move_node_to_tail(self.dic[key])
            self.dic[key].val = value
        elif self.capacity:
            self.dic[key] = node
            self.insert_node_to_tail(node)
            self.capacity -= 1
        else:
            k = self.head.next.key
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            del self.dic[k]
            self.insert_node_to_tail(node)
            self.dic[key] = node