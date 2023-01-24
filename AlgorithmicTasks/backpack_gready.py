'''Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6.
Каждая из следующих n строк задает стоимость 0≤c_i≤2⋅10^6 и объём 0≤w_i≤2⋅10^6предмета (n, W, c_i и w_i — целые числа). 
Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, 
стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак,
с точностью не менее трёх знаков после запятой.'''
def main():
    n, W = list(map(int, input().split()))
    price_volume = [list(map(int, input().split())) for i in range(n)]
    sp_price = [[p/v, v] for p, v in price_volume]
    sp_price.sort(reverse=True)
    result = 0
    for sp, v in sp_price:
        can_take = min(v, W)
        result += can_take * sp
        W -= can_take
        if W <= 0:
            break
    print('{:.3f}'.format(result))

import heapq

def main_heap():
    # Реализация через кучу
    n, W = list(map(int, input().split()))
    price_volume = [list(map(int, input().split())) for i in range(n)]
    sp_price = [(-p/v, v)for p, v in price_volume]
    heapq.heapify(sp_price)
    result = 0
    while sp_price and W:
        sp, v = heapq.heappop(sp_price)
        can_take = min(v, W)
        result -= can_take * sp
        W -= can_take
    print('{:.3f}'.format(result))


if __name__ == "__main__":
    main()