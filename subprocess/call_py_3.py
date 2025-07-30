# * Library imports
import os

def call_python3_script(script_path):
    try:
        command = "python3 {} 2>&1".format(script_path)
        pipe = os.popen(command)
        output = pipe.read().strip()
        exit_code = pipe.close()

        if exit_code is None:
            print(output)
            return output
        else:
            print("Script failed with exit code: {}".format(exit_code))
            return None
    except Exception as e:
        print("An error occurred: {}".format(e))


def call_python3_with_args(script_path, *args):
    try:
        args_str = ' '.join('"{}"'.format(arg) if ' ' in str(arg) else str(arg) for arg in args)
        command = "python3 {} {} 2>&1".format(script_path, args_str)

        pipe = os.popen(command)
        output = pipe.read().strip()
        exit_code = pipe.close()

        if exit_code is None:
            print(output)
            return output
        else:
            print("Script with args failed with exit code: {}".format(exit_code))
            return None
    except Exception as e:
        print("An error occurred: {}".format(e))