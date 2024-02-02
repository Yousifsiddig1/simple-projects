#!/usr/bin/env python3
import shutil
import psutil

def cpu_h():
    cpu_use = psutil.cpu_percent(interval=1)
    return cpu_use < 75  # Return True if the CPU usage is less than 75%

def disk_u(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20  # Return True if the free space is more than 20%

if not cpu_h() or not disk_u('/'):
    print('Error!')
else:
    print("Everything is okay")


#
# Instructions for running the script in a Unix-like environment:
# 1. Make the script executable by running: chmod +x system_check.py
# 2. Execute the script using: ./system_check.py
# Note: The first line in the script (shebang) is important for the executable to work.
# - In Windows:
#   1. Open a command prompt or PowerShell.
#   2. Navigate to the directory containing the script.
#   3. Execute the script using: python system_check.py
