def reverse_integer(x: int, n: int) -> int:
    y = 0
    i = int('1' + '0'*(n-1))
    while i >= 1:
        temp = int(x/10)
        y += (round((x/10 - temp), 1) * 10) * i
        y = int(y)
        x = temp
        i /= 10
    return y


if __name__ == "__main__":
    x = input()
    print(reverse_integer(
            int(x),
            len(x) if int(x)>0 else len(x)-1
        )
    )