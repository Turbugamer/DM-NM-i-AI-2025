import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models


class NN_Model():
    
    def load_data(self, filepath, target_len=None):
        labels = []
        features = []

        with open(filepath, 'r') as f:
            lines = [line.strip() for line in f if len(line.strip()) > 1]

        for line in lines:
            label = int(line[0])
            feature = [int(b) for b in line[1:]]
            labels.append(label)
            features.append(feature)

        # Finn maks lengde hvis ikke oppgitt
        if target_len is None:
            target_len = max(len(f) for f in features)

        # Pad alle til samme lengde
        padded_features = [f + [0] * (target_len - len(f)) for f in features]

        return np.array(padded_features), np.array(labels), target_len
    
    def runModel(self, X_train, y_train, X_val, y_val, X_test, y_test):
        model = models.Sequential([
        layers.Input(shape=(X_train.shape[1],)),
        layers.Dense(128, activation='relu'),
        layers.Dense(128, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')
        ])

        model.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy'])

        model.fit(X_train, y_train,
                epochs=20,
                batch_size=128,
                validation_data=(X_val, y_val))
        
        
        test_loss, test_acc = model.evaluate(X_test, y_test)
        print(f"Test accuracy: {test_acc:.2f}")
       
        model.save("../tumor-segmentation/ferdig_trent_model.h5")
       
        
    