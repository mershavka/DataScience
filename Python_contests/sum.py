import os
from collections import Counter

file_path = os.path.realpath(__file__)
print()
with open('/Users/mershavka/Repositories/DataScience/Python_contests/input.txt', 'r') as f_in:
    J = f_in.readline()
    S = f_in.readline()
J_dict = Counter(J)
print(J_dict)
S_dict = Counter(S)
print(S_dict)
result = 0
for key, value in S_dict.items():
    if key in J_dict:
        result += J_dict[key]
with open('/Users/mershavka/Repositories/DataScience/Python_contests/output.txt', 'w') as f_out:
    f_out.write(str(result))
