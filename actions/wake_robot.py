# * Library imports
import time

def wake_robot(motion_service, led_service, tts_service):
    if motion_service and led_service:
        try:
            motion_service.wakeUp()
            led_service.fadeRGB("FaceLeds", 0x000080FF, 1.0)

            time.sleep(1)

            tts_service.say("Good Morning! How can I help you?")
        except Exception as e:
            print("Error waking up the robot: {}".format(e))