import os
import sys
import shutil

def install_xip():
    """Install XIP service and configuration files"""
    if os.geteuid() != 0:
        print("Installation requires root privileges")
        sys.exit(1)

    # Create necessary directories
    os.makedirs("/etc/xip", exist_ok=True)
    os.makedirs("/var/log/xip", exist_ok=True)

    # Copy service files
    shutil.copy("xipd.service", "/etc/systemd/system/")
    
    # Create configuration
    with open("/etc/xip/config.json", "w") as f:
        f.write("""{
    "interface": "eth0",
    "xip_address": null,
    "log_level": "INFO"
}""")

    # Set up logging
    with open("/etc/rsyslog.d/xip.conf", "w") as f:
        f.write("local0.*    /var/log/xip/xip.log")

    print("XIP installation complete")

if __name__ == "__main__":
    install_xip()
