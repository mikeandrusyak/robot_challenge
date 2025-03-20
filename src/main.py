from zumi.zumi import Zumi
from zumi.util.screen import Screen
from zumi.util.vision import Vision 
from zumi.util.camera import Camera
from zumi.personality import Personality
import time

zumi = Zumi()
camera = Camera()
vision = Vision()
screen = Screen()
personality = Personality(zumi, screen)

def qr_code_command(message):
    if message == "Left Circle":
        for i in range(4):
            zumi.turn_left(90)
            zumi.line_follower(3)
    elif message == "Right Circle":
        for i in range(4):
            zumi.turn_right(90)
            zumi.line_follower(3)
    elif message == "Turn Left":
        zumi.turn_left(90)
    elif message == "Turn Right":
        zumi.turn_right(90)
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

def read_qr_code():
    camera.start_camera()
    frame = camera.capture()
    camera.close()
    qr_code = vision.find_QR_code(frame)
    message = vision.get_QR_message(qr_code)
    qr_code_command(message)

if __name__ == "__main__":
    while True:
        # Отримання даних з усіх ІЧ-сенсорів
        front_right, bottom_right, back_right, bottom_left, back_left, front_left = zumi.get_all_IR_data()
        
        # Налаштування порогу (чим менше значення, тим ближче об'єкт)
        threshold = 100 
        speed = 0.5
        # Логіка для виявлення можливих шляхів

        if bottom_left > threshold and bottom_right > threshold:
            zumi.line_follower(speed)
        else:
            zumi.turn_left(90)
            front_right, bottom_right, back_right, bottom_left, back_left, front_left = zumi.get_all_IR_data()
            if bottom_left > threshold and bottom_right > threshold:
                zumi.line_follower(speed)
            else:
                zumi.turn_right(180)
                front_right, bottom_right, back_right, bottom_left, back_left, front_left = zumi.get_all_IR_data()
                if bottom_left < threshold or bottom_right < threshold:
                    zumi.stop()
                    break

