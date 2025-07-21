import qi


def get_all_sessions():
    """
    Get all available sessions on the Pepper robot
    """
    try:
        # Connect to the robot
        session = qi.Session()
        session.connect("tcp://127.0.0.1:9559")  # Default local connection
        # For remote connection, use: session.connect("tcp://ROBOT_IP:9559")

        # Get the session service
        session_service = session.service("ALSessionManager")

        # Get all available sessions
        sessions = session_service.getActiveSessions()

        print("Available sessions:")
        for i, session_info in enumerate(sessions):
            print("Session {}:".format(i + 1))
            print("  ID: {}".format(session_info.get('id', 'N/A')))
            print("  Name: {}".format(session_info.get('name', 'N/A')))
            print("  Status: {}".format(session_info.get('status', 'N/A')))
            print("  Owner: {}".format(session_info.get('owner', 'N/A')))
            print("-" * 30)

        return sessions

    except Exception as e:
        print("Error getting sessions: {}".format(e))
        return []


def get_session_details():
    """
    Alternative method to get session information using ALMemory
    """
    try:
        session = qi.Session()
        session.connect("tcp://127.0.0.1:9559")

        # Get ALMemory service
        memory = session.service("ALMemory")

        # Get session-related information
        session_keys = memory.getDataListName()
        session_related = [key for key in session_keys if 'session' in key.lower()]

        print("Session-related memory keys:")
        for key in session_related:
            try:
                value = memory.getData(key)
                print("{}: {}".format(key, value))
            except:
                print("{}: <unable to retrieve>".format(key))

    except Exception as e:
        print("Error accessing memory: {}".format(e))


def list_running_services():
    """
    List all running services (which represent active sessions/modules)
    """
    try:
        session = qi.Session()
        session.connect("tcp://192.168.88.166:9559")

        # Get service directory
        services = session.services()

        print("Total running services: {}".format(len(services)))
        print("\nRunning services:")
        for service_info in services:
            print("  - {} (ID: {})".format(service_info['name'], service_info['serviceId']))

        return services

    except Exception as e:
        print("Error listing services: {}".format(e))
        return []


if __name__ == "__main__":
    print("=== Getting All Available Sessions ===")
    sessions = get_all_sessions()

    print("\n=== Session Details from Memory ===")
    get_session_details()

    print("\n=== Running Services ===")
    services = list_running_services()