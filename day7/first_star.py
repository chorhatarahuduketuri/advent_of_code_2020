import re

re_bag = re.compile(r'(\w*\s\w*\sbag)')

data = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        data.append(re_bag.findall(line))


def extract_containing_bags(line, contained_bag):
    if contained_bag in line[1:]:
        return line[0]


containing_bags = set()


def find_containing_bags(contained_bag):
    for datum in data:
        bag = extract_containing_bags(datum, contained_bag)
        if bag:
            containing_bags.add(bag)
            find_containing_bags(bag)


find_containing_bags('shiny gold bag')
print(len(containing_bags))
