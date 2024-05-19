def get_gps_coordinates(device_file='/dev/gps'):
    try:
        with open(device_file, 'r') as f:
            data = f.readline().strip().split(',')
            latitude = float(data[0])
            longitude = float(data[1])
            return latitude, longitude
    except FileNotFoundError:
        print(f"GPS device file '{device_file}' not found.")
        return None, None
    except Exception as e:
        print(f"Error reading GPS data: {e}")
        return None, None