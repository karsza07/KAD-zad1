import csv
import matplotlib.pyplot as plt

#insertion sort - w3schools
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

def mediana(arr):
    insertionSort(arr)
    num = len(arr)
    if num % 2 != 0:
        return arr[(num-1)//2]
    else:
        return round((arr[(num-1)//2]+arr[num//2])/2, 2)

def dolnyKwartyl(arr):
    insertionSort(arr)
    num = len(arr)
    mid = num // 2
    return mediana(arr[0:mid])

def gornyKwartyl(arr):
    insertionSort(arr)
    num = len(arr)
    mid = num // 2

    if num %2 != 0:
        start = mid + 1
    else:
        start = mid

    return mediana(arr[start:])

def odchylenie(lista):
    n = len(lista)
    if n < 2:
        return 0.0
    sr = sum(lista) / n
    wariancja = sum((x - sr) ** 2 for x in lista) / (n - 1)
    return round(wariancja**0.5, 2)

def point2(arr, total):
    # 1. Długość działki kielicha
    print(" długość działki kielicha: ")
    print(
        f"minimum: {min(arr['Długość działki kielicha'])}, "
        f"średnia arytmetyczna: {round(sum(arr['Długość działki kielicha']) / total, 2)} "
        f"(±{odchylenie(arr['Długość działki kielicha'])})"
    )
    print(
        f"mediana: {mediana(arr['Długość działki kielicha'])}, "
        f"dolny kwartyl: {dolnyKwartyl(arr['Długość działki kielicha'])}, "
        f"gorny kwartyl: {gornyKwartyl(arr['Długość działki kielicha'])}, "
        f"maximum: {max(arr['Długość działki kielicha'])}\n"
    )

    # 2. Szerokość działki kielicha
    print(" szerokość działki kielicha: ")
    print(
        f"minimum: {min(arr['Szerokość działki kielicha'])}, "
        f"średnia arytmetyczna: {round(sum(arr['Szerokość działki kielicha']) / total, 2)} "
        f"(±{odchylenie(arr['Szerokość działki kielicha'])})"
    )
    print(
        f"mediana: {mediana(arr['Szerokość działki kielicha'])}, "
        f"dolny kwartyl: {dolnyKwartyl(arr['Szerokość działki kielicha'])}, "
        f"gorny kwartyl: {gornyKwartyl(arr['Szerokość działki kielicha'])}, "
        f"maximum: {max(arr['Szerokość działki kielicha'])}\n"
    )

    # 3. Długość płatka
    print(" długość płatka: ")
    print(
        f"minimum: {min(arr['Długość płatka'])}, "
        f"średnia arytmetyczna: {round(sum(arr['Długość płatka']) / total, 2)} "
        f"(±{odchylenie(arr['Długość płatka'])})"
    )
    print(
        f"mediana: {mediana(arr['Długość płatka'])}, "
        f"dolny kwartyl: {dolnyKwartyl(arr['Długość płatka'])}, "
        f"gorny kwartyl: {gornyKwartyl(arr['Długość płatka'])}, "
        f"maximum: {max(arr['Długość płatka'])}\n"
    )

    # 4. Szerokość płatka
    print(" szerokość płatka: ")
    print(
        f"minimum: {min(arr['Szerokość płatka'])}, "
        f"średnia arytmetyczna: {round(sum(arr['Szerokość płatka']) / total, 2)} "
        f"(±{odchylenie(arr['Szerokość płatka'])})"
    )
    print(
        f"mediana: {mediana(arr['Szerokość płatka'])}, "
        f"dolny kwartyl: {dolnyKwartyl(arr['Szerokość płatka'])}, "
        f"gorny kwartyl: {gornyKwartyl(arr['Szerokość płatka'])}, "
        f"maximum: {max(arr['Szerokość płatka'])}\n"
    )

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
print(" ")

#pkt 2
allData = {
    "Długość działki kielicha": (
            setosaData["Długość działki kielicha"]
            + versicolorData["Długość działki kielicha"]
            + virginicaData["Długość działki kielicha"]
    ),
    "Szerokość działki kielicha": (
            setosaData["Szerokość działki kielicha"]
            + versicolorData["Szerokość działki kielicha"]
            + virginicaData["Szerokość działki kielicha"]
    ),
    "Długość płatka": (
            setosaData["Długość płatka"]
            + versicolorData["Długość płatka"]
            + virginicaData["Długość płatka"]
    ),
    "Szerokość płatka": (
            setosaData["Szerokość płatka"]
            + versicolorData["Szerokość płatka"]
            + virginicaData["Szerokość płatka"]
    ),
}

print("dane łącznie dla wszystkich gatunków:")
point2(allData, flowersInTotal)

#zad3

#długośc działki kielicha histogram dla awszystkich kwiatów
dane = allData["Długość działki kielicha"]
bins = [4.0, 4.4, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0] #podziałka osi x
plt.xlabel("Długość  (cm)")
plt.ylabel("liczebność")
plt.ylim(0, 36) #zakres osi y
plt.title("Długość działki kielicha")
plt.hist(dane, bins, histtype='bar', edgecolor='black') # typ histogramu dane i kolor obwodu słupków
plt.show()

dane = allData["Szerokość działki kielicha"]
bins = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0] #podziałka osi x wyznaczona metoda prob i błędów poki nie znaleziono najlepszej reprezentacji danych
plt.xlabel("szerokość  (cm)")
plt.ylabel("liczebność")
plt.title("szerokość działki kielicha")
plt.hist(dane, bins, histtype='bar', edgecolor='black') # typ histogramu dane i kolor obwodu słupków
plt.ylim(0, 75) #zakres osi y
plt.show()