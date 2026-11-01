# 🚀 Professional High-Speed Wi-Fi & Network Scanner

A lightweight, multi-threaded network scanning tool written in Python that automatically detects active local devices, IP addresses, MAC addresses, and device manufacturers within seconds.

## ✨ Features
* **Auto Subnet Detection:** Automatically finds your local machine's IP and scans the entire `/24` subnet.
* **High-Speed Multithreading:** Powered by Python's `concurrent.futures` to scan 254 IP addresses in under 3-4 seconds.
* **Hardware Identification:** Resolves MAC addresses via ARP and queries vendor APIs to identify device brands.
* **Clean Terminal Output:** Formatted tabular results for easy reading.

## 📋 Requirements
* Python 3.x
* Windows OS (uses native `arp` and `ping` commands)

## ⚙️ Usage
1. Clone or download the repository.
2. Run the script using Command Prompt:
   ```cmd
   python scanner.py
