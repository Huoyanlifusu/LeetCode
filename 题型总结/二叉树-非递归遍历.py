方法一 用栈来模拟递归

前序遍历 
不断往栈里添加左子和右子节点 直到所有节点都被遍历
stack = []
res = []
if root: stack.append(root)
while stack:
    node = stack.pop()
    if node:
        res.append(node.val)
    else:
        continue
    stack.append(node.right)
    stack.append(node.left)
return res

后序遍历 
颠倒入栈顺序 反转数值列表即可
res = []
stack = []
if root: stack.append(root)

while stack:
    node = stack.pop()
    if node:
        res.append(node.val)
    else:
        continue
    stack.append(node.left)
    stack.append(node.right)
if res:
    res.reverse()
return res

中序遍历 
巧妙在于左子节点为空时栈弹出 右子节点为空时同样弹出
stack = []
res = []
cur = root
while cur or stack:
    if cur:
        stack.append(cur)
        cur = cur.left
    else:
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
return res

方法二 用队列实现遍历

层序遍历 102, 107, 116, 117, 199, 429, 515, 637
图论中bfs在二叉树的应用
queue = []
result = []
if root:
    queue.append(root)
while queue:
    size = len(queue)
    path = []
    while size:
        size -= 1
        node = queue.pop(0)
        path.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    result.append(path)
return result
