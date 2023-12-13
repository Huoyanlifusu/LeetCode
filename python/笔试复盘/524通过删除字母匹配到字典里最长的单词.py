s = input("匹配字符串")
dictionary = input("字符串数组").split()

res = ""
# 双指针
# 贪心的思想，因为删除后的字符串数组仍然是按照原先的顺序
# 因此遇到相遇字符就可以删除，以此增加后面的搜索空间
for word in dictionary:
    i, j = 0, 0
    while i < len(s) and j < len(word):
        if s[i] == word[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == len(word):
        if len(word) > len(res) or len(word) == len(res) and word < res:
            res = word

print(res)