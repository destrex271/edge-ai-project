import cv2
import numpy as np

image = cv2.imread("./hello.jpg")

image = cv2.resize(image, (900, 400))
print(image.shape)

value = input("Enter the degree of brightness increase: ")

cv2.imshow("Image", image)
cv2.waitKey(0)

# def gamma_corr(image, gamma):
#     invGamma = 1.0/gamma
#     table= np.array([((i/255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
#     return cv2.LUT(image, table)


# def log_transform(image, c):
#     table = np.array([(np.log((i/255.0)+1) * c) * 255 for i in np.arange(0, 256)]).astype("uint8")
#     return cv2.LUT(image, table)

# i_corr1 = gamma_corr(image, 1)
# i_corr2 = log_transform(image, 0.4)

# cv2.imshow('gamma', i_corr1)
# cv2.waitKey(0)
# cv2.imshow('log', i_corr2)
# cv2.waitKey(0)


def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

image = increase_brightness(image, 40)

cv2.imshow("Bright", image)
cv2.waitKey(0)