#Skrypt do liczenia plików zaczynających się od danego ciągu znaków w zadanym katalogu.

import os

folder_path = "c:\\Users\\Maciek\\Desktop\\train\\"  # Zastąp to ścieżką do swojego folderu
folder_path1 = "c:\\Users\\Maciek\\Desktop\\test\\test\\"  # Zastąp to ścieżką do swojego folderu
output_file = "c:\\Users\\Maciek\\Desktop\\liczba_plikow.txt" 
# Inicjalizacja słownika do przechowywania liczby plików dla każdego numeru
counts = {}
counts1 = {}
# Przeszukiwanie plików w folderze
for filename in os.listdir(folder_path):
    if (filename.startswith("0") and filename[1:3].isdigit()):
        prefix = filename[:3]
        counts[prefix] = counts.get(prefix, 0) + 1

for filename in os.listdir(folder_path1):
    if (filename.startswith("0") and filename[1:3].isdigit()):
        prefix = filename[:3]
        counts1[prefix] = counts1.get(prefix, 0) + 1

# Zapisywanie wyników do pliku tekstowego
with open(output_file, 'w') as file:
    for prefix in sorted([f"{i:03}" for i in range(40)]):
        count = counts.get(prefix, 0)
        count1 = counts1.get(prefix, 0)
        file.write(f"{prefix}\t {count} \t {count1}\n")

print(f"Wyniki zostały zapisane do pliku: {output_file}")