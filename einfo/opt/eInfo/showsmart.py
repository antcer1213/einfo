#!/usr/bin/python
#
# Author: Louwrentius
# Revisions By: Anthony "Antcer" Cervantes
# Requirement: smart
#
# Version: 1.0
#

import re
import sys
import os

smarterror = False

pcidevices = ""
diskbysortdata = ""

#
# Get all network interfaces
#
def get_block_devices():
    devicepath = "/sys/block"
    diskdevices = os.listdir(devicepath)
    diskdevices = [i for i in diskdevices if not "loop" in i]
    diskdevices = [i for i in diskdevices if not "ram" in i]
    diskdevices = [i for i in diskdevices if not "sr" in i]
    return diskdevices

def get_param_from_smart(data,parameter,distance=-1,delimiter=" "):
    regex = re.compile(parameter + '(.*)')
    match = regex.search(data)
    if match:
        try:
            model = match.group(1).split(delimiter)[distance]
            return str(model).strip()
        except OSError:
            print "An error happened"
            return None
    return None


def get_smart_data(device, rec_data, toolkit):
    smartdata = str()
    #~ if toolkit:
        #~ from general import run
        #~ command = "smartctl -a %s"%device
        #~ run(command, smartdata, endfx=[finish_process_device, device, rec_data, smartdata])
    #~ else:
    import subprocess
    try:
        rawdata = subprocess.Popen(['smartctl', '-a', device], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        smartdata = rawdata[0]
        errordata = rawdata[1]
        if errordata:
            smartdata = None
    except OSError:
        global smarterror
        smarterror = True
        smartdata = None
    return finish_process_device(device, rec_data, smartdata)

def process_device(diskdevice, rec_data=False, toolkit=False):
    fullpath = "/dev/" + diskdevice

    return get_smart_data(fullpath, rec_data, toolkit)

def finish_process_device(device, rec_data, d):
    data = {}
    data['info'] = {}
    #INFO
    data['info']['Model Family'] = get_param_from_smart(d,"Model Family:",delimiter=":")
    data['info']['Device Model'] = get_param_from_smart(d,"Device Model:",delimiter=":")
    data['info']['Serial Number'] = get_param_from_smart(d,"Serial Number:",delimiter=":")
    data['info']['LU WWN Device ID'] = get_param_from_smart(d,"LU WWN Device Id:",delimiter=":")
    data['info']['Firmware Version'] = get_param_from_smart(d,"Firmware Version:",delimiter=":")
    data['info']['User Capacity'] = get_param_from_smart(d,"User Capacity:",delimiter=":")
    data['info']['Sector Size'] = get_param_from_smart(d,"Sector Size:",delimiter=":")
    data['info']['Rotation Rate'] = get_param_from_smart(d,"Rotation Rate:",delimiter=":")
    #~ data['info']['Device is'] = get_param_from_smart(d,"Device is:",delimiter=":")
    data['info']['ATA Version'] = get_param_from_smart(d,"ATA Version is:",delimiter=":")
    data['info']['SATA Version'] = get_param_from_smart(d,"SATA Version is:",delimiter=":")
    data['info']['SMART Support'] = get_param_from_smart(d,"SMART support is:",delimiter=":")
    #STATS
    data['stats'] = {}
    data['stats']['Health Status'] = get_param_from_smart(d,"self-assessment test result")
    data['stats']['Spin-Up Time'] = get_param_from_smart(d, "  3 S")
    data['stats']['Start/Stop Count'] = get_param_from_smart(d,"  4 S")
    data['stats']['Reallocated Sector Count'] = get_param_from_smart(d,"  5 R")
    data['stats']['Power-On Hours'] = get_param_from_smart(d,"  9 P")
    data['stats']['Power Cycle Count'] = get_param_from_smart(d," 12 P")
    data['stats']['Host Writes (32MiB)'] = get_param_from_smart(d,"225 H")
    data['stats']['Work ID - Media Wear Indicator'] = get_param_from_smart(d,"226 W")
    data['stats']['Work ID - Host Reads Percentage'] = get_param_from_smart(d,"227 W")
    data['stats']['Workload Minutes'] = get_param_from_smart(d,"228 W")
    data['stats']['Available Reserved Space'] = get_param_from_smart(d,"232 A")
    data['stats']['Media Wearout Indicator'] = get_param_from_smart(d,"233 M")
    data['stats']['End-to-end Error'] = get_param_from_smart(d,"184 E")
    #TESTS
    data['tests'] = {}

    return data

    #~ rec_data(device.split("/")[-1], data)

if __name__ == "__main__":
    process_device(device)
