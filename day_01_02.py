from itertools import groupby
from itertools import chain

day = '01'
problem = '02'

with open(f'input/day_{day}_{problem}.txt') as f:
    input_text = f.readlines()

input_list = []
for sub in input_text:
    input_list.append(sub.replace("\n", ""))

chunks = [list(y) for x, y in groupby(input_list, lambda z: z == '') if not x]
chunks_int = [[int(num) for num in sub] for sub in chunks]

summed = []
for i in chunks_int:
    summed.append(sum(i))

summed.sort()

result = sum(summed[-3:])

print(result)