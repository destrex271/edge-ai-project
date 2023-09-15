import cv2
import numpy as np
import copy

"""

def change_warmth(orig, value):
    image = copy.deepcopy(orig)
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

    image[:, :, 1] = image_green
    image[:, :, 2] = image_red
    return image

"""

def warmth_change(orig, percent = 0.3):
    image = copy.deepcopy(orig)
    if percent == 0:
        return image
    green_param = 0.8 * percent
    image_red = image[:, :, 2]
    image_green = image[:, :, 1]

    mask_red = image_red * percent
    mask_green = image_green * green_param

    image[:, :, 2] = np.clip(image_red + mask_red, 10, 255)
    image[:, :, 1] = np.clip(image_green + mask_green, 10, 255)

    return image

image = cv2.imread("./hello1.jpeg")
image = cv2.resize(image, (800, 600))

#Range of percent - [-0.5, 0.5]
value, percent = 50, 0.4


if image is None:
    print("Image was not loaded successfully!!")
    exit(0)

cv2.imshow("Original Image", image)

"""

warm_image = change_warmth(image, value)

cv2.imshow("Warmth changed using absolute value", warm_image)
cv2.waitKey(0)

"""

warm_image1 = warmth_change(image, percent)

cv2.imshow("Warmth changed using percent", warm_image1)
cv2.waitKey(0)

cv2.destroyAllWindows()