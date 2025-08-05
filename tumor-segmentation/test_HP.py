from dataloder import Dataloder



inPath = "../tumor-segmentation/data/patients/imgs"
outPath = "../tumor-segmentation/data/HP"


load_obj_imgtoHP = Dataloder(inPath, outPath)

load_obj_imgtoHP.HPconverter()        
               

bitStrings = load_obj_imgtoHP.convertToBitstrings(label=0)  #Her er lable = 0 asså bilder der pasienten ikke har kreft



#Eksempel på hvordan bilde navn og bit streng henger sammen
print(bitStrings[1][:25]) # Filnavn
print(len(bitStrings))
print(type(bitStrings))


txt_path = "../tumor-segmentation/data/"
#load_obj_imgtoHP.sendToCSV(bitStrings[1])
for i in range(len(bitStrings)):

    load_obj_imgtoHP.sendToTXT(bitStrings[i], txt_path)