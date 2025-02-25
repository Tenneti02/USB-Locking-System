# 🔑 USB Lock & Unlock System

### Keep Your Laptop Secure with a Simple USB Key!

Imagine stepping away from your laptop and it **locks automatically** the moment you unplug your USB. Sounds cool, right? This project lets you use a **USB drive as a key** to lock and unlock your system seamlessly. No more worrying about unauthorized access!

---

## 🚀 Features

✅ **Instant Locking:** Your laptop locks **immediately** when the USB is removed.  
✅ **USB-Based Authentication:** Your system stays **unlocked only if the correct USB is inserted**.  
✅ **Real-Time Monitoring:** The script continuously checks for the USB presence every few seconds.  
✅ **Simple & Lightweight:** Runs in the background without affecting performance.  
✅ **Customizable:** Easily tweak the settings to match your security needs.  

---

## 💪 Getting Started

### 1️⃣ Generate Your USB Key

To set up your security key, you'll first generate an encryption key and store it on your USB.

1. Insert your USB drive.
2. Open `generate.py` and update the USB path if needed (default: `E:/usb_key.key`).
3. Run the following command:

   ```bash
   python generate.py
   ```

4. This will create a `usb_key.key` file on your USB and a backup on your local system.

---

### 2️⃣ Start USB Monitoring

Now, let's enable **real-time USB monitoring** so your system locks if the USB is removed.

1. Open `usb.py` and update the drive letter if needed (default: `E:`).
2. Run the script:

   ```bash
   python usb.py
   ```

3. The system will now monitor the USB:
   - **If the USB is present**, the laptop stays **unlocked**.
   - **If the USB is removed**, the laptop **locks immediately**.

---

## 🔍 How It Works

| Action | System Behavior |
|--------|---------------|
| USB is inserted | System remains **unlocked** |
| USB is removed | System **locks instantly** |
| USB is reinserted | System stays **unlocked** |

---

## 🔧 Customization

### ✅ Change USB Drive Letter
If your USB has a different drive letter, modify this line in `usb.py`:

```python
usb_drive = 'E:'  # Change 'E:' to match your USB drive
```

### ⏳ Adjust Monitoring Frequency
To change how often the script checks for the USB, update this line in `usb.py`:

```python
time.sleep(3)  # Change 3 to a different number of seconds
```

---

## ⚠️ Troubleshooting

💡 **USB Not Detected?**  
👉 Run `wmic logicaldisk get caption` in **Command Prompt** to check available drives.  
👉 Make sure the USB is properly plugged in.  

💡 **System Locks Instantly?**  
👉 Check if the `usb_key.key` file exists on the USB.  
👉 Ensure the script is running (`python usb.py`).  

---

## 🛡️ Security Note

This system currently **checks for the presence** of the USB but does not verify the file contents. For **enhanced security**, consider modifying the script to validate the key using cryptographic methods.

---

## 🎉 Enjoy Your USB Security System!

Now, your laptop is always protected! 🚀🔒 If you have any suggestions or improvements, feel free to contribute.

Happy Coding! 🌟

