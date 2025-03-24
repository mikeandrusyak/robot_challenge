from zumi.zumi import Zumi
from zumi.util.screen import Screen
from zumi.util.vision import Vision 
from zumi.util.camera import Camera
from zumi.personality import Personality
from zumi.protocol import Note # Note allows Zumi to play notes (music)

import pandas as pd
import time
from datetime import datetime

zumi = Zumi()
camera = Camera()
vision = Vision()
screen = Screen()
personality = Personality(zumi, screen)

number_of_objects = 0
log = {}

def line_correction(bottom_left, bottom_right, desired_angle, threshold):
    if bottom_left > threshold and bottom_right < threshold:
        desired_angle +=5
    elif bottom_left < threshold and bottom_right > threshold:
        desired_angle -=5
    return desired_angle

def turning_correction(desired_angle, turn_angle):
    if desired_angle >= -turn_angle if desired_angle<0 else turn_angle:
        desired_angle = -abs(turn_angle-abs(desired_angle))
    else:
        desired_angle = abs(turn_angle-abs(desired_angle))
    return desired_angle

def turn_to_check(turn):
    zumi.reset_gyro()
    if turn == 'left':
        zumi.turn_left(90)
    elif turn == 'right':
        zumi.turn_right(180)
    time.sleep(0.01)
    desired_angle = zumi.read_z_angle()
    return desired_angle

def move_after_turning(speed, desired_angle):
    zumi.reset_gyro() 
    for x in range(3):
        zumi.go_straight(speed, desired_angle)

def object_detected(threshold=100):
    front_right, bottom_right, back_right, bottom_left, back_left, front_left = zumi.get_all_IR_data() # Get center IR sensor value
    
    return front_right < threshold and front_left < threshold

def log_event(action):
    timestamp = datetime.now()
    log[action] = log.setdefault(action, [])
    log[action].append(timestamp)

def qr_code_command(message, number_of_objects):
    if message == "Left Circle":
        for j in range(number_of_objects):
            for i in range(4):
                zumi.turn_right(90)
                zumi.line_follower(3)
    elif message == "Right Circle":
        for j in range(number_of_objects):
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

def read_qr_code(number_of_objects):
    camera.start_camera()
    frame = camera.capture()
    camera.close()
    qr_code = vision.find_QR_code(frame)
    message = vision.get_QR_message(qr_code)
    qr_code_command(message, number_of_objects)
    return message

def line_correction(bottom_left, bottom_right, desired_angle, threshold):
    if bottom_left > threshold and bottom_right < threshold:
        desired_angle +=5
    elif bottom_left < threshold and bottom_right > threshold:
        desired_angle -=5
    return desired_angle

def turning_correction(desired_angle, turn_angle):
    if desired_angle >= -turn_angle if desired_angle<0 else turn_angle:
        desired_angle = -abs(turn_angle-abs(desired_angle))
    else:
        desired_angle = abs(turn_angle-abs(desired_angle))
    return desired_angle

def turn_to_check(turn):
    zumi.reset_gyro()
    if turn == 'left':
        zumi.turn_left(90)
    elif turn == 'right':
        zumi.turn_right(180)
    time.sleep(0.01)
    desired_angle = zumi.read_z_angle()
    return desired_angle

def move_after_turning(speed, desired_angle):
    zumi.reset_gyro() 
    for x in range(3):
        zumi.go_straight(speed, desired_angle)

def finish_with_180_turn():
    zumi.stop()
    log_event("finish")
    print("Reached end. Performing 180° turn.")
    screen.draw_text_center("Finisher box\nTurning 180°")
    zumi.turn_left(180)
    screen.draw_text_center("Done!")

def save_dict_to_csv(data_dict):
    # Generate file name with current time
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = f"output_{current_time}.csv"

    # Create empty list to store rows
    rows = []

    # Go through all actions and timestamps
    for action, timestamps in data_dict.items():
        for timestamp in timestamps:
            # Add row to list of rows
            rows.append({"timestamp": timestamp, "action": action})

    # Create DataFrame from list of rows
    df = pd.DataFrame(rows)

    # Sort DataFrame by column timestamp
    df = df.sort_values(by='timestamp')

    # Save DataFrame in CSV file
    df.to_csv(file_name, index=False)
    print("Data saved in ", file_name)

zumi.mpu.calibrate_MPU()
zumi.reset_gyro()
desired_angle = zumi.read_z_angle() 

log_event('start')
log_event('end_line')
try:
    while True:
        # Set the threshold for the IR sensors and the speed
        threshold = 50 
        speed = 5

        if object_detected():
            log_event('object_detected')
            number_of_objects += 1
            zumi.play_note(13, 500) # 13 is note type (1 - 60), 500 is duration in ms
            screen.draw_text_center(f"Objects: {number_of_objects}") # Display object count on screen
            # Wait until the object is removed
            print("Waiting for object to be removed...")
            while object_detected():
                zumi.stop()
                time.sleep(0.1)
            log_event('object_removed')
            print("Object removed. Resuming movement.")
            log_event('qr_code_read')
            message = read_qr_code(number_of_objects)
            log_event('qr_code_command: ' + message + " done")
            

        # Read all IR sensor values
        front_right, bottom_right, back_right, bottom_left, back_left, front_left = zumi.get_all_IR_data()

        # Correction to line if one sensor is on the line and the other is off
        desired_angle = line_correction(bottom_left, bottom_right, desired_angle, threshold)

        # Move forward with the corrected heading
        if bottom_left > threshold or bottom_right > threshold:
            zumi.go_straight(speed, desired_angle)
        else:
            log_event('end_line')
            
            if (log['end_line'][-1] - log['end_line'][-2]).total_seconds() > 3:
                go_left = True
            
                log_event('check_left')
                # Turn to check if left is line
                turned_left_angle = turn_to_check('left')

                # Calculate angle if turn was too much or not enough
                desired_angle = turning_correction(turned_left_angle, 90)

                front_right, bottom_right, back_right, bottom_left, back_left, front_left = zumi.get_all_IR_data()
            else:
                go_left = False
            if (bottom_left > threshold or bottom_right > threshold) and go_left:
                log_event('move_left')
                move_after_turning(speed, desired_angle)
            else:
                
                log_event('check_right')
                # Turn to check if right is line
                turned_right_angle = turn_to_check('right') 
                
                # Calculate angle if turn was too much or not enough
                desired_angle = turning_correction(turned_right_angle, 180)

                front_right, bottom_right, back_right, bottom_left, back_left, front_left = zumi.get_all_IR_data()

                if bottom_left > threshold or bottom_right > threshold:
                    log_event('move_right')
                    move_after_turning(speed, desired_angle)
                else:
                    zumi.stop()
                    finish_with_180_turn()
                    log_event('stop')
                    break
finally:
    zumi.stop()
    log_event('stop')
    save_dict_to_csv(log)