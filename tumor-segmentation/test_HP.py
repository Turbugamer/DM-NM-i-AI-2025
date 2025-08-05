from dataloder import Dataloder



inPath = "../tumor-segmentation/data/controls/imgs"
outPath = "../tumor-segmentation/data/HPC"


load_obj_imgtoHP = Dataloder(inPath, outPath)

load_obj_imgtoHP.HPconverter()        
               

bitStrings = load_obj_imgtoHP.convertToBitstrings(label=0)  #Her er lable = 1 asså bilder der pasienten har kreft




txt_path = "../tumor-segmentation/data/"

for i in range(len(bitStrings)):

    load_obj_imgtoHP.sendToTXT(bitStrings[i], txt_path)
    
    
print("Alt i orden")