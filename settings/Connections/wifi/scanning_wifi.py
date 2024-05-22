import subprocess

"""
scan the wifi 
"""

def scan_wifi():
    try:
        output = subprocess.check_output(["iwlist", "wlan0", "scan"], universal_newlines=True)
        networks = []
        ssid = None
        for line in output.split('\n'):
            line = line.strip()
            if "ESSID" in line:
                ssid = line.split('"')[1]
            elif "Signal level" in line and ssid:
                signal_strength = int(line.split("=")[1].split("/")[0])
                networks.append({'ssid': ssid, 'signal_strength': signal_strength})
                ssid = None
        return networks
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return []

if __name__ == "__main__":
    wifi_networks = scan_wifi()
    if wifi_networks:
        for network in wifi_networks:
            print("SSID: {}, Signal Strength: {} dBm".format(network['ssid'], network['signal_strength']))
    else:
        print("No Wi-Fi networks found.")
