# * Library imports
import time

def wake_robot(motion_service, led_service, tts_service):
    if motion_service and led_service and tts_service:
        try:
            motion_service.wakeUp()
            led_service.fadeRGB("FaceLeds", 0x000080FF, 1.0)

            time.sleep(3)

            tts_service.say("Hello! I am awake and ready to help you!")
        except Exception as e:
            print("Error waking up the robot: {}".format(e))