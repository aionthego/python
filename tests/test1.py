import sys

def collect_fre(input: str) -> str:
    result: dict[str, int] = {}
    for char in input:
        print(char)
        if char in result:
            count = result[char]
            result[char] = count + 1
        else:
            result[char] = 1
    for k in result.keys():
        print(f'key {k}: {result[k]}')

def main(input: str):
    collect_fre(input)

if __name__ == "__main__":
    input: str = "abcadebcf"
    print(input)
    main(input)
