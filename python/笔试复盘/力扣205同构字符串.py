import collections
s = input()
t = input()
# 通过两个哈希表的互相映射，确保两对字符串的每对字符都有一一映射的关系，
# 如果存在打破映射规则的情况，则视为不匹配
dic_s = collections.defaultdict(str)
dic_t = collections.defaultdict(str)

res = True

if len(s) != len(t):
    res = False

else:
    for i in range(len(s)):
        ch_s, ch_t = s[i], t[i]
        if (ch_s in dic_s and dic_s[ch_s] != ch_t) or (ch_t in dic_t and dic_t[ch_t] != ch_s):
            res = False
            break
        dic_s[ch_s] = ch_t
        dic_t[ch_t] = ch_s

print(res)