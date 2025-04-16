# -*- coding:utf-8 -*-
import LCD_1in44

import RPi.GPIO as GPIO
import time
from PIL import Image
import requests
from io import BytesIO

# GPIO button pins (not used here but initialized)
KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13
KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16

# Init GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.cleanup()
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the LCD
disp = LCD_1in44.LCD()
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT
disp.LCD_Init(Lcd_ScanDir)
disp.LCD_Clear()

# Set the image URL
image_url = "image.png"  # Replace with your preferred image

try:
    LCD.LCD_Init(Lcd_ScanDir)
    LCD.LCD_Clear()
    print("Downloading image...")
    response = requests.get(image_url)
    response.raise_for_status()
    
    # Load and process the image
    image = Image.open(image_url)
    image = image.resize((128, 128)).convert('RGB')
    
    print("Displaying image on LCD...")
    disp.LCD_ShowImage(image, 0, 0)

except Exception as e:
    print(f"Error: {e}")

# Keep the image displayed
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program stopped and GPIO cleaned up.")
