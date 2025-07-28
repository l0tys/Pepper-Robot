# * Library imports
from naoqi import ALProxy

class PepperServices:
    def __init__(self, PEPPER_IP, PEPPER_PORT):
        self.IP = PEPPER_IP
        self.PORT = PEPPER_PORT

        self.motion_service = None
        self.tts_service = None
        self.led_service = None
        self.nav_service = None
        self.au_life_service = None
        self.as_service = None
        self.memory_service = None
        self.sr_service = None

    def get_services(self):
        try:
            services = {
                'motion_service': 'ALMotion',
                'tts_service': 'ALTextToSpeech',
                'led_service': 'ALLeds',
                'nav_service': 'ALNavigation',
                'au_life_service': 'ALAutonomousLife',
                'as_service': 'ALAnimatedSpeech',
                'memory_service': 'ALMemory',
                'sr_service': 'ALSpeechRecognition',
            }

            for service, service_name in services.iteritems():
                setattr(self, service, ALProxy(service_name, self.IP, self.PORT))

            return True
        except Exception as e:
            print("Error initializing services: {}".format(e))
            return False