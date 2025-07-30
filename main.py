# * Library imports
import os
from dotenv import load_dotenv
import time

# * File imports
from services import PepperServices
from actions import wake_robot, rest_robot, t_pose_robot
from subprocess import call_python3_script, call_python3_with_args

load_dotenv()

class Pepper:
    def __init__(self):
        self.PEPPER_IP = os.getenv("PEPPER_IP")
        self.PEPPER_PORT = int(os.getenv("PEPPER_PORT"))
        self.AI_API_KEY = os.getenv("AI_API_KEY")
        self.services = None

    def main(self):
        self.services = PepperServices(self.PEPPER_IP, self.PEPPER_PORT)

        if not self.services.get_services():
            print("Can't connect to Pepper robot")
            return

        print("Connected to Pepper robot")

        try:
            call_python3_with_args("test.py", 'world')

            self.services.as_service.setBodyLanguageMode(1)

            self.services.tts_service.setParameter("speed", 100)
            self.services.tts_service.setParameter("pitch", 0.5)

            wake_robot(motion_service=self.services.motion_service,led_service=self.services.led_service, tts_service=self.services.tts_service)

            time.sleep(2)

        except Exception as e:
            print("An error occurred: {}".format(e))

        finally:
            rest_robot(motion_service=self.services.motion_service)

if __name__ == "__main__":
    pepper = Pepper()
    pepper.main()