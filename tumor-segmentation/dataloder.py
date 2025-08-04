import os
from os import listdir


class Dataloder:
    
    def __init__(self, dir):
        self.dir = dir    
    
    def loadalldata(self):
        folder_dir = self.dir
        print(len(folder_dir))
        print(type(folder_dir))
        
        for images in os.listdir(folder_dir):
        # check if the image ends with png
            if (images.endswith(".png")):
                print(images)
                