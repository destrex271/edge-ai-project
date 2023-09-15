import cv2
import numpy as np


def increase_brightness(image, percent = 0.3):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    v = hsv[:, :, 2]

    mask = v * percent

    hsv[:, :, 2] = np.clip(mask + v, 10, 255)

    image_mod = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return image_mod

image = cv2.imread("./hello.jpeg")
if image is None:
    print("Image could not be loaded successfully!!")
    exit(0)

#Range of change is [-0.8, 0.8]
percent_change = 0.8
image = cv2.resize(image, (850, 600))

cv2.imshow("Image", image)
cv2.waitKey(0)

image = increase_brightness(image, percent_change)

cv2.imshow("Bright", image)
cv2.waitKey(0)