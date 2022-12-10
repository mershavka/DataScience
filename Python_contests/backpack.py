'''Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6.
Каждая из следующих n строк задает стоимость 0≤c_i≤2⋅10^6 и объём 0≤w_i≤2⋅10^6предмета (n, W, c_i и w_i — целые числа). 
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, 
стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак,
с точностью не менее трёх знаков после запятой.'''
def main():
    n, W = list(map(int, input().split()))
    price_volume = [list(map(int, input().split())) for i in range(n)]
    sp_price = [[p/v, v] for p, v in price_volume]
    sp_price.sort()
    result = 0
    while W and sp_price:
        sp = sp_price[-1][0]
        v = sp_price[-1][1]
        if v > W:
            v = W
        result += v * sp
        W -= v
        sp_price.pop(-1)
    print(result)

if __name__ == "__main__":
    main()