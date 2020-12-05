def decode_seat(datum):
    datum = datum.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return [int(datum[0:7], 2), int(datum[7:10], 2)]


data = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        data.append(decode_seat(line))

seat_ids = [x[0] * 8 + x[1] for x in data]
seat_ids.sort()

for i, seat_id in enumerate(seat_ids):
    if seat_ids[i + 1] != seat_id + 1:
        print(seat_id + 1)
        exit(4)
