import re


def check_height(x):
    pass


valid_fields = {
    'byr': lambda x: 1920 <= x <= 2002,  # Birth Year'
    'iyr': lambda x: 2010 <= x <= 2020,  # Issue Year'
    'eyr': lambda x: 2020 <= x <= 2030,  # Expiration Year'
    'hgt': lambda x: check_height(x),  # Height'
    'hcl': lambda x: re.compile(r'^#[0-9a-f]{6}$').match(x),  # Hair Color'
    'ecl': lambda x: re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$').match(x),  # Eye Color'
    'pid': lambda x: re.compile(r'^[0-9]{9}$').match(x),  # Passport ID'
    'cid': lambda x: True,  # Country ID'
}

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
