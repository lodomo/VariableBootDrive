import hashlib
import subprocess

import yaml


class DeviceAPI:
    """
    Methods:
    - mount [path]
    - unmount
    - flash_mode_on
    - flash_mode_off
    - sign_in [password]
    - change_password [old_password] [new_password]
    - web_interface_on
    - web_interface_off
    - update
    - info
    """

    def __init__(self):
        self.CODES = {
            "success": 0,
            "missing_option": 1,
            "invalid_option": 2,
            "invalid_argument(s)": 3,
            "pin_not_set": 4,
            "pin_incorrect": 5,
            "invalid_pin": 6,
            "pin_already_set": 7,
        }

        pass

    def mount(self, *args, **kwargs):
        return 0

    def unmount(self, *args, **kwargs):
        return 0

    def flash_mode_on(self, *args, **kwargs):
        """
        Sets the entire SD card as a USB drive

        Runs the command:
        sudo modprobe g_mass_storage file=/dev/mmcblk0p2 removable=1
        """
        if not self.__has_args(0, *args):
            return self.CODES["invalid_argument(s)"]

        result = subprocess.run(
            [
                "sudo",
                "modprobe",
                "g_mass_storage",
                "file=/dev/mmcblk0p2",
                "removable=1",
            ]
        )

        return 0

    def flash_mode_off(self, *args, **kwargs):
        """
        sudo rmmod g_mass_storage
        """

        if not self.__has_args(0, *args):
            return self.CODES["invalid_argument(s)"]

        subprocess.run(["sudo", "rmmod", "g_mass_storage"])

        return 0

    def sign_in(self, *args, **kwargs):
        """
        Takes in a 4 digit pin and checks if it matches the stored pin
        """
        if not self.__has_args(1, *args):
            return self.CODES["invalid_argument(s)"]

        settings = self.__import_yaml()

        if "pin_hash" not in settings["device"]:
            return self.CODES["pin_not_set"]

        pin = args[0]
        pin_hash = self.__hash(pin)

        if pin_hash != settings["device"]["pin_hash"]:
            return self.CODES["pin_incorrect"]

        return self.CODES["success"]

    def create_password(self, *args, **kwargs):
        if not self.__has_args(1, *args):
            return self.CODES["invalid_argument(s)"]

        settings = self.__import_yaml()

        if "pin_hash" in settings["device"]:
            return self.CODES["pin_already_set"]

        pin = args[0]

        if not self.__valid_pin(pin):
            return self.CODES["invalid_pin"]

        settings["device"]["pin_hash"] = self.__hash(pin)

        self.__update_yaml(settings)
        return self.CODES["success"]

    def change_password(self, *args, **kwargs):
        if not self.__has_args(2, *args):
            return self.CODES["invalid_argument(s)"]

        old_pin = args[0]
        new_pin = args[1]

        settings = self.__import_yaml()

        is_old_pin = self.sign_in(old_pin)
        if is_old_pin != self.CODES["success"]:
            return is_old_pin

        if not self.__valid_pin(new_pin):
            return self.CODES["invalid_pin"]

        settings["device"]["pin_hash"] = self.__hash(new_pin)
        self.__update_yaml(settings)
        return self.CODES["success"]

    def web_interface_on(self, *args, **kwargs):
        return 0

    def web_interface_off(self, *args, **kwargs):
        return 0

    def update(self, *args, **kwargs):
        return 0

    def info(self, *args, **kwargs):
        return 0

    def __force_pin_reset(self):
        settings = self.__import_yaml()
        settings["device"].pop("pin_hash", None)
        self.__update_yaml(settings)
        return

    def __hash(self, pin):
        return hashlib.sha256(pin.encode()).hexdigest()

    def __valid_pin(self, pin):
        """
        Check if the pin is a 4-digit number
        """
        return pin.isdigit() and len(pin) == 4

    def __has_args(self, count, *args):
        if not args:
            return False
        return len(args) == count

    def __import_yaml(self):
        yaml_file = "settings.yaml"
        with open(yaml_file, "r") as file:
            settings = yaml.safe_load(file)
        return settings

    def __update_yaml(self, settings):
        yaml_file = "settings.yaml"
        with open(yaml_file, "w") as file:
            yaml.safe_dump(settings, file)
        return settings
