import cv2
import numpy as np


def increase_brightness(image, percent = 0.3):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    v = hsv[:, :, 2]

    mask = v * percent

    hsv[:, :, 2] = np.clip(mask + v, 10, 255)

    image_mod = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return image_mod
