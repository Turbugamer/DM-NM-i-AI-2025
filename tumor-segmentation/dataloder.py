import os
from os import listdir
from scipy import ndimage
import numpy as np
import cv2


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
    

    def convertToBitstrings(self):
        
        bitstrings = []
        
        for filename in os.listdir(self.outpath):
            if filename.endswith(".png") or filename.endswith(".jpg"):
                fullpath = os.path.join(self.outpath, filename)
                img = cv2.imread(fullpath, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    continue

                # Terskel: binært bilde
                _, binary = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)
                bitstring = binary.flatten().tolist()

                bitstrings.append([filename, bitstring])

        return bitstrings

               

