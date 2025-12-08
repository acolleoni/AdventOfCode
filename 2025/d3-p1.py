file = open('input3.txt', 'r')
lines = file.readlines()

result = 0
for line in lines:
    number_dispositions = [[] for _ in range(10)]
    for index, number in enumerate(line.strip()):
        number_dispositions[int(number)].append(index)
    decina_position = -1
    decina_value = -1
    unita_value=-1
    #per ogni cifra da 9 a 0 (digit)
    for digit in reversed(range(10)):
        #se non ho ancora un numero in saccoccia (decina o unita)
        if decina_position == -1 and unita_value == -1:
            #se ho due numeri della cifra piu' alta li accoppio e formo un numero vincente
            if len(number_dispositions[digit]) > 1:
                result = result + digit * 10 + digit
                break
            #se ho un solo numero della cifra piu' alta lo metto in saccoccia
            elif len(number_dispositions[digit]) == 1:
                if number_dispositions[digit][0] == len(line)-2:
                    unita_value = digit
                else:
                    decina_position = number_dispositions[digit][0]
                    decina_value = digit
        #se ho un numero in saccoccia
        else:
            #se per la digit che sto verificando ora e' presente
            if len(number_dispositions[digit]) != 0:
                #se avevo trovato una unita', questo numero e' la decina
                if unita_value != -1:
                    result = result + digit * 10 + unita_value
                    break
                #se avevo trovato una decina, questo numero e' l'unita'
                if number_dispositions[digit][-1] > decina_position:
                    result = result + decina_value * 10 + digit
                    break

print(result)