from zumi.zumi import Zumi
from zumi.util.screen import Screen
import time
from datetime import datetime
from zumi.util.vision import Vision
from zumi.util.camera import Camera 
from zumi.personality import Personality
import cv2
import moving_functions as mf


zumi =    Zumi()
camera    = Camera()
screen    = Screen()
vision    = Vision()
personality = Personality(zumi, screen)

def face_detection(zumi, camera, screen, vision):
    camera.start_camera()
    captured_picture = camera.capture()
    captured_picture = vision.convert_to_gray(captured_picture) 
    camera.close()
    # screen.show_image(captured_picture) #used to check whether the picture of the face was in frame of the captured picture
    if vision.find_face(captured_picture)==None:
        screen.draw_text_center("No Face Detected!")
        screen.show_image(captured_picture)
        cv2.imwrite("Picture_Taken.png", captured_picture)
        print("image1")
        camera.show_image(captured_picture)
        return captured_picture
    else:
        screen.draw_text_center("Face Detected!")
        zumi.play_note(40, 500)
        return None   
    time.sleep(1)

def qr_code_command(zumi, personality, message, speed, number_of_objects, threshold):
    if message == "Left Circle":
        mf.circle('left', speed, number_of_objects, threshold)
    elif message == "Right Circle":
        mf.circle('right', speed, number_of_objects, threshold)
    elif message == "Turn Left":
        zumi.signal_left_on()
        zumi.turn_left(90)
        zumi.signal_left_off()
    elif message == "Turn Right":
        zumi.signal_right_on()
        zumi.turn_right(90)
        zumi.signal_right_off()
    elif message == "Stop":
        zumi.stop()
    elif message == "Zumi is happy today!":
        personality.happy()
    elif message == "Zumi is angry today!":
        personality.angry()
    elif message == "Zumi is celebrating today!":
        personality.celebrate()
    else:
        print("Invalid command")

def read_qr_code(camera, screen, vision, speed, number_of_objects, threshold):
    camera.start_camera()
    frame = camera.capture()
    screen.show_image(frame) #to make sure qr-code is in frame of picture
    camera.close()
    qr_code = vision.find_QR_code(frame)
    message = vision.get_QR_message(qr_code)
    qr_code_command(message, speed, number_of_objects, threshold)
    return message