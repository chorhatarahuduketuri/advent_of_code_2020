with open('input.txt', 'r') as f:
    data_descending = [int(x) for x in f.readlines() if any(char.isdigit() for char in x)]

data_descending.sort(reverse=True)
data_ascending = data_descending[::-1]

for big in data_descending:
    for small in data_ascending:
        if big+small == 2020:
            print(big*small)
            exit(4)
