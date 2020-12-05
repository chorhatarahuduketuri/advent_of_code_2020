def decode_seat(datum):
    datum = datum.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return [int(datum[0:7], 2), int(datum[7:10], 2)]

data = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        data.append(decode_seat(line))

print(max([x[0] * 8 + x[1] for x in data]))
