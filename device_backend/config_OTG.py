CONFIG_FILE = "/boot/config.txt"
OTG_LINE = "dtoverlay=dwc2"


def ensure_otg_line():
    try:
        with open(CONFIG_FILE, "r") as f:
            lines = [line.strip() for line in f.readlines()]

        if OTG_LINE in lines:
            print("OTG mode is already enabled.")
            return

        # Append the line if it's missing
        with open(CONFIG_FILE, "a") as f:
            f.write("\n" + OTG_LINE + "\n")
        print("OTG mode enabled: Added line to config.txt.")
    except Exception as e:
        print(f"Error modifying config.txt: {e}")


if __name__ == "__main__":
    ensure_otg_line()
