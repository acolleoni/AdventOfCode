file = open("input5.txt", "r")
lines = file.readlines()
file.close()

line_index = 0
ranges = []
while lines[line_index] != '\n':
    lines[line_index] = lines[line_index].strip()
    range_start, range_end=lines[line_index].split('-')
    ranges.append((int(range_start), int(range_end)))
    line_index+=1

def valueIsInRange(value, range):
    return value >= range[0] and value <= range[1]

def rangesOverlap(range, other_range):
    return valueIsInRange(range[0], other_range) or valueIsInRange(range[1], other_range) or valueIsInRange(other_range[0], range) or valueIsInRange(other_range[1], range)

def mergeRanges(range, other_range):
    new_start = range[0] if range[0] <= other_range[0] else other_range[0]
    new_end = range[1] if range[1] >= other_range[1] else other_range[1]
    return (new_start, new_end)

for range_index, range in enumerate(ranges):
    for other_range_index, other_range in enumerate(ranges):
        if range_index == other_range_index:
            continue
        if rangesOverlap(range, other_range):
            ranges[range_index] = (-1, -1)
            ranges[other_range_index] = mergeRanges(range, other_range)

total_valid_numbers=0
for range in ranges:
    if range[0] == -1:
        continue
    total_valid_numbers += range[1] - range[0] + 1

print(total_valid_numbers)