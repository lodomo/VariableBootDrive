import subprocess

PREFIX = "[VariableBootDrive] "
PACKAGES = [
    "redis",
    "pipenv",
]


def main():
    for package in PACKAGES:
        apt_install(package)
    pass


def is_installed(package):
    try:
        subprocess.check_call(["which", package])
        return True
    except subprocess.CalledProcessError:
        return False


def apt_install(package):
    if is_installed(package):
        print(f"{package} is already installed.")
        return

    print(f"Installing {package}...")
    subprocess.check_call(["sudo", "apt", "install", "-y", package])


def print(*args, **kwargs):
    args = (PREFIX,) + args
    __builtins__.print(*args, **kwargs)


if __name__ == "__main__":
    main()
