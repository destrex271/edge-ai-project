import cv2

def sharpenImage(image, multiplier):

    sharpened_image = cv2.Laplacian(image, cv2.CV_64F,ksize=1)

    # Convert the Laplacian result back to the uint8 data type
    sharpened_image=sharpened_image*multiplier
    sharpened_image = cv2.convertScaleAbs(sharpened_image)
    # Add the sharpened image to the original image
    sharpened_colored_image = cv2.add(image, sharpened_image)

    return sharpened_colored_image
