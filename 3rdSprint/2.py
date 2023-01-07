import string
def is_palindrom(s:str) -> bool:
    s =s.translate(str.maketrans('', '', string.punctuation)).lower().replace(" ",'')
    return s == s[::-1]  

def main():
    s = input()
    print(is_palindrom(s))

if __name__ == '__main__':
    main()


