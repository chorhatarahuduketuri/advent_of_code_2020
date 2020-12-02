import re

with open('input.txt', 'r') as f:
    data = [x for x in f.readlines() if any(char.isdigit() for char in x)]

re_pw_data = re.compile(r"^(?P<count>\d{1,2}-\d{1,2})\s(?P<character>\w):\s(?P<password>\w*)$")


def parse_line(pw_data):
    result = re_pw_data.match(pw_data).groupdict()
    result['count'] = [int(x) for x in result['count'].split('-')]
    return result


def check_password(pw_datum):
    occurances = pw_datum['password'].count(pw_datum['character'])
    return pw_datum['count'][0] <= occurances <= pw_datum['count'][1]


print(sum([check_password(parse_line(x)) for x in data]))
