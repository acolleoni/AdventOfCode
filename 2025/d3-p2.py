file = open('input-3.txt', 'r')
lines = file.readlines()

DIGITS_NUMBER = 12

result = 0
for line in lines:
    line = line.strip()
    number_dispositions = [[] for _ in range(10)]
    for index, number in enumerate(line.strip()):
        number_dispositions[int(number)].append(index)
    
    #per ogni cifra da 9 a 0 (digit)
    line_number = ''
    digit = 9
    position_index = 0
    last_digit_found_position = -1
    #finche' non abbiamo composto le 12 cifre
    while len(line_number) < DIGITS_NUMBER:
        #se ci sono ancora occorrenze della cifra da analizzare
        if position_index < len(number_dispositions[digit]):
            #se la posizione di questa occorrenza di questa cifra e' in pos. minore dell'ultima trovata
            if number_dispositions[digit][position_index] <= last_digit_found_position:
                position_index +=1
                continue
            #se la lunghezza della sottostringa successiva all'occorrenza che stiamo analizzando del digit e' > 12
            if len(line[number_dispositions[digit][position_index]:]) >= (DIGITS_NUMBER - len(line_number)):
                line_number += str(digit)
                last_digit_found_position = number_dispositions[digit][position_index]
                position_index = 0
                digit = 9
            else:
                digit -= 1
                position_index = 0
        #se sono arrivato a fine occorrenze di una cifra, passo alla cifra successiva da controllare
        else:
            digit -= 1
            position_index = 0
    result += int(line_number)
print(result)