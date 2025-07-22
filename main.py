# * Library imports
import os
from dotenv import load_dotenv
import naoqi

from actions import wake_up

load_dotenv()

class Pepper:
    def __init__(self):
        self.PEPPER_IP = os.getenv("PEPPER_IP")
        self.PORT = int(os.getenv("PEPPER_PORT"))
        self.motion_service = None
        self.tts_service = None
        self.led_service = None
        self.nav_service = None

    def get_services(self):
        self.motion_service = naoqi.ALProxy("ALMotion", self.PEPPER_IP, self.PORT)
        self.tts_service = naoqi.ALProxy("ALTextToSpeech", self.PEPPER_IP, self.PORT)
        self.led_service = naoqi.ALProxy("ALLeds", self.PEPPER_IP, self.PORT)
        self.nav_service = naoqi.ALProxy("ALNavigation", self.PEPPER_IP, self.PORT)

    def main(self):
        try:
            self.get_services()
            print("Connected to Pepper robot")
        except Exception as e:
            print("Can't connect to Pepper robot: {}".format(e))
            return

        try:
            wake_up(self.motion_service, self.led_service, self.tts_service)

            while True:
                self.nav_service.explore(5)
        except Exception as e:
            print("An error occurred: {}".format(e))

        finally:
            self.motion_service.rest()

if __name__ == "__main__":
    pepper = Pepper()
    pepper.main()