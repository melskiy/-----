from functools import cmp_to_key


def compare(item1, item2):
    if item1 + item2 > item2 + item1:
        return -1
    if item2 + item1 > item1 + item2:
        return 1
    return 0


def largest_number(a: list) -> str:
    return ''.join(sorted(a, key=cmp_to_key(compare)))


def main():
    n = int(input())
    CorrentLIst = list(input().split())
    print(largest_number(CorrentLIst))


if __name__ == '__main__':
    main()
