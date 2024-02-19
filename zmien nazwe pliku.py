#Skrypt do masowej zmiany nazw plików które zaczynają się określoną sekwencją znaków.

import os

def zmien_nazwe_pliku(nazwa_pliku):
    nowa_nazwa = "034" + nazwa_pliku[3:]
    return nowa_nazwa

def zmien_pierwsze_trzy_znaki(folder):
    for nazwa_pliku in os.listdir(folder):
        if nazwa_pliku.startswith("035"):
            stara_sciezka = os.path.join(folder, nazwa_pliku)
            nowa_nazwa = zmien_nazwe_pliku(nazwa_pliku)
            nowa_sciezka = os.path.join(folder, nowa_nazwa)
            os.rename(stara_sciezka, nowa_sciezka)
            print(f"Zmieniono nazwę pliku: {stara_sciezka} -> {nowa_sciezka}")

folder = "c:\\Users\\Maciek\\Desktop\\train\\"  # Zastąp to ścieżką do swojego folderu
folder1 = "c:\\Users\\Maciek\\Desktop\\test\\test\\"  # Zastąp to ścieżką do swojego folderu        
zmien_pierwsze_trzy_znaki(folder)
zmien_pierwsze_trzy_znaki(folder1)