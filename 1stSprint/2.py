def sleight_of_hand(field: str) -> int:
    c = 0
    for i in range(1, 10):
        if 0 < field.count(str(i)) <= 2 * k:
            c += 1
    return c
k = int(input())
field = "".join(input() for i in range(4))

print(sleight_of_hand(field))