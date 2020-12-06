with open('input.txt', 'r') as f:
    print(sum([len(z) for z in [set.intersection(*[set(y) for y in x.split('\n')]) for x in f.read().strip().split('\n\n')]]))
