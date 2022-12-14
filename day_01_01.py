from itertools import groupby

day = '01'
problem = '01'

with open(f'input/day_{day}_{problem}.txt') as f:
    input_text = f.readlines()

input_list = []
for sub in input_text:
    input_list.append(sub.replace("\n", ""))

chunks = [list(y) for x, y in groupby(input_list, lambda z: z == '') if not x]
chunks_int = [[int(num) for num in sub] for sub in chunks]

i = 0
result = 0

for i in chunks_int:
    curr = sum(i)
    result = max(curr, result)

print(result)
