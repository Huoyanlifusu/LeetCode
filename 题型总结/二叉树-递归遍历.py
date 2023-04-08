1.确定函数的参数和返回值
2.确定递归终止的条件
3.确定单层递归的逻辑

前序
def digui(cur, path):
    if cur == None:
        return
    path.append(cur.val)
    digui(cur.left, path)
    digui(cur.right, path)
    return path
          
中序
def digui(cur, path):
    if cur == None:
        return
    digui(cur.left, path)
    path.append(cur.val)
    digui(cur.right, path)
    return path
  
后序
def digui(cur, path):
    if not cur:
        return
    digui(cur.left, path)
    digui(cur.right, path)
    path.append(cur.val)
    return path
