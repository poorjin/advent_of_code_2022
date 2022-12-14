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
curr = 0
store = {}
for i in range(len(chunks)):
    store[i] =  sum(chunks_int[i])
    curr = max(store[i], curr)

print(curr)
