import sys

def test3():
    print("test 3")
    input: str = "abcabcabdabeabf"
    result: set() = {char for char in input}
    print(result)
            

if __name__ == "__main__":
    test3()
