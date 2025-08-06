from NN_Model import NN_Model



load_obj_NN = NN_Model()


trainingData = "../tumor-segmentation/data/TrainSet.txt"
valData = "../tumor-segmentation/data/ValSet.txt"
testData = "../tumor-segmentation/data/TestSet.txt"

# Last inn treningsdata og få target_len
X_train, y_train, target_len = load_obj_NN.load_data(trainingData)
print(target_len) #396400

# Bruk samme target_len for validering og test
X_val, y_val, _   = load_obj_NN.load_data(valData, target_len)
X_test, y_test, _ = load_obj_NN.load_data(testData, target_len)

print("All data lastet inn")

load_obj_NN.runModel(X_train, y_train, X_val, y_val, X_test, y_test)


