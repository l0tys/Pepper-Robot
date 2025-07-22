# * Library imports
import os
from dotenv import load_dotenv
import naoqi
import time

from actions import wake_up

def main():
    load_dotenv()
    PEPPER_IP = os.getenv("PEPPER_IP")
    PORT = int(os.getenv("PEPPER_PORT"))

    try:
        # Get all services
        motion_service = naoqi.ALProxy("ALMotion", PEPPER_IP, PORT)
        tts_service = naoqi.ALProxy("ALTextToSpeech", PEPPER_IP, PORT)
        led_service = naoqi.ALProxy("ALLeds", PEPPER_IP, PORT)
        print("Connected to Pepper robot")
    except Exception as e:
        print("Can't connect to Pepper robot: {}".format(e))
        return

    try:
        wake_up(motion_service, led_service, tts_service)
    except Exception as e:
        print("An error occurred: {}".format(e))

    finally:
        time.sleep(3)
        motion_service.rest()

if __name__ == "__main__":
    main()