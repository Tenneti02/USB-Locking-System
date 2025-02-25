from cryptography.fernet import Fernet

# Generate a unique key
key = Fernet.generate_key()

# Save the key to the USB
usb_path = "E:/usb_key.key"  # Replace E: with your USB drive letter
with open(usb_path, "wb") as key_file:
    key_file.write(key)

# Save a copy on the laptop
laptop_path = "C:/Users/Tenneti/Desktop/stored_key.key"
# Replace C: with your desired location
with open(laptop_path, "wb") as key_file:
    key_file.write(key)

print("Key generated and saved successfully.")
