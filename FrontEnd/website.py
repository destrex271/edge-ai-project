import cv2
# import streamlit as st

# Import the utilities
from Face_Detection.ikshan import detect
from Rishabh.warmth import warmth_change
from Rishabh.brightness import increase_brightness
from satu_and_contrast.saturation import contrast, saturation
from Vishist.sharpen import sharpenImage
from Vishist.hueshift import shiftHue

video_feed = cv2.VideoCapture(0)
change = False
sat_val = 0
warm_val = 0
cont_val = 0
brgt_val = 0
sharp_val = 0
hue_val = 0


def on_saturation(v):
    global sat_val
    # change = True
    sat_val = v


def on_warmth(v):
    global warm_val
    # change = True
    warm_val = v


def on_contrast(v):
    global cont_val
    cont_val = v


def on_brgt(v):
    global brgt_val
    brgt_val = v


def on_sharpen(v):
    global sharp_val
    sharp_val = v


def on_hue(v):
    global hue_val
    hue_val = v







windowName = "image"
cv2.namedWindow(windowName)
cv2.createTrackbar('Saturation', windowName, 50, 100, on_saturation)
on_saturation(50)
cv2.createTrackbar('Warmth', windowName, 50, 100, on_warmth)
cv2.createTrackbar('Contrast', windowName, 50, 100, on_contrast)
cv2.createTrackbar('Brightness', windowName, 100, 200, on_brgt)
cv2.createTrackbar('Sharpen Image', windowName, 0, 100, on_sharpen)
cv2.createTrackbar('Hue', windowName, 50, 100, on_hue)
# cv2.createTrackbar('sensitivity', windowName, 0, 100, on_saturation)
# cv2.createTrackbar('sensitivity', windowName, 0, 100, on_saturation)

while True:
    _, frame = video_feed.read()
    # cv2.createTrackbar('slider', windowName, 0, 100, on_change)
    print("HERE", sat_val)
    # if sat_val > 0:
    #     print("SAT")
    frame = saturation(frame, sat_val/100)
    frame = warmth_change(frame, warm_val/100 - 0.5)
    frame = contrast(frame, cont_val/100 - 0.5)
    frame = increase_brightness(frame, brgt_val/100 - 1)
    frame = sharpenImage(frame, (sharp_val/100))
    frame = shiftHue(frame, (hue_val/100) - 0.5)
    cv2.imshow(windowName, frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cv2.destroyAllWindows()
