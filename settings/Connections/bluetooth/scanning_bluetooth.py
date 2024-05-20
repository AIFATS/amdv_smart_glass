import subprocess

def scan_bluetooth():
    try:
        output = subprocess.check_output(["hcitool", "scan"], universal_newlines=True)
        devices = []
        for line in output.split('\n'):
            if line:
                parts = line.split('\t')
                if len(parts) == 2:
                    devices.append({'mac_address': parts[0], 'device_name': parts[1]})
        return devices
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return []

if __name__ == "__main__":
    bluetooth_devices = scan_bluetooth()
    if bluetooth_devices:
        for device in bluetooth_devices:
            print("MAC Address: {}, Device Name: {}".format(device['mac_address'], device['device_name']))
    else:
        print("No Bluetooth devices found.")
