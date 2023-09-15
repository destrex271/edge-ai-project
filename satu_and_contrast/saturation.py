import cv2
import numpy as np


def saturation(image, percentage: float = 0, increase: bool = True):

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)
    saturation_channel = hsv[:, :, 1]
    mask = saturation_channel * percentage

    saturation_channel = mask
    if increase:
        saturation_channel = np.clip(saturation_channel + mask, 10, 255)
    else:
        saturation_channel = np.clip(saturation_channel - mask, 10, 255)

    hsv[:, :, 1] = saturation_channel
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
