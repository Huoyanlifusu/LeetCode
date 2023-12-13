# 大体的设计思想：用哈希表存储键值对，再用双向链表记录节点的更改顺序
# 一旦取了某个键值，或者插入了新的键值对，就把对应的节点移动到链表的末尾
# 从而保证最久没有被使用的键在链表的头部

class ListNode(object):
    def __init__(self, key=None, val=None) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRU(object):
    def __init__(self, capacity) -> None:
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
        self.tail.prev = node
        node.prev.next = node

    
    def get(self, key):
        if key in self.dic:
            self.move_node_to_tail(self.dic[key])
            return self.dic[key].val
        else:
            return -1
    
    def put(self, key, value):
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.move_node_to_tail(node)
        else:
            node = ListNode(key=key, val=value)
            if len(self.dic.keys()) == self.capacity:
                tmp = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.dic[tmp.key]
            self.insert_node_to_tail(node)
            self.dic[key] = node

obj = None
while True:
    order = input("指令")
    param = list(map(int, input("参数").split()))

    if order == "LRUCache":
        obj = LRU(capacity=param[0])
    elif order == "put":
        obj.put(param[0], param[1])
        print(obj.dic)
    elif order == "get":
        x = obj.get(param[0])
        print(x)
    else:
        break