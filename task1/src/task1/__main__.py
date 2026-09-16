def main():
    a = 0
    b = 0
    while id(a) == id(b):
        a += 1
        b += 1
    N = a - 1
    a = 0
    b = 0
    while id(a) == id(b):
        a -= 1
        b -= 1
    M = a + 1
    print(M, N)

if __name__ == "__main__":
    main()