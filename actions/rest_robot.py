def rest_robot(motion_service):
    if motion_service:
        try:
            motion_service.rest()
        except Exception as e:
            print("Error putting robot to rest: {}".format(e))