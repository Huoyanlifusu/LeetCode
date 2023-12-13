def solution(price, target):
    i, j = 0, len(price) - 1
    while i < j:
        if price[i] + price[j] == target:
            return [price[i], price[j]]
        elif price[i] + price[j] < target:
            i += 1
        else:
            j -= 1