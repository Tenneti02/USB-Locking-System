import os
import time
import ctypes

def lock_laptop():
    # Lock the laptop using ctypes.windll
    print("Locking system...")
    ctypes.windll.user32.LockWorkStation()

def unlock_laptop():
    # Code to unlock (this would normally be part of a larger authentication system)
    print("System remains unlocked.")

def check_usb_key():
    # List all drives
    partitions = [drive.strip() for drive in os.popen("wmic logicaldisk get caption").read().splitlines() if len(drive.strip()) == 2]
    print(f"Available partitions: {partitions}")  # Debugging line to see available drives

    # Check if USB is inserted by looking for the specific partition (e.g., E:)
    usb_drive = 'E:'  # Assuming USB drive is E:
    if usb_drive in partitions:
        print(f"USB drive detected at {usb_drive}. Checking the key...")
        # Here you would check the USB key, assuming it's just detection for simplicity
        print("Authentication successful. System remains unlocked.")
        return True
    else:
        print("USB not detected. Locking system...")
        lock_laptop()
        return False

def monitor_usb():
    while True:
        print("Monitoring USB drive...")
        if not check_usb_key():  # Lock system if USB is not found
            print("USB still not connected. System remains locked.")
        else:
            print("USB detected. System remains unlocked.")
        time.sleep(3 )  # Prevent excessive checking

if __name__ == "__main__":
    monitor_usb()

