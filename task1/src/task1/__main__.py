def countNM(isPositive):
    """Функция прибавляет или убавляет от двух нулевых переменных единицу 
    и возвращает значение, при котором две переменные имеют одиннаковый id.
    Args:
        isPositive (bool): Если true, то функция складывает, если false, то убавляет.
    Returns:
        int: Значение при котором две переменные имеют одиннаковый id.
    """
    a = 0
    b = 0
    count = 1
    if isPositive == False:
        count = -1
    while id(a) == id(b):
        a += count
        b += count
    return a - count

def main():
    N = countNM(True)
    M = countNM(False)
    print(M, N)

if __name__ == "__main__":
    main()