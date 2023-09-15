import cv2
import numpy as np
# import os

def change_warmth(image, value):
    green_param = 0.6
    if value == 0:
        return image
    image_red = image[:, :, 2]
    image_green = image[:, :, 1]

    flag = 0

    if value < 0:
        flag = 1
        green_param = 0.4

    value = abs(value)
    val_green = np.uint8(value * green_param) 
    mod_image = np.zeros_like(image)

    #value can be positive or negative

    if flag == 0:
        image_red[image_red < 255 - value] += value 
        image_red[image_red >= 255 - value] = 255
        image_green[image_green < 255 - val_green] += val_green 
        image_green[image_green >= 255 - val_green] = 255
    else:
        image_red[image_red > value] -= value 
        image_red[image_red <= value] = 0
        image_green[image_green > val_green] -= val_green 
        image_green[image_green <= val_green] = 0

    mod_image[:, :, 0] = image[:, :, 0]
    mod_image[:, :, 1] = image_green
    mod_image[:, :, 2] = image_red
    return mod_image
    

# print("We are currently in pwd:", os.getcwd())
image = cv2.imread("./hello.jpg")
image = cv2.resize(image, (800, 600))

#Range of value - [-50, 50]
value = 50

if image is None:
    print("Image was not loaded successfully!!")
    exit(0)

cv2.imshow("Original Image", image)

warm_image = change_warmth(image, value)

cv2.imshow("Warmth changed", warm_image)
cv2.waitKey(0)

cv2.destroyAllWindows()