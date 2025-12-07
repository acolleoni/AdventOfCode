file = open('input2.txt', 'r')
text_input = file.read()
range_texts = text_input.split(",")
ranges = []
for text in range_texts:
    split_text = text.split("-")
    ranges.append((int(split_text[0]),int(split_text[1])))
result = 0
for number_range in ranges:
    for number in range(number_range[0],number_range[1]+1):
        number_string = str(number)
        if len(number_string)%2 != 0 :
            continue
        if number_string[0:int(len(number_string)/2)] == number_string[int(len(number_string)/2):]:
            result = result + number
print(result)