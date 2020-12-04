import re

re_hcl = re.compile(r'^#[0-9a-f]{6}$')
re_ecl = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')
re_pid = re.compile(r'^[0-9]{9}$')
re_hgt_cm = re.compile(r'^\d{3}cm$')
re_hgt_in = re.compile(r'^\d{2}in$')

valid_fields = {
    'byr': lambda x: 1920 <= int(x) <= 2002,  # Birth Year
    'iyr': lambda x: 2010 <= int(x) <= 2020,  # Issue Year
    'eyr': lambda x: 2020 <= int(x) <= 2030,  # Expiration Year
    'hgt': lambda x: check_height(x),  # Height
    'hcl': lambda x: re_hcl.match(x),  # Hair Color
    'ecl': lambda x: re_ecl.match(x),  # Eye Color
    'pid': lambda x: re_pid.match(x),  # Passport ID
}

data = []

with open('input.txt', 'r') as f:
    credential = {}
    text = f.read()
    lines = [line.replace('\n', ' ').strip() for line in text.split('\n\n')]
    for line in lines:
        data.append({k: v for (k, v) in [x.split(':') for x in line.split(' ')]})


def check_height(x):
    if re_hgt_cm.match(x):
        if 150 <= int(x[0:3]) <= 193:
            return True
    if re_hgt_in.match(x):
        if 59 <= int(x[0:2]) <= 76:
            return True
    return False


number_of_valid_passports = 0
for datum in data:
    if all([(datum.get(k) and v(datum[k])) for (k, v) in valid_fields.items()]):
        number_of_valid_passports += 1

print(number_of_valid_passports)
