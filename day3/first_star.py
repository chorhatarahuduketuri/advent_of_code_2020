with open('input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]
tree_count = 0
h_pos = 0
for row in data:
    if row[h_pos] == '#':
        tree_count += 1
    h_pos += 3
    if h_pos >= len(row):
        h_pos -= len(row)

print(tree_count)
