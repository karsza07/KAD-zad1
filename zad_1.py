import csv

flowersInTotal = 150
setosaTotal = 0
versicolorTotal = 0
virginicaTotal = 0

with open('data1.csv', 'r', encoding='utf-8') as plik:
    reader = csv.reader(plik, delimiter=',')
    for row in reader:
        number = row[-1]
        if number == "0":
            setosaTotal += 1
        elif number == "1":
            versicolorTotal += 1
        else:
            virginicaTotal += 1

print(" ")
print(setosaTotal, versicolorTotal, virginicaTotal)

setosaProcent = round(setosaTotal/flowersInTotal*100,1)
versicolorProcent = round(versicolorTotal/flowersInTotal*100,1)
virginicaProcent = round(virginicaTotal/flowersInTotal*100, 1)

print(setosaProcent, versicolorProcent, virginicaProcent)



