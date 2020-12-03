import numpy as np

with open('input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

tree_count = 0
tree_counts = []
h_pos = 0

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for s, slope in enumerate(slopes):
    h_velocity, v_velocity = slope
    for v_pos in range(0, len(data), v_velocity):
        if data[v_pos][h_pos] == '#':
            tree_count += 1
        h_pos += h_velocity
        if h_pos >= len(data[v_pos]):
            h_pos -= len(data[v_pos])

    tree_counts.append(tree_count)
    tree_count = 0
    h_pos = 0

print(np.prod(tree_counts))
