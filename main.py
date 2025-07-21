import qi
import sys
import time

def main():
    app = qi.Application(sys.argv)
    app.start()

    session = qi.Session()
    session.connect("tcp://192.168.88.166:9559")

    try:
        # Get Services
        motion = session.service("ALMotion")
        tts = session.service("ALTextToSpeech")
        leds = session.service("ALLeds")
        audio = session.service("ALAudioDevice")

        # Wake up the robot
        motion.wakeUp()

        tts.setParameter("pitchShift", 0.5)
        tts.setParameter("speed", 90)

        audio.setOutputVolume(40)

        leds.fadeRGB("FaceLeds", 0x00AAFF, 5.0)

        motion.setAngles(["LShoulderPitch", "RShoulderPitch"], [-0.5, -0.5], 0.3)
        motion.setAngles(["LElbowRoll", "RElbowRoll"], [-0.8, 0.8], 0.3)
        motion.setAngles(["LHand", "RHand"], [0.0, 0.0], 0.5)

        time.sleep(0.5)

        message = "test"

        # tts.say("\\rspd=120\\\\vol=90\\\\vct=90\\" + message)

        time.sleep(1)
        motion.setAngles("HeadYaw", -0.3, 0.5)  # Turn head left angrily
        time.sleep(0.5)
        motion.setAngles("HeadYaw", 0.3, 0.5)  # Turn head right angrily
        time.sleep(0.5)
        motion.setAngles("HeadYaw", 0.0, 0.5)  # Center head
        try:
            motion.setAngles(["LAnklePitch", "RAnklePitch"], [0.1, 0.1], 0.8)
            time.sleep(0.2)
            motion.setAngles(["LAnklePitch", "RAnklePitch"], [-0.1, -0.1], 0.8)
        except:
            pass

        motion.setAngles(["LShoulderPitch", "RShoulderPitch"], [1.0, 1.0], 0.5)
        motion.setAngles(["LElbowRoll", "RElbowRoll"], [-0.3, 0.3], 0.5)
        motion.setAngles(["LHand", "RHand"], [0.6, 0.6], 0.5)

        print("Pepper has calmed down")

    except Exception as e:
        print("Error: {}".format(e))

    finally:
        try:
            tts.setParameter("pitchShift", 1.0)
            tts.setParameter("speed", 100)
            audio.setOutputVolume(60)
            leds.fadeRGB("FaceLeds", 0x00AAFF, 1.0)
        except:
            pass

    app.stop()

if __name__ == "__main__":
    main()