from scipy import ndimage
import numpy as np
import os
import cv2

def main():
    inPath = "../tumor-segmentation/data/patients/imgs"
    outPath = "../tumor-segmentation/data/HP"

    # Sørg for at output-mappen finnes
    os.makedirs(outPath, exist_ok=True)

    for filename in os.listdir(inPath):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            full_input_path = os.path.join(inPath, filename)

            # Les inn bilde
            img = cv2.imread(full_input_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                print(f"Kunne ikke lese {filename}")
                continue

            # High-pass filter: original - blur + 127
            blurred = cv2.GaussianBlur(img, (21, 21), 3)
            hp = cv2.addWeighted(img, 1.0, blurred, -1.0, 127)

            # Lagre resultat
            full_output_path = os.path.join(outPath, filename)
            cv2.imwrite(full_output_path, hp)

if __name__ == '__main__':
    main()
