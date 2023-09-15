import cv2
import numpy as np
from numba import jit, prange, uint8, float64, njit, vectorize


def saturation(image, percentage: float = 0, increase: bool = True):

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    saturation_channel = hsv[:, :, 1]
    mask = saturation_channel * percentage

    saturation_channel = mask
    if increase:
        saturation_channel = np.clip(saturation_channel + mask, 10, 255)
    else:
        saturation_channel = np.clip(saturation_channel - mask, 10, 255)

    hsv[:, :, 1] = saturation_channel
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


@njit(parallel=True)
def contrast(image, percentage: float=0):
    percentage = 255 * percentage
    factor = (259 * (percentage + 255))/(255*(259-percentage))
    result = np.zeros_like(image)
    for i in prange(0, len(image)):
        pixels = image[i]
        for j in prange(0, len(pixels)):
            pixel = pixels[j]
            pixel = np.clip((factor * (pixel - 128)) + 128, 0, 180)
            result[i][j] = pixel
            j += 1
        i += 1
    return result



