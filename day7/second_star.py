import re

# re_bag = re.compile('(\d+)(\s\w*\s\w*\sbag)')
re_bag = re.compile('(\d+\s)?(\w*\s\w*\sbag)')

data = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        data.append(re_bag.findall(line))


def extract_contained_bags(line, contained_bag):
    if ('', contained_bag) in line:
        return line[1:]


containing_bags = []


def count_contained_bags(contained_bag):
    print(f'contained_bag: {contained_bag}')
    for datum in data:
        bags = extract_contained_bags(datum, contained_bag[1])
        print(f'bags: {bags}')
        if bags:
            for bag in bags:
                print(f'bag[0]: {bag[0]}')
                print(f'bag[1]: {bag[1]}')
                return int(contained_bag[0])*count_contained_bags(bag[1]) if count_contained_bags(bag[1]) else 1
        return 1*int(contained_bag[0])
    return 1*int(contained_bag[0])
            # for bag in bags:
            #     containing_bags.add(bags)
            #     count_contained_bags(bags)



print(count_contained_bags(('1', 'shiny gold bag')))
