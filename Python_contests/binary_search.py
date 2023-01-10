"""В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных натуральных чисел,
не превышающих 10^9, в порядке возрастания, во второй — целое число 1≤k≤10^5
и k натуральных чисел b_1,…,b_k, не превышающих 10^9. Для каждого i от 1 до k
необходимо вывести индекс 1≤j≤n, для которого A[j]=b_i, или -1, если такого j нет."""
import math
def binary_search(value, sorted_list):
    index = -1
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mean = math.floor(left + (right - left)/2)
        if sorted_list[mean] == value:
            index = mean
            break
        elif sorted_list[mean] < value:
            left = mean + 1
        else:
            right = mean - 1
    index = index + 1 if index >= 0 else index
    return index

def left_binary_search(value, sorted_list):
    # l < x <= r
    left = -1
    right = len(sorted_list)
    while right - left > 1:
        mean = (left + right)//2
        if sorted_list[mean] < value:
            left = mean
        else:
            right = mean
    if sorted_list[right] == value:
        return right
    return -1

def right_binary_search(value, sorted_list):
    # l <= x < r
    left = -1
    right = len(sorted_list)
    while right - left > 1:
        mean = (left + right)//2
        if sorted_list[mean] <= value:
            left = mean
        else:
            right = mean
    if sorted_list[left] == value:
        return left
    return -1

def main():
    n, *A = map(int, input().split())
    k, *B = map(int, input().split())
    result = []
    for element in B:
        result.append(binary_search(element, A))
    print(*result)

if __name__ == "__main__":
    main()