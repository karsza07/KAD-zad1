import csv

# pkt 1
flowersInTotal = 150
setosaTotal = 0
versicolorTotal = 0
virginicaTotal = 0

setosaData = {
    "Długość działki kielicha": [],
    "Szerokość działki kielicha": [],
    "Długość płatka": [],
    "Szerokość płatka": []
}

versicolorData = {
    "Długość działki kielicha": [],
    "Szerokość działki kielicha": [],
    "Długość płatka": [],
    "Szerokość płatka": []
}

virginicaData = {
    "Długość działki kielicha": [],
    "Szerokość działki kielicha": [],
    "Długość płatka": [],
    "Szerokość płatka": []
}

with open("data1.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        number = row[-1].strip()
        if number == "0":
            setosaData["Długość działki kielicha"].append(float(row[0]))
            setosaData["Szerokość działki kielicha"].append(float(row[1]))
            setosaData["Długość płatka"].append(float(row[2]))
            setosaData["Szerokość płatka"].append(float(row[3]))
        elif number == "1":
            versicolorData["Długość działki kielicha"].append(float(row[0]))
            versicolorData["Szerokość działki kielicha"].append(float(row[1]))
            versicolorData["Długość płatka"].append(float(row[2]))
            versicolorData["Szerokość płatka"].append(float(row[3]))
        elif number == "2":
            virginicaData["Długość działki kielicha"].append(float(row[0]))
            virginicaData["Szerokość działki kielicha"].append(float(row[1]))
            virginicaData["Długość płatka"].append(float(row[2]))
            virginicaData["Szerokość płatka"].append(float(row[3]))

setosaTotal = len(setosaData["Długość działki kielicha"])
versicolorTotal = len(versicolorData["Długość działki kielicha"])
virginicaTotal = len(virginicaData["Długość działki kielicha"])

setosaProcent = round(setosaTotal / flowersInTotal * 100, 1)
versicolorProcent = round(versicolorTotal / flowersInTotal * 100, 1)
virginicaProcent = round(virginicaTotal / flowersInTotal * 100, 1)

print("")
print(f"Liczebności: Setosa: {setosaTotal}, Versicolor: {versicolorTotal}, Virginica: {virginicaTotal}")
print(f"Udzialy (%): Setosa: {setosaProcent}%, Versicolor: {versicolorProcent}%, Virginica: {virginicaProcent}%")