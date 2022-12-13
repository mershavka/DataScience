def main():
    k, l = map(int, input().split())
    encoder = {}
    min_bit_length = 10**4
    for _ in range(k):
        symbol, value = input().split(": ")
        encoder[value] = symbol
        min_bit_length = len(value) if len(value) < min_bit_length else min_bit_length
    code = input()
    result = ""
    stopper = min_bit_length
    while code:
        tmp = code[:stopper]
        if tmp in encoder.keys():
            result += encoder[tmp]
            code = code[stopper:]
            stopper = min_bit_length
        else:
            stopper += 1
    print(result)
        

if __name__ == "__main__":
    main()