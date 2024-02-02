#!/usr/bin/env python3
import shutil
import psutil

def cpu_h():
    cpu_use = psutil.cpu_percent(interval=1)
    return cpu_use < 75  # return True if the CPU usage is less than 75%

def disk_u(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20  # return True if the free space is more than 20%

if not cpu_h() or not disk_u('/'):
    print('Error!')
else:
    print("Everything is okay")
#
