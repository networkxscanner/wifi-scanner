import subprocess
import socket
import urllib.request
import concurrent.futures
import time

def get_device_vendor(mac_address):
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=2) as response:
            return response.read().decode('utf-8')
    except:
        return "Unknown Brand"

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_mac_address(target_ip):
    try:
        output = subprocess.check_output(['arp', '-a', target_ip], universal_newlines=True)
        for line in output.split('\n'):
            if target_ip in line:
                parts = line.split()
                if len(parts) >= 2:
                    return parts[1].replace('-', ':')
    except:
        pass
    return None

def scan_single_ip(target_ip):
    # Fast ping with 50ms timeout
    result = subprocess.run(['ping', '-n', '1', '-w', '50', target_ip], 
                            stdout=subprocess.DEVNULL, 
                            stderr=subprocess.DEVNULL)
    
    if result.returncode == 0:
        mac = get_mac_address(target_ip)
        vendor = get_device_vendor(mac) if mac else "Router / Local Machine"
        return (target_ip, mac if mac else "N/A", vendor)
    return None

def main():
    start_time = time.time()
    local_ip = get_local_ip()
    print(f"[-] Aapka Local IP: {local_ip}")
    
    ip_prefix = ".".join(local_ip.split('.')[:3]) + "."
    print(f"[-] High-Speed Network Scan Start ho gaya hai: {ip_prefix}0/24...\n")
    print(f"{'IP Address':<16} | {'MAC Address':<18} | {'Manufacturer / Brand'}")
    print("-" * 65)

    active_devices = []
    
    # Multithreading Engine (50 concurrent threads for maximum speed)
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(scan_single_ip, ip_prefix + str(i)) for i in range(1, 255)]
        
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res:
                active_devices.append(res)
                print(f"{res[0]:<16} | {res[1]:<18} | {res[2]}")

    elapsed_time = time.time() - start_time
    print("-" * 65)
    print(f"[+] Scan Complete! Total Active Devices: {len(active_devices)}")
    print(f"[+] Time Taken: {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    print("--- Professional High-Speed Wi-Fi Scanner Pro ---")
    main()
    input("\n[+] Scan mukammal ho gaya hai. Exit karne ke liye Enter dabayein...")