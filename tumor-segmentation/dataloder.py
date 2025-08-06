import os
from os import listdir
from scipy import ndimage
import numpy as np
import cv2
import csv
import random

class Dataloder:
    
    def __init__(self, inpath, outpath):
        self.inpath = inpath
        self.outpath = outpath
                
    def HPconverter(self):
        inpath = self.inpath
        outpath = self.outpath

        if os.makedirs(outpath, exist_ok=True):
            print("Invalide output path")
        
        for filename in os.listdir(inpath):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                full_input_path = os.path.join(inpath, filename)

                # Les inn bilde
                img = cv2.imread(full_input_path, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    print(f"Kunne ikke lese {filename}")
                    continue

                # High-pass filter: original - blur + 127
                blurred = cv2.GaussianBlur(img, (21, 21), 3)
                hp = cv2.addWeighted(img, 1.0, blurred, -1.0, 127)

                # Lagre resultat
                full_output_path = os.path.join(outpath, filename)
                cv2.imwrite(full_output_path, hp)
    

    def convertToBitstrings(self, label=None):
        bitstrings = []

        for filename in os.listdir(self.outpath):
            if filename.lower().endswith((".png", ".jpg")):
                fullpath = os.path.join(self.outpath, filename)
                img = cv2.imread(fullpath, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    continue

                _, binary = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)
                bitstring = binary.flatten().tolist()

                if label is not None:
                    pic_value =  [label] + bitstring
                    bitstrings.append(pic_value)
                    
                else:
                    bitstrings.append([filename, bitstring])

        return bitstrings



                
               
    def sendToTXT(self, bitstrings, out_path):
        txt_filename = "HPNegativeBitstrings.txt"
        full_path = os.path.join(out_path, txt_filename)

        os.makedirs(out_path, exist_ok=True)

        with open(full_path, 'a') as txtfile:
            
            for entry in bitstrings:
                strEntry = str(entry)
                #label = str(entry)  # 0 eller 1
                #bits = ''.join(str(b) for b in entry)  # Lag streng av 0 og 1
                #line = label + bits  # Evt. label + "," + bits hvis du vil ha med label separat
                txtfile.write(strEntry)

            txtfile.write("\n")
        
        
    def dataShuflerForTXT(self, dataFilePath, pathToOutput, nameOfNewFile):
        # 1. Les alle linjer fra filen
        with open(dataFilePath, "r") as file:
            lines = file.readlines()

        # 2. Shuffle linjene
        random.shuffle(lines)

        full_path = os.path.join(pathToOutput, nameOfNewFile)
        
        # 3. Skriv dem til ny fil 
        with open(full_path, "w") as file:
            file.writelines(lines)

        print("Ferdig! Filen er shufflet.")
        
        

    def dataSplitter(self, data, out_path, out_name_train, out_name_val, out_name_test):
        
        with open(data, "r") as f:
            lines = f.readlines()
        random.shuffle(lines)

        # Beregn størrelser
        total = len(lines)
        train_size = int(total * 0.7)
        val_size = int(total * 0.15)
        test_size = total - train_size - val_size  # Tar med alt som gjenstår

        # Del opp i tre deler
        train_data = lines[:train_size]
        val_data = lines[train_size:train_size + val_size]
        test_data = lines[train_size + val_size:]

        
        full_path_train = os.path.join(out_path, out_name_train)
        full_path_val = os.path.join(out_path, out_name_val)
        full_path_test = os.path.join(out_path, out_name_test)
        
        
        # Skriv til egne filer
        with open(full_path_train, "w") as f:
            f.writelines(train_data)

        with open(full_path_val, "w") as f:
            f.writelines(val_data)

        with open(full_path_test, "w") as f:
            f.writelines(test_data)

        print(f"Ferdig! Split: {train_size} treningsdata, {val_size} validering, {test_size} test.")
