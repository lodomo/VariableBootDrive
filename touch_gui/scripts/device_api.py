import subprocess

class DeviceAPI:
    def __init__(self):
        self.api_location = "../device/main.py"
        pass

    def sign_in(self, pin):
        success = subprocess.run(
            ["python", self.api_location, "--sign-in", pin]
        )
        return success.returncode == 0
