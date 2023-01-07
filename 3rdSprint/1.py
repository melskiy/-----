def dec_to_bin(n:int) -> str:
    bin = ''
    sign = ''
    if n < 0:
        sign = '-'
        n = abs(n)
    if n == 0:
        return '0'
    while n > 0:
        bin = str(n % 2) + bin
        n = n // 2
    return sign + bin
  

def main():
    n = int(input())
    print(dec_to_bin(n))

if __name__ == '__main__':
    main()
