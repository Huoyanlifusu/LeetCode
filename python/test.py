path = []
array = []
def partition(s):
    backsearch(s, 0)
    return array

def backsearch(s, startindex):
    if startindex == len(s):
        array.append(path.copy())
        return
    for i in range(startindex, len(s)):
        if huiwen(s[startindex:i+1]):
            path.append(str(s[startindex:i+1]))
        else:
            continue
        backsearch(s, i+1)
        path.remove(str(s[startindex:i+1]))

def huiwen(s):
    if len(s) == 1:
        return True
    else:
        left, right = 0, len(s) -1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
# partition("aab")
