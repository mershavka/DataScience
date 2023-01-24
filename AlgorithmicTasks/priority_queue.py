"""Очередь с приоритетом

Первая строка входа содержит число операций 1≤n≤10^5.
Каждая из последующих n строк задают операцию одного из следующих двух типов:
- Insert x, где 0≤x≤10^9 — целое число;
- ExtractMax;
Первая операция добавляет число x в очередь с приоритетами, 
вторая — извлекает максимальное число и выводит его."""
import math
class priorityQueue:
    def __init__(self) -> None:
        self.heap = []

    def siftUp(self):
        sifting_index = len(self.heap) - 1
        while sifting_index > 0 and self.heap[sifting_index] > self.heap[math.floor((sifting_index-1)/2)]:
            self.heap[sifting_index], self.heap[math.floor((sifting_index-1)/2)] = self.heap[math.floor((sifting_index-1)/2)], self.heap[sifting_index]
            sifting_index = math.floor((sifting_index-1)/2)

    def siftDown(self):
        sifting_index = 0
        while 2 * sifting_index < len(self.heap) - 1:
            first_child_index = 2 * sifting_index + 1
            second_child_index = first_child_index + 1
            if second_child_index >= len(self.heap):
                second_child_index = first_child_index
            child_index = first_child_index if self.heap[first_child_index] >= self.heap[second_child_index] else second_child_index
            if self.heap[sifting_index] >= self.heap[child_index]:
                break
            self.heap[sifting_index], self.heap[child_index] = self.heap[child_index], self.heap[sifting_index]
            sifting_index = child_index

    def append(self, value):
        self.heap.append(value)
        self.siftUp()

    def extractMax(self):
        if not self.heap:
            return
        maxx = self.heap[0]
        if len(self.heap)>1:
            self.heap[0]=self.heap.pop()
        else:
            return self.heap.pop()
        self.siftDown()
        return maxx


def main():
    n = int(input())
    heap = priorityQueue()
    for _ in range(n):
        command = input().split()
        if command[0] == "ExtractMax":
            print(heap.extractMax())
        elif command[0] == "Insert":
            value = int(command[1])
            heap.append(value)


if __name__ == "__main__":
    main()