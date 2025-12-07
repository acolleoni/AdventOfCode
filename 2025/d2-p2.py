import sympy
import textwrap

file = open('input2.txt', 'r')
text_input = file.read()
range_texts = text_input.split(",")
ranges = []
for text in range_texts:
    split_text = text.split("-")
    ranges.append((int(split_text[0]),int(split_text[1])))
result = 0
for number_range in ranges:
    print("*")
    for number in range(number_range[0],number_range[1]+1):
        number_string = str(number)
        divisors = sympy.divisors(len(number_string))
        divisors.reverse()
        for divisor in divisors[1:]:
            splitted_string=textwrap.wrap(number_string, divisor)
            invalid_number = True
            for index, substring in enumerate(splitted_string):
                if index+1 < len(splitted_string) and substring != splitted_string[index+1]:
                    invalid_number = False
                    break
            if invalid_number:
                result = result + number
                break
print(result)