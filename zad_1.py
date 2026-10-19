import csv
import matplotlib.pyplot as plt
import math #do liczenia sumy itd
import itertools #d iterowania wydajnie

def mediana(arr):
    s=sorted(arr)
    num = len(s)
    if num % 2 != 0:
        return s[(num-1)//2] #zwraca środkową wartośc
    else:
        return round((s[(num-1)//2]+s[num//2])/2, 2) #srednia środkowych wartości jesli parzyste

def dolnyKwartyl(arr):
    s=sorted(arr)
    mid = len(s) // 2
    return mediana(s[0:mid]) #mediana dolnej połowy

def gornyKwartyl(arr):
    s=sorted(arr)
    num = len(s)
    mid = num // 2
    if num %2 != 0:
        start = mid + 1
    else:
        start = mid

    return mediana(s[start:]) #mediana górnej połowy

def odchylenie(lista):
    n = len(lista)
    if n < 2: #jak ma mniej niz 2 elementy nie mozna obliczyc odchylenia
        return 0.0
    sr = sum(lista) / n
    wariancja = sum((x - sr) ** 2 for x in lista) / (n - 1) #suma kwadroatów różnucy kazddego elemnetu od sredniej podzielone na n-1 elementow
    return round(wariancja**0.5, 2) #pierwiastek z wariancji to dochylenie, zaokrąglenie do dwóch miejsc po przecinku

#to jest do przepisania do sprawka
def point2(arr, total):
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

def korelacja_pearsona(x, y):
    n = len(x) #liczba punktów pomiarowych
    sr_x = sum(x) / n
    sr_y = sum(y) / n #srednie arytemtyczne dla obu wartosci
    licznik = sum((xi - sr_x) * (yi - sr_y) for xi, yi in zip(x, y)) #suma iloczynow odchylen punktow od sredniej
    mianownik = math.sqrt(sum((xi - sr_x)**2 for xi in x) * sum((yi - sr_y)**2 for yi in y)) #iloczyn sum kwadratów odchyleń pod pierwiastkiem
    return licznik / mianownik if mianownik != 0 else 0.0

def regresja_liniowa(x, y): #obliczanie wwspolczynnikow
    n = len(x)
    sr_x = sum(x) / n
    sr_y = sum(y) / n
    licznik = sum((xi - sr_x) * (yi - sr_y) for xi, yi in zip(x, y)) # to amo co w korelacji
    mianownik = sum((xi - sr_x)**2 for xi in x) #oblicza sumę kwadratów odchyleń zmiennej x od jej średniej
    a = licznik / mianownik #wspolczynnik a
    b = sr_y - a * sr_x #wspolczynnik b
    return a, b

flowersInTotal = 150
setosaTotal = 0
versicolorTotal = 0
virginicaTotal = 0

setosaData = {  #utworzenie słowników
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

#import ddanuch do słownika
with open("data1.csv", "r") as f: #otiwera plik w trybie do oczty jako f
    reader = csv.reader(f) #dzieli każda linie na kolumny do odczytania
    for row in reader: #dla każdej kolumny w rzędzie
        number = row[-1].strip()  #sprawdza numer odpowiadający gatunkowi
        if number == "0":
            setosaData["Długość działki kielicha"].append(float(row[0])) #odpowiednie wartości trafiają do odpowiednich kluczy
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

setosaProcent = round(setosaTotal / flowersInTotal * 100, 1) #wartości procentowe
versicolorProcent = round(versicolorTotal / flowersInTotal * 100, 1)
virginicaProcent = round(virginicaTotal / flowersInTotal * 100, 1)

print("")
print(f"Liczebności: Setosa: {setosaTotal}, Versicolor: {versicolorTotal}, Virginica: {virginicaTotal}")
print(f"Udzialy (%): Setosa: {setosaProcent}%, Versicolor: {versicolorProcent}%, Virginica: {virginicaProcent}%")
print(" ")


allData = { #słownik zawierający wszystko
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


#wczesniej tutaj byl kazdy wykres rysowany osobno stad wiadomo jakie są najlepsze podziałki dla wykresów
#teraz jest jedna pętla dla każdego histogramu
konfiguracja_cech= [ #dane dla wykresów, tablica słowników
    {
        #"Nazwa":"Długość działki kielicha",
        "Klucz":"Długość działki kielicha",
        "Jednostka":"Długość",
        "podzialki":[4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0],
        "hist":(0,36),
        "box":(4,8)
    },
    {
        #"Nazwa":"Szerokość działki kielicha",
        "Klucz":"Szerokość działki kielicha",
        "Jednostka":"Szerokość",
        "podzialki":[2.0,2.5,3.0,3.5,4.0,4.5],
        "hist":(0,75),
        "box":(1.8,4.6)        
    },
    {
        #"Nazwa": "Długość płatka", nazwa jest taka sama jak klucz??? po co jest nazwa?
        "Klucz": "Długość płatka",
        "Jednostka": "Długość",
        "podzialki": [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0],
        "hist": (0, 32),
        "box": (0.8, 7.2)
    },
    {
        #"Nazwa": "Szerokość płatka",
        "Klucz": "Szerokość płatka",
        "Jednostka": "Szerokość",
        "podzialki": [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6],
        "hist": (0, 42),
        "box": (0.0, 2.7)
    }
]
#histogramy i pudełkowe

gatunki_etykiety = ["setosa", "versicolor", "virginica"]
fig1,axes1=plt.subplots(nrows=4,ncols=2,figsize=(10,14)) #tworzenie siatki do rysowania wykresów 4 rzedy 2 kolumny, rozmiar całego okna to 10 na 14 (w calach)
plt.subplots_adjust(hspace=0.45,wspace=0.25) #odległosci miedzy kolejnymi wykresami na siatce
for i,cfg in enumerate(konfiguracja_cech):
    ax_hist=axes1[i,0] #wykres z wiersza i kolumny 0, miejsce dla hisotgramu
    ax_box=axes1[i,1] #wykres z wiersza i kolumny 1, miejse dla pudełkowego
    klucz = cfg["Klucz"]

    #tworzenie histogramu
    ax_hist.hist(allData[klucz], bins=cfg["podzialki"], edgecolor='black') #rysowanie histogramu dla danych z tablicy, bins to podziałki
    ax_hist.set_title(cfg["Klucz"]) #ustawienie tytułu
    ax_hist.set_xlabel(cfg["Jednostka"]) #label dla osi x
    ax_hist.set_ylabel("Liczebność")  #label dla osi y
    ax_hist.set_ylim(cfg["hist"]) #zakres osi pionowej y

    #tworzenie wykresów pudełkowych
    pudelka = [
        setosaData[klucz], #trzy zbiory, jeden dla każdego gatunku
        versicolorData[klucz],
        virginicaData[klucz]
    ]


    ax_box.boxplot(pudelka, tick_labels=gatunki_etykiety) #rysuje wykres dla danych z tabeli, ustawia etykiety pod pudelkami
    ax_box.set_title(cfg["Klucz"]) #ustawienie tytułu
    ax_box.set_xlabel("Gatunek") #label dla osi x
    ax_box.set_ylabel(cfg["Jednostka"]) #label dla osi y
    ax_box.set_ylim(cfg["box"]) #zakres osi y

plt.savefig("wykres_zad3.png", dpi=300, bbox_inches='tight')
plt.show()

#reszta wykresow
pary_cech = list(itertools.combinations([c["Klucz"] for c in konfiguracja_cech], 2)) #wszystkie możliwe pary cech
fig2, axes2 = plt.subplots(nrows=3, ncols=2, figsize=(12, 15)) #ustawienie pól dla wszystkich wykresów
axes2 = axes2.flatten() #przekształca macierz wykresów w jednowymiarową liste
plt.subplots_adjust(hspace=0.45, wspace=0.3)
for idx, (cecha_x, cecha_y) in enumerate(pary_cech):
    ax = axes2[idx] #wybieranie pola na wykres
    x = allData[cecha_x] #seria danych z allData dla osi x
    y = allData[cecha_y] #seria danych z all data dla osi y
    r = korelacja_pearsona(x, y)
    a, b = regresja_liniowa(x, y)
    ax.scatter(x, y, color='blue', edgecolors='black', alpha=0.6, label='Pomiary') #rysowanie punktów danych, o przezroczystosci 0.6
    x_min, x_max = min(x), max(x) #skrajne wartości osi x
    ax.plot([x_min, x_max], [a * x_min + b, a * x_max + b], color='red', linewidth=2, label='Regresja') #rysuje prosta regresji
    #poczatek to xmin, koniec to x max, y jest obliczany za pomocą współczynników  z funkcji wyżej
    znak = "+" if b >= 0 else "-"  #ustawianie znaku dla regresji liniowej
    ax.set_title(f"r = {r:.2f}, y = {a:.1f}x {znak} {abs(b):.1f}", fontsize=11, fontweight='bold')
    ax.set_xlabel(f"{cecha_x} (cm)", fontsize=9)
    ax.set_ylabel(f"{cecha_y} (cm)", fontsize=9)
    ax.grid(True, linestyle='--', alpha=0.6) #siatka półprzezroczysta dla łatwiejszego odczytania danych
    ax.legend(loc='upper left', fontsize=8) #legenda w lewym górnym rogu

plt.savefig("wykres_zad4.png", dpi=300, bbox_inches='tight')
plt.show()
