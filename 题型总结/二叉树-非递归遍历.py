方法一 用栈来模拟递归

前序遍历 不断往栈里添加左子和右子节点 直到所有节点都被遍历
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

后序遍历 颠倒入栈顺序 反转数值列表即可
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
