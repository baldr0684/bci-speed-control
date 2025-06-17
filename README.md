# Robot Speed Control Using BCI Demo

This project demonstrates how to control the speed of a Lego EV3 robot using brain–computer interface (BCI) signals from an Emotiv headset and a Raspberry Pi.

---

## Prerequisites

* **Admin rights** on both laptop/Desktop and Raspberry Pi
* **USB enablement** on Raspberry Pi for EV3 connection
* Laptop/Desktop and Raspberry Pi **must be on the same network** (open network recommended)

---

## Hardware Requirements

* Emotiv Insight or EPOC+ headset
* Lego EV3 brick (powered by 6× AA batteries)
* Raspberry Pi 3B+ (powered via power bank)
* Bluetooth USB dongle (for Emotiv–PC pairing)
* USB cable (for Pi–EV3 connection)

---

## Software Requirements

### On Laptop/Desktop

* Windows 8 or Windows 10
* Internet Explorer (for BCI GUI, if needed)
* Python 3.6
* .NET Framework 4.0 or above
* Python modules:

  * `flask`
  * `flask_cors`

  ```bash
  pip install flask flask_cors
  ```

### On Raspberry Pi

* Raspbian with Python 3
* Python modules:

  * `requests`
  * `usb.core`

  ```bash
  sudo pip3 install requests pyusb
  ```

---

## Setup Instructions

1. **Power on devices**

   * Switch on the Emotiv headset via its power button.
   * Power the Raspberry Pi from a power bank.
   * Power up the EV3 brick by pressing its center button.

2. **Network configuration**

   * Ensure both the laptop/Desktop and Raspberry Pi are connected to the **same network**.

3. **Clone the repository**

   On both machines, navigate to your working directory and clone:

   ```bash
   git clone https://github.com/<username>/bci-speed-control.git
   ```

4. **Configure Raspberry Pi IP**

   * On the Pi, open the speed control script:

     ```bash
     cd ~/Desktop/LegoSpeedControlUsingEpoc
     sudo nano speed_control.py
     ```

   * Update the `IP_ADDRESS` variable to match your laptop’s/Desktop’s IP address (do **not** change port or route).

5. **Install dependencies**

   * On Laptop/Desktop:

     ```bash
     pip install flask flask_cors
     ```
   * On Raspberry Pi:

     ```bash
     sudo pip3 install requests pyusb
     ```

---

## Execution Steps

### 1. Run BCI Publisher (Laptop/Desktop)

1. Plug in the Bluetooth dongle and pair the Emotiv headset.
2. Power on the Emotiv device.
3. In a command prompt, navigate to the BCI folder and run:

   ```bash
   python publish.py
   ```

### 2. Run Speed Control Service (Raspberry Pi)

1. In a terminal on the Pi, navigate to the code folder:

   ```bash
   cd ~/Desktop/LegoSpeedControlUsingEpoc
   ```
2. Start the speed control script:

   ```bash
   sudo python3 speed_control.py
   ```

* Use **Ctrl + C** (or **Ctrl + Z**) to stop the scripts on either machine at any time.

---

## Notes

* Ensure the EV3 brick and Pi remain powered throughout the demo.
* Check network connectivity if signals are not received.
* Consult Emotiv and EV3 documentation for troubleshooting hardware connections.

---

*End of README*
