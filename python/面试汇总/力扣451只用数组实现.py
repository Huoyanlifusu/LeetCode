class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        def cntIndex(i):
            if arr[i].isdigit(): cnti = 52+int(arr[i])
            elif arr[i] == arr[i].lower(): cnti = ord(arr[i])-ord('a')
            else: cnti = 26+ord(ch)-ord('A')
            return cnti

        ch_counter = [0] * 62
        arr = ["0"] * len(s)
        for i, ch in enumerate(s):
            arr[i] = ch
            ch_counter[cntIndex(i)] += 1

        def partition(arr, left, right):
            pivot = cntIndex(left)
            i = left + 1
            for j in range(left+1, right):
                nj = cntIndex(j)
                if ch_counter[nj] > ch_counter[pivot] or (ch_counter[nj] == ch_counter[pivot] and arr[j] < arr[left]):
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[left], arr[i-1] = arr[i-1], arr[left]
            return i-1

        def quicksort(arr, left, right):
            if left >= right:
                return
            pi = partition(arr, left, right)
            quicksort(arr, left, pi)
            quicksort(arr, pi+1, right)
        
        quicksort(arr, 0, len(arr))
        return "".join(arr)