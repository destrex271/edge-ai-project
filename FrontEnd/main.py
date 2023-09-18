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


def on_press():
    print("OK")


p1, p2 = None, None
state = 0
def on_mouse(event, x, y, flags, userdata):
    global state, p1, p2
    # Left click
    if event == cv2.EVENT_LBUTTONUP:
        # Select first point
        if state == 0:
            p1 = (x,y)
            state += 1
        # Select second point
        elif state == 1:
            p2 = (x,y)
            state += 1

    # Right click (erase current ROI)
    if event == cv2.EVENT_RBUTTONUP:
        p1, p2 = None, None
        state = 0

# Register the mouse callback

windowName = "image"
cv2.namedWindow(windowName)
cv2.setMouseCallback(windowName, on_mouse)
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
    # print("HERE", sat_val)
    # if sat_val > 0:
    #     print("SAT")
    if state > 1:
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 1)
        width = p2[0] - p1[0]
        height = p2[1] - p1[1]
        region = frame[p1[1]:p1[1] + height,p1[0]:p1[0] + width,:]
        print(region)
        region = saturation(region, sat_val/100)
        region = warmth_change(region, warm_val/100 - 0.5)
        region = contrast(region, cont_val/100 - 0.5)
        region = increase_brightness(region, brgt_val/100 - 1)
        region = sharpenImage(region, (sharp_val/100))
        region = shiftHue(region, (hue_val/100) - 0.5)
        frame[p1[1]:p1[1] + height,p1[0]:p1[0] + width,:] = region
    cv2.imshow(windowName, frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cv2.destroyAllWindows()
