import sys

from device_api import DeviceAPI

# Provides command line interface for the device
# Will only take one argument at a time
#
# Handles the following commands:
# - mount [ISO to mount]
# - unmount
# - flash_mode_on
# - flash_mode_off
# - sign_in
# - create_password
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

DEVICE_API = DeviceAPI()

OPTIONS = {
    "--mount": DEVICE_API.mount,
    "--unmount": DEVICE_API.unmount,
    "--flash_mode_on": DEVICE_API.flash_mode_on,
    "--flash_mode_off": DEVICE_API.flash_mode_off,
    "--sign_in": DEVICE_API.sign_in,
    "--create_password": DEVICE_API.create_password,
    "--change_password": DEVICE_API.change_password,
    "--web_interface_on": DEVICE_API.web_interface_on,
    "--web_interface_off": DEVICE_API.web_interface_off,
    "--update": DEVICE_API.update,
    "--info": DEVICE_API.info,
}


def main(*args, **kwargs):
    if not args:
        return show_help()

    command = args[0]
    if command in ["--help", "-h"]:
        return show_help()

    if command not in OPTIONS:
        return show_help(DEVICE_API.CODES["invalid_option"])

    try:
        if len(args) == 1:
            return OPTIONS[command]()
        else:
            return OPTIONS[command](*args[1:])
    except Exception:
        return show_help(DEVICE_API.CODES["invalid_argument(s)"])
    pass


def show_help(return_code=DEVICE_API.CODES["success"]):
    print(
        """
        Usage: python main.py [option] [arguments]
        Options:
        --help, -h:                     Show this help message
        --mount [path]:                 Mount the an ISO file for USB use
        --unmount:                      Unmount the device ISO
        --flash_mode_on:                Turn on flash drive mode
        --flash_mode_off:               Turn off the flash drive mode
        --sign_in [pin]:                Sign in with the provided password
        --change_password [old] [new]:  Change the password
        --web_interface_on:             Turn on the web interface
        --web_interface_off:            Turn off the web interface
        --update:                       Update the device
        --info:                         Get information about the device
        """
    )
    return return_code


if __name__ == "__main__":
    args = sys.argv[1:]
    exit(main(*args))
