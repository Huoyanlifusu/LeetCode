class ListNode(object):
    def __init__(self, val=0):
        self.next = None
        self.val = val

nodes = list(map(int, input("请输入链表数据").split()))
head = ListNode(nodes[0])
ref = head
for num in nodes[1:]:
    cur_node = ListNode(num)
    ref.next = cur_node
    ref = cur_node

# 关键在于维护两个指针 一个存储下个节点 一个存储下一次的前个节点
cur = head
tmp = None
while cur and cur.next:
    res = cur.next
    cur.next = tmp
    tmp = cur
    cur = res

if cur:
    cur.next = tmp

while cur:
    print(cur.val)
    cur = cur.next