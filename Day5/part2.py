import re

result = {}

with open('Day5/data.txt', 'r') as file:
    lines = file.read().splitlines()

for line in lines:
    if ' 1   2' not in line:
        continue
    data = line.replace(' ', '')
    for i in range(len(data)):
        result[data[i]] = []

lines.reverse()

for line in lines:
    if '[' not in line:
        continue
    data = line.replace('[', '').replace(']', '').replace('    ', '0').replace(' ', '')
    for i in range(len(data)):
        if data[i] == '0':
            continue
        result[str(i + 1)].append(data[i])

lines.reverse()

for line in lines:
    if 'move' not in line:
        continue
    line = line.strip()
    match = re.match(r'move (\d+) from (\d+) to (\d+)', line)
    moves, source, destination = map(int, match.groups())

    slice = result[str(source)][-moves:]
    result[str(source)] = result[str(source)][:-moves]
    result[str(destination)] += slice

count1 = len(result['1'])
count2 = len(result['2'])
count3 = len(result['3'])
count4 = len(result['4'])
count5 = len(result['5'])
count6 = len(result['6'])
count7 = len(result['7'])
count8 = len(result['8'])
count9 = len(result['9'])

print("Result: ")
print(result['1'][count1 - 1] + result['2'][count2 - 1] + result['3'][count3 - 1] +
      result['4'][count4 - 1] + result['5'][count5 - 1] + result['6'][count6 - 1] +
      result['7'][count7 - 1] + result['8'][count8 - 1] + result['9'][count9 - 1])
