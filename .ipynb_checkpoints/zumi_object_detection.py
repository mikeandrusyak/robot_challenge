# import libraries
from zumi.zumi import Zumi
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

from zumi.zumi import Zumi

zumi = Zumi()

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

while True:
    if object_detected():
        print("Object detected ahead! Stopping.")
        zumi.stop()
        object_count += 1  # Increase object counter by 1        
        # Wait until the object is removed
        print("Waiting for object to be removed...")
        while object_detected():
            time.sleep(0.5)  # Check every 0.5s
        
        print("Object removed. Resuming movement.")
    
    zumi.forward()
    time.sleep(0.1)  # Small delay to avoid excessive sensor checks

zumi.stop()
print(f"Total objects detected: {object_count}")    

##########################################################################################

import time
from zumi.zumi import Zumi
from zumi.util.screen import Screen  # Import screen module

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
screen.draw_text("Objects: 0")  # Display initial count

while True:
    if object_detected():
        zumi.stop()
        object_count += 1  # Increase object counter
        
        # Update Zumi's screen with object count
        screen.draw_text(f"Objects: {object_count}")
        
        # Wait until the object is removed
        while object_detected():
            time.sleep(0.5)  # Check every 0.5s
        
        screen.draw_text("Object removed")  # Temporary message
        time.sleep(1)
        screen.draw_text(f"Objects: {object_count}")  # Restore count display
    
    zumi.forward()
    time.sleep(0.1)  # Small delay to avoid excessive sensor checks

zumi.stop()
