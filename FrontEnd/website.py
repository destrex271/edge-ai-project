import cv2
import streamlit as st

st.title("Webcam Live Feed")
text = ["Start" , "Stop"]
button_run = st.button('Start')
saturation  = st.slider('Saturation', 0, 100, 0, key='saturation')
hue         = st.slider('Hue', 0, 100, 0, key='hue')
Contrast    = st.slider('Contrast', 0, 100, 0, key='contrast')
brightness  = st.slider('Brightness', 0, 100, 0, key='brightness')
sharpen     = st.slider('Sharpen', 0, 100, 0, key='sharpen')
warmth      = st.slider('Warmth', 0, 100, 0, key='warmth')

button_stop = st.button('Stop')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

running = False

while True:
    if button_run:
        running = True
    if button_stop:
        running = False

    if running:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
    else:
        st.write('Stopped')
        break

camera.release()
