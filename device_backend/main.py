import sys

from device_api import DeviceAPI

# Provides command line interface for the device
# Will only take one argument at a time
#
# Handles the following commands:
# - mount
# - unmount
# - create_password
# - sign_in
# - change_password
# - web_interface_on
# - web_interface_off
# - update
# - info
#
# Example Usage:
# python main.py --mount /mnt/usb
# python main.py --unmount
# python main.py --sign_in 1234
# python main.py --change_password 1234 5678
# python main.py --web_interface_on
# python main.py --web_interface_off
# python main.py --update

OPTIONS = {
    "--help": DeviceAPI.help,
    "-h": DeviceAPI.help,
    "--mount": DeviceAPI.mount,
    "--unmount": DeviceAPI.unmount,
    "--create_password": DeviceAPI.create_password,
    "--sign_in": DeviceAPI.sign_in,
    "--change_password": DeviceAPI.change_password,
    "--web_interface_on": DeviceAPI.web_interface_on,
    "--web_interface_off": DeviceAPI.web_interface_off,
    "--update": DeviceAPI.update,
    "--info": DeviceAPI.info,
}

CODES = {
    "success": 0,
    "missing_option": 1,
    "invalid_option": 2,
    "invalid_argument(s)": 3,
}


def main(*args, **kwargs):
    if not args:
        return help()

    command = args[0]
    if command not in OPTIONS:
        return help(CODES["invalid_option"])

    try:
        return OPTIONS[command](*args[1:])
    except Exception:
        return help(CODES["invalid_argument(s)"])
    pass


def help(return_code=CODES["success"]):
    return return_code


if __name__ == "__main__":
    args = sys.argv[1:]
    exit(main(*args))
