import pytest
from device_api import DeviceAPI

def test_sign_in_create_password_change_password():
    ## Tests Sign in, Create Password, Change Password
    device = DeviceAPI()
    device._DeviceAPI__force_pin_reset()
    assert device.sign_in() == device.CODES["invalid_argument(s)"]
    assert device.sign_in("1234") == device.CODES["pin_not_set"]
    assert device.sign_in(["1234"]) == device.CODES["pin_not_set"]
    assert device.create_password("1234") == device.CODES["success"]
    assert device.sign_in("1234") == device.CODES["success"]
    assert device.sign_in("5678") == device.CODES["pin_incorrect"]
    assert device.change_password("1234", "5678") == device.CODES["success"]
    assert device.sign_in("1234") == device.CODES["pin_incorrect"]
    assert device.sign_in("5678") == device.CODES["success"]
    assert device.change_password("5678", "66666") == device.CODES["invalid_pin"]
    assert device.change_password("5678", "6666") == device.CODES["success"]
    assert device.sign_in("5678") == device.CODES["pin_incorrect"]
    assert device.sign_in("6666") == device.CODES["success"]
    assert device.sign_in("66666") == device.CODES["pin_incorrect"]
