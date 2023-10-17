def fizzbuzz(i: int) -> str:
    """
    # FizzBuzz

    1. 3の倍数の場合はFizz
    2. 5の倍数の場合はBuzz
    3. 3の倍数かつ5の倍数の場合はFizzBuzz
    4. それ以外は数字を文字列に変換して返す
    """
    tmp = ""
    if i % 3 == 0:
        tmp = "Fizz"
    if i % 5 == 0:
        tmp += "Buzz"
    return tmp if tmp != "" else str(i)


if __name__ == "__main__":
    for i in range(1, 100 + 1):
        print(fizzbuzz(i))
