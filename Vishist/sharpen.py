import cv2

def sharpenImage(multiplier):
    multiplier=(1.5/100)*multiplier
    image = cv2.imread('sudoku.jpeg')

    # Check if the image was loaded successfully
    if image is None:
        print("Error: Could not load the image.")
    else:
        # Apply the Laplacian filter to the image for sharpening
        sharpened_image = cv2.Laplacian(image, cv2.CV_64F,ksize=1)

        # Convert the Laplacian result back to the uint8 data type
        sharpened_image=sharpened_image*multiplier
        sharpened_image = cv2.convertScaleAbs(sharpened_image)
        # Add the sharpened image to the original image
        sharpened_colored_image = cv2.add(image, sharpened_image)

        # Display the original, sharpened, and sharpened colored images
        cv2.imshow('Original Image', image)
        # cv2.imshow('Sharpened Image', sharpened_image)
        cv2.imshow('Sharpened Colored Image', sharpened_colored_image)

        # Wait for a key press and close the windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()


sharpenImage(100)