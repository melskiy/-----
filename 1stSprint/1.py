def zerodist(array: list) -> list:
    indexes = [i for i, d in enumerate(array) if d == 0]
    for i in range(len(array)):
        array[i] = min(abs(i - x) for x in indexes)
    return array


ListofNumbers = list(map(int, input().split()))

print(*zerodist(ListofNumbers))
