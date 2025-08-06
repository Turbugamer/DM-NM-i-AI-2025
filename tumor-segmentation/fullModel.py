import tensorflow as tf
import numpy as np
import cv2

MODEL_PATH = "../tumor-segmentation/ferdig_trent_model.h5"
TARGET_LEN = 396400  # fra treningsdata
model = tf.keras.models.load_model(MODEL_PATH)

def get_threshold_segmentation(img: np.ndarray, threshold: int) -> np.ndarray:
    # Ignorer threshold, vi bruker modellen isteden

    # High-pass filter (samme som i treningen)
    blurred = cv2.GaussianBlur(img, (21, 21), 3)
    hp = cv2.addWeighted(img, 1.0, blurred, -1.0, 127)

    # Binariser og gjør om til 1D bitstring
    _, binary = cv2.threshold(hp, 127, 1, cv2.THRESH_BINARY)
    bitstring = binary.flatten().tolist()

    # Pad til TARGET_LEN
    if len(bitstring) < TARGET_LEN:
        bitstring += [0] * (TARGET_LEN - len(bitstring))
    elif len(bitstring) > TARGET_LEN:
        bitstring = bitstring[:TARGET_LEN]

    # Modell input må være 2D
    input_array = np.array([bitstring])

    # Modell prediksjon
    prediction = model.predict(input_array)[0][0]

    # Returnér maske basert på prediksjon
    if prediction > 0.5:
        white_mask = np.ones_like(img, dtype=np.uint8) * 255
        return np.stack([white_mask]*3, axis=-1)# "Kreft"
    else:
        black_mask = np.zeros_like(img, dtype=np.uint8)
        return np.stack([black_mask]*3, axis=-1)