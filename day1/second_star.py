with open('input.txt', 'r') as f:
    data = [int(x) for x in f.readlines() if any(char.isdigit() for char in x)]

for x in data:
    for y in data:
        for z in data:
            if x+y+z == 2020:
                print(x*y*z)
                exit(4)