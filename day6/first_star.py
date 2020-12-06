with open('input.txt', 'r') as f:
    print(sum([len(set(x.replace('\n', ''))) for x in f.read().split('\n\n')]))
