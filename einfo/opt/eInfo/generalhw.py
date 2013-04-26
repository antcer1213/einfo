#!/usr/bin/env python
# encoding: utf-8
import general
from os import system

"""                 eInfo
==============================================
    Contains Hardware Information functions.

  Maintainer:    Anthony "AntCer" Cervantes
"""


class Hardware_Info():
    def __init__(self):
        with open("/opt/eInfo/info/dmiinfo") as file:
            data = file.readlines()
        del data[0:5]
        self.data = list(general.splitter(data, "Handle ", True))
        for x in self.data:
            for i in range(len(x)):
                if x[i].startswith("Handle "):
                    del x[i]
                    break

    def mobo_info(self):
        for x in self.data:
            for i in range(len(x)):
                if x[i].startswith("Base Board Information"):
                    mobo = x
                    break

        for x in mobo:
            if x.startswith("\tManufacturer:"):
                x = x[1:-1]
                man = x
                break
        for x in mobo:
            if x.startswith("\tProduct Name:"):
                x = x[1:-1]
                nam = x
                break
        for x in mobo:
            if x.startswith("\tVersion:"):
                x = x[1:-1]
                ver = x
                break
        for x in mobo:
            if x.startswith("\tSerial Number:"):
                x = x[1:-1]
                sn = x
                break

        feat = []
        for x in mobo:
            if x.startswith("\t\t"):
                x = x[:-1].replace("\t\t", "")
                feat.append(x)

        return [man, nam, ver, sn, "Features:", feat]

    def bios_info(self):
        for x in self.data:
            for i in range(len(x)):
                if x[i].startswith("BIOS Information"):
                    bios = x
                    break

        for x in bios:
            if x.startswith("\tVendor:"):
                x = x[1:-1]
                ven = x
                break
        for x in bios:
            if x.startswith("\tVersion:"):
                x = x[1:-1]
                ver = x
                break
        for x in bios:
            if x.startswith("\tRelease Date:"):
                x = x[1:-1]
                rel = x
                break
        for x in bios:
            if x.startswith("\tRuntime Size:"):
                x = x[1:-1]
                runsiz = x
                break
        for x in bios:
            if x.startswith("\tROM Size:"):
                x = x[1:-1]
                romsiz = x
                break
        for x in bios:
            if x.startswith("\tBIOS Revision:"):
                x = x[1:-1]
                birev = x
                break
        for x in bios:
            if x.startswith("\tFirmware Revision:"):
                x = x[1:-1]
                firev = x
                break

        char = []
        for x in bios:
            if x.startswith("\t\t"):
                x = x[:-1].replace("\t\t", "")
                char.append(x)

        return [ven, ver, rel, runsiz, romsiz, birev, firev, "Characteristics:", char]


    def sys_info(self):
        for x in self.data:
            for i in range(len(x)):
                if x[i].startswith("System Information"):
                    sysinfo = x
                    break

        for x in sysinfo:
            if x.startswith("\tManufacturer:"):
                x = x[1:-1]
                man = x
                break
        for x in sysinfo:
            if x.startswith("\tProduct Name:"):
                x = x[1:-1]
                nam = x
                break
        for x in sysinfo:
            if x.startswith("\tVersion:"):
                x = x[1:-1]
                ver = x
                break
        for x in sysinfo:
            if x.startswith("\tSerial Number:"):
                x = x[1:-1]
                ser = x
                break
        for x in sysinfo:
            if x.startswith("\tUUID:"):
                x = x[1:-1]
                uid = x
                break
        for x in sysinfo:
            if x.startswith("\tWake-up Type:"):
                x = x[1:-1]
                wutyp = x
                break
        for x in sysinfo:
            if x.startswith("\tSKU Number:"):
                x = x[1:-1]
                num = x
                break
        for x in sysinfo:
            if x.startswith("\tFamily:"):
                x = x[1:-1]
                fam = x
                break

        return [man, nam, ver, ser, uid, wutyp, num, fam]


    def mem_info(self):
        for x in self.data:
            for i in range(len(x)):
                if x[i].startswith("Physical Memory Array"):
                    meminfo = x
                    break

        for x in meminfo:
            if x.startswith("\tLocation:"):
                x = x[1:-1]
                loc = x
                break
        for x in meminfo:
            if x.startswith("\tError Correction Type:"):
                x = x[1:-1]
                err = x
                break
        for x in meminfo:
            if x.startswith("\tMaximum Capacity:"):
                x = x[1:-1]
                mx = x
                break
        for x in meminfo:
            if x.startswith("\tNumber Of Devices:"):
                x = x[1:-1]
                num = x
                break

        mem = ["Physical Memory Array", loc, err, mx, num]

        copy = [s for s in self.data if s[0] == "Memory Device\n"]

        if copy is None:
            return ['N/A']

        for i, y in enumerate(copy):
            mem.append(" ")
            mem.append("Memory Device %s" %i)
            for x in y:
                if x.startswith("\tSize:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tForm Factor:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tType:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tSpeed:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tManufacturer:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tLocator:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tBank Locator:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tType Detail:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tData Width:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tTotal Width:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tSerial Number:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tPart Number:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tConfigured Clock Speed:"):
                    x = x[1:-1]
                    mem.append(x)
                elif x.startswith("\tRank:"):
                    x = x[1:-1]
                    mem.append(x)

        return mem

    def bat_info(self):
        for x in self.data:
            for i in range(len(x)):
                if x[i].startswith("Portable Battery"):
                    batinfo = x
                    break

        if batinfo is None:
            return ['N/A']

        for x in batinfo:
            if x.startswith("\tName:"):
                x = x[1:-1]
                nam = x
                break
        for x in batinfo:
            if x.startswith("\tManufacturer:"):
                x = x[1:-1]
                man = x
                break
        for x in batinfo:
            if x.startswith("\tLocation:"):
                x = x[1:-1]
                loc = x
                break
        for x in batinfo:
            if x.startswith("\tChemistry:"):
                x = x[1:-1]
                chem = x
                break
        for x in batinfo:
            if x.startswith("\tDesign Capacity:"):
                x = x[1:-1]
                dcap = x
                break
        for x in batinfo:
            if x.startswith("\tDesign Voltage:"):
                x = x[1:-1]
                dvol = x
                break
        for x in batinfo:
            if x.startswith("\tMaximum Error:"):
                x = x[1:-1]
                mx = x
                break
        for x in batinfo:
            if x.startswith("\tSBDS Version:"):
                x = x[1:-1]
                ver = x
                break
        for x in batinfo:
            if x.startswith("\tSBDS Serial Number:"):
                x = x[1:-1]
                sn = x
        for x in batinfo:
            if x.startswith("\tSBDS Manufacture Date:"):
                x = x[1:-1]
                dat = x
                break

        return [nam, man, loc, chem, dcap, dvol, mx, ver, sn, dat]

    def vid_info(self):
        copy = []
        for x in self.data:
            if len(x) == 7:
                if x[5] == "\tPort Type: Video Port\n":
                    copy.append(x)

        if copy is None:
            return ['N/A']

        vid  = []

        for i, y in enumerate(copy):
            if i > 0:
                vid.append(" ")
            vid.append("Video Port %s" %i)
            for x in y:
                if x.startswith("\tInternal Reference Designator:"):
                    x = x[1:-1]
                    vid.append(x)
                elif x.startswith("\tInternal Connector Type:"):
                    x = x[1:-1]
                    vid.append(x)
                elif x.startswith("\tExternal Reference Designator:"):
                    x = x[1:-1]
                    vid.append(x)
                elif x.startswith("\tExternal Connector Type:"):
                    x = x[1:-1]
                    vid.append(x)

        return vid

    def vid_dev_info(self):
        with open("/opt/eInfo/info/viddevinfo") as file:
            data = file.readlines()
        copy = list(general.splitter(data, "*-", True))
        for x in copy:
            if x[0].startswith("  *-"):
                del x[0]
            for i in range(len(x)):
                if x[i].startswith("       "):
                    x[i] = x[i][7:]

        if copy is None:
            return ['N/A']

        vid = []

        for i, y in enumerate(copy):
            if i > 0:
                vid.append(" ")
            vid.append("Video Device %s" %i)
            for x in y:
                if x.startswith("description:"):
                    x = x[:-1].title()
                    vid.append(x)
                elif x.startswith("product:"):
                    x = x[:-1].title()
                    vid.append(x)
                elif x.startswith("vendor:"):
                    x = x[:-1].title()
                    vid.append(x)
                elif x.startswith("physical id:"):
                    x = x[:-1].title()
                    vid.append(x)
                elif x.startswith("bus info:"):
                    x = x[:-1].title()
                    vid.append(x)
                elif x.startswith("version:"):
                    x = x[:-1].title()
                    vid.append(x)
                elif x.startswith("width:"):
                    x = x[:-1].title()
                    vid.append(x)
                elif x.startswith("clock:"):
                    x = x[:-1].capitalize()
                    vid.append(x)
                elif x.startswith("configuration:"):
                    vid.append("Configuration:")
                    interim = x.split()
                    del interim[0]
                    vid.append(interim)
                elif x.startswith("capabilities:"):
                    vid.append("Capabilities:")
                    interim = x.split()
                    del interim[0]
                    vid.append(interim)
                elif x.startswith("resources:"):
                    vid.append("Resources:")
                    interim = x.split()
                    del interim[0]
                    vid.append(interim)

        return vid

    def aud_info(self):
        copy = []
        for x in self.data:
            if len(x) == 7:
                if x[5] == "\tPort Type: Audio Port\n":
                    copy.append(x)

        if copy is None:
            return ['N/A']

        aud  = []

        for i, y in enumerate(copy):
            if i > 0:
                aud.append(" ")
            aud.append("Audio Port %s" %i)
            for x in y:
                if x.startswith("\tInternal Reference Designator:"):
                    x = x[1:-1]
                    aud.append(x)
                elif x.startswith("\tInternal Connector Type:"):
                    x = x[1:-1]
                    aud.append(x)
                elif x.startswith("\tExternal Reference Designator:"):
                    x = x[1:-1]
                    aud.append(x)
                elif x.startswith("\tExternal Connector Type:"):
                    x = x[1:-1]
                    aud.append(x)

        return aud

    def aud_dev_info(self):
        with open("/opt/eInfo/info/auddevinfo") as file:
            data = file.readlines()
        copy = list(general.splitter(data, "*-", True))
        for x in copy:
            if x[0].startswith("  *-"):
                del x[0]
            for i in range(len(x)):
                if x[i].startswith("       "):
                    x[i] = x[i][7:]

        if copy is None:
            return ['N/A']

        aud = []

        for i, y in enumerate(copy):
            if i > 0:
                aud.append(" ")
            aud.append("Audio Device %s" %i)
            for x in y:
                if x.startswith("description:"):
                    x = x[:-1].title()
                    aud.append(x)
                elif x.startswith("product:"):
                    x = x[:-1].title()
                    aud.append(x)
                elif x.startswith("vendor:"):
                    x = x[:-1].title()
                    aud.append(x)
                elif x.startswith("physical id:"):
                    x = x[:-1].title()
                    aud.append(x)
                elif x.startswith("bus info:"):
                    x = x[:-1].title()
                    aud.append(x)
                elif x.startswith("version:"):
                    x = x[:-1].title()
                    aud.append(x)
                elif x.startswith("width:"):
                    x = x[:-1].title()
                    aud.append(x)
                elif x.startswith("clock:"):
                    x = x[:-1].capitalize()
                    aud.append(x)
                elif x.startswith("configuration:"):
                    aud.append("Configuration:")
                    interim = x.split()
                    del interim[0]
                    aud.append(interim)
                elif x.startswith("capabilities:"):
                    aud.append("Capabilities:")
                    interim = x.split()
                    del interim[0]
                    aud.append(interim)
                elif x.startswith("resources:"):
                    aud.append("Resources:")
                    interim = x.split()
                    del interim[0]
                    aud.append(interim)

        return aud

    def net_info(self):
        copy = []
        for x in self.data:
            if len(x) == 7:
                if x[5] == "\tPort Type: Network Port\n":
                    copy.append(x)

        for x in self.data:
            if len(x) == 7:
                if "802.11" in x[1] or "WiFi" in x[1] or "Ethernet" in x[1]:
                    copy.append(x)

        if copy is None:
            return ['N/A']

        net  = []

        for i, y in enumerate(copy):
            if y[0].startswith("Port Connector Information"):
                if i > 0:
                    net.append(" ")
                net.append("Network Port %s" %i)
                for x in y:
                    if x.startswith("\tInternal Reference Designator:"):
                        x = x[1:-1]
                        net.append(x)
                    elif x.startswith("\tInternal Connector Type:"):
                        x = x[1:-1]
                        net.append(x)
                    elif x.startswith("\tExternal Reference Designator:"):
                        x = x[1:-1]
                        net.append(x)
                    elif x.startswith("\tExternal Connector Type:"):
                        x = x[1:-1]
                        net.append(x)
            else:
                if i > 0:
                    net.append(" ")
                net.append("Network Device %s" %i)
                for x in y:
                    if x.startswith("\tReference Designation:"):
                        x = x[1:-1]
                        net.append(x)
                    elif x.startswith("\tType:"):
                        x = x[1:-1]
                        net.append(x)
                    elif x.startswith("\tStatus:"):
                        x = x[1:-1]
                        net.append(x)
                    elif x.startswith("\tType Instance:"):
                        x = x[1:-1]
                        net.append(x)
                    elif x.startswith("\tBus Address:"):
                        x = x[1:-1]
                        net.append(x)

        return net

    def net_dev_info(self):
        with open("/opt/eInfo/info/netdevinfo") as file:
            data = file.readlines()
        copy = list(general.splitter(data, "*-", True))
        for x in copy:
            if x[0].startswith("  *-"):
                del x[0]
            for i in range(len(x)):
                if x[i].startswith("       "):
                    x[i] = x[i][7:]

        if copy is None:
            return ['N/A']

        net = []

        for i, y in enumerate(copy):
            if i > 0:
                net.append(" ")
            net.append("Network Device %s" %i)
            for x in y:
                if x.startswith("description:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("product:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("vendor:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("physical id:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("bus info:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("logical name:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("version:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("serial:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("size:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("capacity:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("width:"):
                    x = x[:-1].title()
                    net.append(x)
                elif x.startswith("clock:"):
                    x = x[:-1].capitalize()
                    net.append(x)
                elif x.startswith("configuration:"):
                    net.append("Configuration:")
                    interim = x.split()
                    del interim[0]
                    net.append(interim)
                elif x.startswith("capabilities:"):
                    net.append("Capabilities:")
                    interim = x.split()
                    del interim[0]
                    net.append(interim)
                elif x.startswith("resources:"):
                    net.append("Resources:")
                    interim = x.split()
                    del interim[0]
                    net.append(interim)

        return net

    def net_int_loc_info(self):
        system("iwconfig > /opt/eInfo/info/netintlocinfo")
        with open("/opt/eInfo/info/netintlocinfo") as file:
            data = file.readlines()
        data.pop(-1)
        data.reverse()
        data.append("\n")
        data.reverse()
        copy = list(general.splitter(data, "\n"))
        for x in copy:
            if x[0] == "\n":
                del x[0]
            for i in range(len(x)):
                x[i] = x[i][9:]
                x[i] = x[i].replace("  ", "        ")

        if copy is None:
            return ['N/A']

        net = []

        for i, y in enumerate(copy):
            if i > 0:
                net.append(" ")
            net.append("Interface %s - Local Information" %i)
            for x in y:
                x = x[:-1]
                net.append(x)

        return net

    def net_int_rem_info(self):
        system("iwconfig > /opt/eInfo/info/netintreminfo")
        with open("/opt/eInfo/info/netintreminfo") as file:
            data = file.readlines()
        data.pop(-1)
        data.reverse()
        data.append("\n")
        data.reverse()
        copy = list(general.splitter(data, "\n"))
        for x in copy:
            if x[0] == "\n":
                del x[0]
            for i in range(len(x)):
                x[i] = x[i][9:]
                x[i] = x[i].replace("  ", "     ")

        if copy is None:
            return ['N/A']

        net = []

        for i, y in enumerate(copy):
            if i > 0:
                net.append(" ")
            net.append("Interface %s - Remote Information" %i)
            for x in y:
                x = x[:-1]
                net.append(x)

        return net
