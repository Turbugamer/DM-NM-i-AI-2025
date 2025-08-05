from dataloder import Dataloder



inPath = "../tumor-segmentation/data/patients/imgs"
outPath = "../tumor-segmentation/data/HP"


load_obj_imgtoHP = Dataloder(inPath, outPath)

load_obj_imgtoHP.HPconverter()        
               

bitStrings = load_obj_imgtoHP.convertToBitstrings(label=0)  #Her er lable = 0 asså bilder der pasienten ikke har kreft

#Eksempel på hvordan bilde navn og bit streng henger sammen
print(bitStrings[0][0]) # Filnavn
print(bitStrings[0][1][:100]) # Første 100 bits