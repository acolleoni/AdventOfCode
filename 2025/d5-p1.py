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

line_index+=1

fresh_ingredients_nr=0
while line_index != len(lines):
    current_id = int(lines[line_index].strip())
    for range in ranges:
        if current_id >= range[0] and current_id <= range[1]:
            fresh_ingredients_nr+=1
            break
    line_index+=1

print(fresh_ingredients_nr)