# * Library imports
import naoqi
import time

def wake_up(motion_service, led_service, tts_service):
    motion_service.wakeUp()
    time.sleep(2)

    led_service.fadeRGB("FaceLeds", 0x000080FF, 1.0)
    time.sleep(1)

    tts_service.say("Hello! I am awake and ready to help you!")