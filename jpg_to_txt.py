#Skrypt zamieniający obrazki w folderze na plik txt z wypisanymi jasnościami kolejnych pikseli. Wykorzystywany do przygotowania danych dla sieci neuronowej.

import os
from PIL import Image
import numpy as np
def save_brightness_to_text(images_directory, output_file):
    # Otwarcie pliku do zapisu
    with open(output_file, "w") as file:
        # Przechodzenie przez każdy obrazek w katalogu
        for filename in os.listdir(images_directory):
            if filename.endswith(".png"):
                # Ścieżka do obrazka
                image_path = os.path.join(images_directory, filename)
                first_three_chars = filename[:3]
                if first_three_chars == "000":
                    number = 0
                else:
                    number = int(first_three_chars)
                output_values = np.zeros(35, dtype=float)
                output_values[number] = 1.0
                # Otwarcie obrazka przy użyciu biblioteki PIL
                image = Image.open(image_path)

                # Konwersja do skali szarości, jeśli nie jest
                if image.mode != 'L':
                    image = image.convert('L')

                # Pobranie jasności pikseli
                pixels = list(image.getdata())

                # Zapisanie jasności do pliku tekstowego
                brightness_values = [f"{pixel / 255.0:.4f}" for pixel in pixels]
                file.write(";".join(brightness_values)+ ";" +";".join(map(str, output_values)) + "\n")
# Użycie funkcji z podanymi katalogiem obrazków i nazwą pliku wynikowego
#images_directory = "c:\\Users\\Maciek\\Desktop\\test\\test\\"
#output_file = "c:\\Users\\Maciek\\Desktop\\testing-E.txt"
images_directory = "c:\\Users\\Maciek\\Desktop\\train\\"
output_file = "c:\\Users\\Maciek\\Desktop\\training-E.txt"
save_brightness_to_text(images_directory, output_file)
