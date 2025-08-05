import os
from os import listdir
from scipy import ndimage
import numpy as np
import cv2
import csv


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




    def sendToCSV(self, bitstrings):
        
        csvFileName = "HPBitstrings.csv"
        
        with open("../tumor-segmentation/data/" + csvFileName, 'w', newline='') as csvfile:
            
            csv_writer = csv.writer(csvfile)

            print(type(bitstrings))
            print(len(bitstrings))
            
            csv_writer.writerow(bitstrings)
            
        print(f"Data successfully written to {"../tumor-segmentation/data/" + csvFileName}")
                
               
    def sendToTXT(self, bitstrings, out_path):
        txt_filename = "HPBitstrings.txt"
        full_path = os.path.join(out_path, txt_filename)

        os.makedirs(out_path, exist_ok=True)

        with open(full_path, 'w') as txtfile:
            for entry in bitstrings:
                label = str(entry)  # 0 eller 1
                bits = ''.join(str(b) for b in entry)  # Lag streng av 0 og 1
                line = label + bits  # Evt. label + "," + bits hvis du vil ha med label separat
                txtfile.write(entry + '\n')

        print(f"✅ Bitstrings written to {full_path} without commas.")
