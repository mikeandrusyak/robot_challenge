from zumi.zumi import Zumi
from zumi.protocol import Note # allows Zumi to play notes (music)
import time


zumi = Zumi()


# basic IR Object Detection and Stop
# This code will make Zumi stop if an object is detected in front of it using the center IR sensor.

def object_detected(threshold=100):
    """
    Checks if an object is directly in front of Zumi using the center IR sensor.
    
    Args:
    - threshold (int): Sensor value above which an object is considered detected.
    
    Returns:
    - bool: True if an object is detected ahead, False otherwise.
    """
    front_center = zumi.get_all_IR_data()[1]  # Get center IR sensor value
    return front_center > threshold

while True:
    if object_detected():
        print("Object detected ahead! Stopping.")
        zumi.stop()
        break
    
    zumi.forward()
    time.sleep(0.1)

zumi.stop()

##########################################################################################

# Advanced Object Detection, Stop and Count Objects
# Plays note when an object is detected 

from zumi.zumi import Zumi
from zumi.util.screen import Screen  # Import screen module
from zumi.protocol import Note # allows Zumi to play notes (music)
import time

zumi = Zumi()
screen = Screen()

def object_detected(threshold=100):
    """
    Checks if an object is directly in front of Zumi using the center IR sensor.
    
    Args:
    - threshold (int): Sensor value above which an object is considered detected.
    
    Returns:
    - bool: True if an object is detected ahead, False otherwise.
    """
    front_center = zumi.get_all_IR_data()[1]  # Get center IR sensor value
    return front_center > threshold

# Initialize object counter
object_count = 0
screen.draw_text_center("Objects: {object_count}")  # Display initial count

while True:
    if object_detected():
        print("Object detected ahead! Stopping.")
        zumi.play_note(13, 500) # 13 is note type (1 - 60), 500 is duration in ms
        zumi.stop()
        object_count += 1  # Increase object counter by 1
        screen.draw_text_center(f"Objects: {object_count}") # Display object count on screen     
        # Wait until the object is removed
        print("Waiting for object to be removed...")
        while object_detected():
            time.sleep(0.5)  # Check every 0.5s
        
        print("Object removed. Resuming movement.")
    
    zumi.forward()
    time.sleep(0.1)  # Small delay to avoid excessive sensor checks

# variable object_count contains the number of objects detected
# needs to be stored in the csv file
# next, I need to add the timestamp of the object detection

#zumi.stop()
# print(f"Total objects detected: {object_count}")    

