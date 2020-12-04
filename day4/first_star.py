required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
data = []

with open('input.txt', 'r') as f:
    credential = {}
    text = f.read()
    lines = [line.replace('\n', ' ').strip() for line in text.split('\n\n')]
    for line in lines:
        data.append({k: v for (k, v) in [x.split(':') for x in line.split(' ')]})

number_of_valid_passports = 0
for datum in data:
    if all(field in datum for field in required):
        number_of_valid_passports += 1

print(f'len(number_of_valid_passports): {number_of_valid_passports}')
