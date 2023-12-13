def bibao(num):
    def inner():
        nonlocal num
        num = [11, 22]
        print(num)
    return inner

if __name__ == "__main__":
    a = [11, 22]
    b = [33, 44]
    n = [a, b]
    f = bibao(n)
    f()
    print(n)