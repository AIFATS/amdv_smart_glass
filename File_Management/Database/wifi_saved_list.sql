-- Create the wifi_details table if it does not already exist
CREATE TABLE IF NOT EXISTS wifi_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ssid TEXT,
    security TEXT,
    password TEXT
);

-- Insert sample Wi-Fi details
INSERT INTO wifi_details (ssid, security, password) VALUES ('HomeWiFi', 'WPA2', 'homepassword');
INSERT INTO wifi_details (ssid, security, password) VALUES ('OfficeWiFi', 'WPA2', 'officepassword');
INSERT INTO wifi_details (ssid, security, password) VALUES ('CafeWiFi', 'WPS', 'cafepassword');
INSERT INTO wifi_details (ssid, security, password) VALUES ('LibraryWiFi', 'WPA', 'librarypassword');
INSERT INTO wifi_details (ssid, security, password) VALUES ('GuestWiFi', 'WEP', 'guestpassword');
