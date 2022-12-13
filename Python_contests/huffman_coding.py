"""Кодирование Хаффмана

По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита,
постройте оптимальный беспрефиксный код. В первой строке выведите количество различных букв k,
встречающихся в строке, и размер получившейся закодированной строки. 
В следующих k строках запишите коды букв в формате "letter: code".
В последней строке выведите закодированную строку."""

from collections import Counter
class Tree:
    def __init__(self, cargo, weight, left=None, right=None):
        self.cargo = cargo
        self.weight = weight
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

def height(node):
    if not node:
        return 0
    l_height = height(node.left) 
    r_height = height(node.right) 
    return max(l_height, r_height) + 1

def print_level(root, level, buffer, result_dic):
    if not root:
        return
    if level == 0:
        if root.left and root.left.cargo:
            result_dic[root.left.cargo] = buffer + "0"
        if root.right and root.right.cargo:
            result_dic[root.right.cargo] = buffer + "1"
    elif level > 0:
        print_level(root.left, level - 1, buffer + "0", result_dic)
        print_level(root.right, level - 1, buffer + "1", result_dic)

def breadth_first(root, result_dic):
    if len(result_dic) == 1:
        return {list(result_dic.keys())[0] : "0"}
    h = height(root)
    buffer = ""
    for i in range(h):
        print_level(root, i, buffer, result_dic)
    return result_dic
        
def main():
    st = "dcbjuiumvvba"
    c = Counter(st)
    result_dict = dict(c)
    r = c.most_common(26)
    r.sort(key=lambda a: (a[1]*(-1), a[0]), reverse=False)

    while len(r) > 1:
        least = r.pop(-1)
        if isinstance(least[0], Tree):
            left = least[0]
        else:
            left = Tree(*least)
        least = r.pop(-1)
        if isinstance(least[0], Tree):
            right = least[0]
        else:
            right = Tree(*least)
        sum_weight = left.weight + right.weight
        tree = Tree(None, sum_weight, left, right)
        r.append((tree, sum_weight))
        r.sort(key=lambda a: (a[1]), reverse=True)

    result_tree = r[0][0]
    coder = breadth_first(result_tree, result_dict)
    code = ''.join([coder[s] for s in st])
    print(len(coder), len(code))
    for k, v in coder.items():
        print (f"{k}: {v}")
    print(code)

if __name__ == "__main__":
    main()
