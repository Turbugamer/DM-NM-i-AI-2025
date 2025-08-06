from dataloder import Dataloder



inPath = "../tumor-segmentation/data/controls/imgs"
outPath = "../tumor-segmentation/data/HPC"


load_obj_imgtoHP = Dataloder(inPath, outPath)


allData = "../tumor-segmentation/data/FullHP.txt"

dataLocation = "../tumor-segmentation/data"
shuffleDataName = "ShuffledData.txt"

#load_obj_imgtoHP.dataShuflerForTXT(allData, dataLocation, shuffleDataName)

allShuffledData = "../tumor-segmentation/data/ShuffledData.txt"


trainDataName = "TrainSet.txt"
valDataName = "ValSet.txt"
testDataName = "TestSet.txt"


#load_obj_imgtoHP.dataSplitter(allShuffledData, dataLocation, trainDataName, valDataName, testDataName)
# Meldingen som ble vist etter at linjen over ble kjørt : 
#       Ferdig! Split: 425 treningsdata, 91 validering, 92 test. = 608 bilder totalt