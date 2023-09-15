import cv2
import numpy as np


def shiftHue(image, percentage, increase=True):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # cv2.imshow("HSV", hsv)
    hue_channel = hsv[:, :, 0]
    mask = hue_channel * percentage
    if increase:
        hue_channel = np.clip(hue_channel + mask, 10, 255)
    else:
        hue_channel = np.clip(hue_channel - mask, 10, 255)

    hsv[:, :, 0] = hue_channel
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
