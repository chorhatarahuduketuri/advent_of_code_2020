import re

with open('input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines() if any(char.isdigit() for char in x)]

re_pw_data = re.compile(r"^(?P<pos>\d{1,2}-\d{1,2})\s(?P<character>\w):\s(?P<password>\w*)$")


def parse_line(pw_data):
    result = re_pw_data.match(pw_data).groupdict()
    result['pos'] = [int(x) for x in result['pos'].split('-')]
    return result


def check_password(pw_datum):
    char1 = pw_datum['password'][pw_datum['pos'][0]-1]
    char2 = pw_datum['password'][pw_datum['pos'][1]-1]
    if (char1+char2).count(pw_datum['character']) == 1:
        return True
    return False


print(sum([check_password(parse_line(x)) for x in data]))
