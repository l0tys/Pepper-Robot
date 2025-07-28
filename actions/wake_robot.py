# * Library imports
import time

def wake_robot(motion_service, led_service, as_service):
    if motion_service and led_service and as_service:
        try:
            motion_service.wakeUp()
            led_service.fadeRGB("FaceLeds", 0x000080FF, 1.0)

            time.sleep(3)

            as_service.say(
                "^start(animations/Stand/Gestures/Hey_1) Hi There, how are you? ^wait(animations/Stand/Gestures/Hey_1)")
        except Exception as e:
            print("Error waking up the robot: {}".format(e))