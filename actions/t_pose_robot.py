# * Library imports
import time

def t_pose_robot(motion_service, hold_duration=30):
    try:
        start_time = time.time()
        while time.time() - start_time < hold_duration:
            motion_service.setAngles("LShoulderPitch", 6, 0.2)
            motion_service.setAngles("LShoulderRoll", 3, 0.2)
            motion_service.setAngles("LElbowYaw", -1.5, 0.2)
            motion_service.setAngles("LElbowRoll", 0.0, 0.2)

            motion_service.setAngles("RShoulderPitch", 6, 0.2)
            motion_service.setAngles("RShoulderRoll", -3, 0.2)
            motion_service.setAngles("RElbowYaw", 1.5, 0.2)
            motion_service.setAngles("RElbowRoll", 0.0, 0.2)

            motion_service.setAngles("LWristYaw", 0.0, 0.2)
            motion_service.setAngles("RWristYaw", 0.0, 0.2)

            time.sleep(0.1)

    except Exception as e:
        print("[ERROR] T-pose failed: {}".format(e))
