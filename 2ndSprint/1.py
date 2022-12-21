def psp(n:int, s='', left=0, right=0) -> None:
    if left == n and right == n:
        print(s)
    else:
        if left < n:
            psp(n, s + '(', left+1, right)
        if right < left:
            psp(n, s + ')', left, right+1)


def main():
    n = int(input())
    psp(n)

if __name__ == '__main__':
    main()
