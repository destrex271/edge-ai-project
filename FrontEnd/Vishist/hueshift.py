import cv2
import numpy as np

def shiftHue(degrees):
    image = cv2.imread('sudoku.jpeg')
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Get the hue, saturation, and value channels
    h, s, v = cv2.split(hsv_image)

    # Shift the hue by 30 degrees
    h_shifted = h + degrees

    # Clip the hue values to be between 0 and 180 degrees
    h_shifted = np.clip(h_shifted, 0, 180)

    # Create a new HSV image with the shifted hue values
    hsv_shifted = cv2.merge([h_shifted, s, v])

    # Convert the HSV image back to RGB color space
    image_shifted = cv2.cvtColor(hsv_shifted, cv2.COLOR_HSV2BGR)

    # Display the original and shifted images
    cv2.imshow('Original image', image)
    cv2.imshow('Shifted image', image_shifted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

shiftHue(180)