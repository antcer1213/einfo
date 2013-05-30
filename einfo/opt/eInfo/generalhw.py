#!/usr/bin/env python
# encoding: utf-8
import general
import dmidecode
from os import system, listdir
import socket, struct, fcntl
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd = sock.fileno()
from decimal import Decimal, getcontext
getcontext().prec = 4

"""                 eInfo
==============================================
    Contains Hardware Information functions.

  Maintainer:    Anthony "AntCer" Cervantes
"""


class Hardware_Info():
    def __init__(self):
        pass

    def mobo_info(self):
        data = dmidecode.baseboard().values()
        mobo = []

        for v in data:
            if v['dmi_type'] == 2: #Motherboard
                mobo.append("Manufacturer: %s" %(v['data']['Manufacturer']))
                mobo.append("Product Name: %s" %(v['data']['Product Name']))
                mobo.append("Version: %s" %(v['data']['Version']))
                mobo.append("Serial Number: %s" %(v['data']['Serial Number']))
                break

        return mobo

    def bios_info(self):
        data = dmidecode.bios().values()
        char = []

        for v in data:
            if v['dmi_type'] == 0: #BIOS
                ven    = "Vendor: %s" %(v['data']['Vendor'])
                ver    = "Version: %s" %(v['data']['Version'])
                rel    = "Release Date: %s" %(v['data']['Relase Date'])
                runsiz = "Runtime Size: %s" %(v['data']['Runtime Size'])
                romsiz = "ROM Size: %s" %(v['data']['ROM Size'])
                birev  = "BIOS Revision: %s" %(v['data']['BIOS Revision'])
                addr   = "Address: %s" %(v['data']['Address'])
                char0  = v['data']['Characteristics']
                char1  = v['data']['Characteristic x1']
                char2  = v['data']['Characteristic x2']
            if v['dmi_type'] == 13: #BIOS Language
                currlang = v['data']['Currently Installed Language']
                lan      = "Number of Languages: %s" %(v['data']['Installed Languages'])

        for x in char0.keys():
            char.append("%s: %s" %(x, char0[x]))

        for x in char1.keys():
            char.append("%s: %s" %(x, char1[x]))

        for x in char2.keys():
            char.append("%s: %s" %(x, char2[x]))


        return [ven, ver, rel, runsiz, romsiz, birev, addr, lan, "Installed Languages:", currlang, "Characteristics:", char]


    def sys_info(self):
        data = dmidecode.system().values()
        sys = []

        for v in data:
            if v['dmi_type'] == 1: #System
                sys.append("Manufacturer: %s" %(v['data']['Manufacturer']))
                sys.append("Product Name: %s" %(v['data']['Product Name']))
                sys.append("Version: %s" %(v['data']['Version']))
                sys.append("Serial Number: %s" %(v['data']['Serial Number']))
                sys.append("UUID: %s" %(v['data']['UUID']))
                sys.append("Wake-up Type: %s" %(v['data']['Wake-Up Type']))
                sys.append("SKU Number: %s" %(v['data']['SKU Number']))
                sys.append("Family: %s" %(v['data']['Family']))


        return sys


    def pci_info(self):
        data = open("/usr/share/misc/pci.ids").readlines()
        data1 = open("/proc/bus/pci/devices").readlines()
        data2 = listdir("/sys/bus/pci/devices")
        vdid = []
        pci = []
        pcinum = 0

        for v in data1:
            vdid.append(v.split()[1])

        for v in vdid:
            if pcinum > 0:
                pci.append(" ")
            VID = v[0:4]
            pci.append("Vendor ID: %s" %VID)
            DID = v[4:]
            pci.append("Device ID: %s" %DID)
            pcinum += 1
            for i, v in enumerate(data):
                if v.startswith("#"):
                    pass
                elif v.startswith("\t"):
                    pass
                elif not v.split() == []:
                    if v.split()[0] == VID:
                        tmp = v.split()
                        del tmp[0]
                        pci.append("Vendor: %s" %" ".join(tmp))
                        num = i + 1
                        while not DID == data[num][1:].split()[0]:
                            num += 1
                        tmp = data[num][1:].split()
                        del tmp[0]
                        pci.append("Device: %s" %" ".join(tmp))
                        while data[num+1].startswith("\t\t"):
                            tmp = data[num+1][2:].split()
                            #~ print pcinum
                            #~ print data2[pcinum-1]
                            #~ print open("/sys/bus/pci/devices/%s/subsystem_vendor"%data2[pcinum-1]).readline()[2:-1]
                            #~ print tmp[0]
                            if open("/sys/bus/pci/devices/%s/subsystem_vendor"%data2[pcinum-1]).readline()[2:-1] == tmp[0] and open("/sys/bus/pci/devices/%s/subsystem_device"%data2[pcinum-1]).readline()[2:-1] == tmp[1]:
                                del tmp[0] ; del tmp[0]
                                pci.append("Subsystem: %s" %" ".join(tmp))
                            num += 1
                    else:
                        pass



        return pci


    def mem_info(self):
        data = dmidecode.memory().values()
        mem = []
        arraynum = 0
        memnum = 0

        for v in data:
            if v['dmi_type'] == 16: #Physical Memory Array
                if arraynum > 0:
                    mem.append(" ")
                mem.append("Physical Memory Array %s" %arraynum)
                mem.append("Location: %s" %(v['data']['Location']))
                mem.append("Error Correction Type: %s" %(v['data']['Error Correction Type']))
                mem.append("Maximum Capacity: %s" %(v['data']['Maximum Capacity']))
                mem.append("Number Of Devices: %s" %(v['data']['Number Of Devices']))

                arraynum += 1
            if v['dmi_type'] == 17: #Memory Device
                mem.append(" ")
                mem.append("Memory Device %s" %memnum)
                mem.append("Size: %s" %(v['data']['Size']))
                mem.append("Form Factor: %s" %(v['data']['Form Factor']))
                mem.append("Type: %s" %(v['data']['Type']))
                mem.append("Speed: %s" %(v['data']['Speed']))
                mem.append("Manufacturer: %s" %(v['data']['Manufacturer']))
                mem.append("Locator: %s" %(v['data']['Locator']))
                mem.append("Bank Locator: %s" %(v['data']['Bank Locator']))
                mem.append("Data Width: %s" %(v['data']['Data Width']))
                mem.append("Total Width: %s" %(v['data']['Total Width']))
                mem.append("Serial Number: %s" %(v['data']['Serial Number']))
                mem.append("Part Number: %s" %(v['data']['Part Number']))
                #~ mem.append("Configured Clock Speed: %s" %(v['data']['Configured Clock Speed']))
                #~ mem.append("Rank: %s" %(v['data']['Rank']))
                mem.append("Type Detail:")
                typedetail = []
                for x in v['data']['Type Detail']:
                    if not x == None:
                        typedetail.append(x)
                mem.append(typedetail)

                memnum += 1

        return mem


    def bat_info(self):
        data = dmidecode.type(22)
        bat = []

        for v in data.keys():
            if type(data[v]) == dict: #Portable Battery
                v = data[v]
                bat.append("Name: %s" %(v['data']['Name']))
                bat.append("Manufacturer: %s" %(v['data']['Manufacturer']))
                bat.append("Location: %s" %(v['data']['Location']))
                bat.append("Chemistry: %s" %(v['data']['SBDS Chemistry']))
                bat.append("Design Capacity: %s" %(v['data']['Design Capacity']))
                bat.append("Design Voltage: %s" %(v['data']['Design Voltage']))
                bat.append("Maximum Error: %s" %(v['data']['Maximum Error']))
                bat.append("Version: %s" %(v['data']['SBDS Version']))
                bat.append("Serial Number: %s" %(v['data']['SBDS Serial Number']))
                bat.append("Manufacture Date: %s" %(v['data']['SBDS Manufacture Date']))

        return bat


    def vid_info(self):
        data = dmidecode.connector().values()
        vid = []
        vidport = 0

        for v in data:
            if v['dmi_type'] == 8 and v['data']['Port Type'] == "Video Port": #Video Port
                if vidport > 0:
                    vid.append(" ")
                vid.append("Video Port %s" %vidport)
                vid.append("Internal Reference Designator: %s" %(v['data']['Internal Reference Designator']))
                vid.append("Internal Connector Type: %s" %(v['data']['Internal Connector Type']))
                vid.append("External Reference Designator: %s" %(v['data']['External Reference Designator']))
                vid.append("External Connector Type: %s" %(v['data']['External Connector Type']))

                vidport += 1

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
        data = dmidecode.connector().values()
        aud = []
        audport = 0

        for v in data:
            if v['dmi_type'] == 8 and v['data']['Port Type'] == "Audio Port": #Audio Port
                if audport > 0:
                    aud.append(" ")
                aud.append("Audio Port %s" %audport)
                aud.append("Internal Reference Designator: %s" %(v['data']['Internal Reference Designator']))
                aud.append("Internal Connector Type: %s" %(v['data']['Internal Connector Type']))
                aud.append("External Reference Designator: %s" %(v['data']['External Reference Designator']))
                aud.append("External Connector Type: %s" %(v['data']['External Connector Type']))

                audport += 1

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
        data1 = dmidecode.connector().values()
        data2 = dmidecode.baseboard().values()
        #~ data2 = dmidecode.QueryTypeId(41) ; print data2

        net = []
        netport = 0
        netdev  = 0

        for v in data1:
            if v['dmi_type'] == 8 and v['data']['Port Type'] == "Network Port": #Network Port
                if netport > 0:
                    net.append(" ")
                net.append("Network Port %s" %netport)
                net.append("Internal Reference Designator: %s" %(v['data']['Internal Reference Designator']))
                net.append("Internal Connector Type: %s" %(v['data']['Internal Connector Type']))
                net.append("External Reference Designator: %s" %(v['data']['External Reference Designator']))
                net.append("External Connector Type: %s" %(v['data']['External Connector Type']))

                netport += 1

        for v in data2:
            if v['dmi_type'] == 41:
                chk = v['data']['Reference Designation']
                if "802.11" in chk or "WiFi" in chk or "Ethernet" in chk:
                    if netport > 0:
                        net.append(" ")
                    net.append("Network Device %s" %netdev)
                    net.append("Name: %s" %(v['data']['Reference Designation']))
                    net.append("Status: %s" %(v['data']['Status']))
                    net.append("Type: %s" %(v['data']['Type']))
                    net.append("Type Instance: %s" %(v['data']['Type Instance']))
                    net.append("Bus Address: %s" %(v['data']['Bus Address']))

                    netdev += 1

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
        data = listdir("/sys/class/net/")

        net = []

        for i, x in enumerate(data):
            if i > 0:
                net.append("<SEP> ")
            net.append("Interface %s" %i)
            net.append("Name: %s" %x)
            net.append("HW Address: %s" %(open("/sys/class/net/%s/address" %x).readline()[:-1]))
            if self.get_ip(x):
                net.append("IPv4 Address: %s" %(self.get_ip(x)))
            if self.get_ip6(x):
                net.append("IPv6 Address: %s" %(self.get_ip6(x)))
            if self.get_brdcst(x):
                net.append("Broadcast: %s" %(self.get_brdcst(x)))
            if self.get_netmsk(x):
                net.append("Netmask: %s" %(self.get_netmsk(x)))
            net.append("TX Queue Len: %s" %(open("/sys/class/net/%s/tx_queue_len" %x).readline()[:-1]))
            net.append("MTU: %s" %(open("/sys/class/net/%s/mtu" %x).readline()[:-1]))
            net.append("Collisions: %s" %(open("/sys/class/net/%s/statistics/collisions" %x).readline()[:-1]))
            net.append("RX:")
            B = Decimal(int(open("/sys/class/net/%s/statistics/rx_bytes" %x).readline()[:-1]))
            if B >= 1000 and B < 1000000:
                B = str(B) + " (%s KB)"%(B/1000)
            elif B >= 1000000 and B < 1000000000:
                B = str(B) + " (%s MB)"%(B/1000000)
            elif B >= 1000000000:
                B = str(B) + " (%s GB)"%(B/1000000000)
            else:
                B = str(B)
            net.append(["Bytes: %s"%(B), "Packets: %s"%open("/sys/class/net/%s/statistics/rx_packets" %x).readline()[:-1], "Errors: %s"%open("/sys/class/net/%s/statistics/rx_errors" %x).readline()[:-1], "Dropped: %s"%open("/sys/class/net/%s/statistics/rx_dropped" %x).readline()[:-1], "Overruns: %s"%open("/sys/class/net/%s/statistics/rx_over_errors" %x).readline()[:-1], "Frame: %s"%open("/sys/class/net/%s/statistics/rx_frame_errors" %x).readline()[:-1]])
            net.append("TX:")
            B = Decimal(int(open("/sys/class/net/%s/statistics/tx_bytes" %x).readline()[:-1]))
            if B >= 1000 and B < 1000000:
                B = str(B) + " (%s KB)"%(B/1000)
            elif B >= 1000000 and B < 1000000000:
                B = str(B) + " (%s MB)"%(B/1000000)
            elif B >= 1000000000:
                B = str(B) + " (%s GB)"%(B/1000000000)
            else:
                B = str(B)
            net.append(["Bytes: %s"%(B), "Packets: %s"%open("/sys/class/net/%s/statistics/tx_packets" %x).readline()[:-1], "Errors: %s"%open("/sys/class/net/%s/statistics/tx_errors" %x).readline()[:-1], "Dropped: %s"%open("/sys/class/net/%s/statistics/tx_dropped" %x).readline()[:-1], "Carrier: %s"%open("/sys/class/net/%s/statistics/tx_carrier_errors" %x).readline()[:-1]])

        return net


    def net_int_rem_info(self):
        data = listdir("/sys/class/net/")

        net = []

        for i, x in enumerate(data):
            if i > 0:
                net.append("<SEP> ")
            net.append("Interface %s" %i)
            net.append("Name: %s" %x)
            if self.get_gwip(x):
                net.append("Gateway IP Address: %s" %(self.get_gwip(x)))
            if self.get_gwmac(x):
                net.append("Gateway HW Address: %s" %(self.get_gwmac(x)))

        return net

#~ -----------------------------------------
#~      Network Info Parsing Functions
#~------------------------------------------
    def get_ip(self, iface):
        SIOCGIFADDR = 0x8915

        ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
        try:
            res = fcntl.ioctl(sockfd, SIOCGIFADDR, ifreq)
        except:
            return None
        ip = struct.unpack('16sH2x4s8x', res)[2]
        return socket.inet_ntoa(ip)

    def get_brdcst(self, iface):
        SIOCGIFBRDADDR = 0x8919

        ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
        try:
            res = fcntl.ioctl(sockfd, SIOCGIFBRDADDR, ifreq)
        except:
            return None
        ip = struct.unpack('16sH2x4s8x', res)[2]
        return socket.inet_ntoa(ip)

    def get_netmsk(self, iface):
        SIOCGIFNETMASK = 0x891b

        ifreq = struct.pack('16sH14s', iface, socket.AF_INET, '\x00'*14)
        try:
            res = fcntl.ioctl(sockfd, SIOCGIFNETMASK, ifreq)
        except:
            return None
        ip = struct.unpack('16sH2x4s8x', res)[2]
        return socket.inet_ntoa(ip)

    def get_macaddr(self, iface):
        SIOCGIFHWADDR = 0x8927

        ifreq = struct.pack('16sH14s', iface, 1, '\x00'*14)
        try:
            res = fcntl.ioctl(sockfd, SIOCGIFHWADDR, ifreq)
        except:
            return None
        address = struct.unpack('16sH14s', res)[2]
        mac = struct.unpack('6B8x', address)

        return ":".join(['%02X' % i for i in mac])

    def get_essid(self, iface):
        SIOCGIFHWADDR = 0x8927

        ifreq = struct.pack('16sH14s', iface, 1, '\x00'*14)
        try:
            res = fcntl.ioctl(sockfd, SIOCGIFHWADDR, ifreq)
        except:
            return None
        address = struct.unpack('16sH14s', res)[2]
        mac = struct.unpack('6B8x', address)

        return ":".join(['%02X' % i for i in mac])

    def get_ip6(self, iface):
        inet6lst = open("/proc/net/if_inet6").readlines()
        for i, x in enumerate(inet6lst):
            inet6lst[i] = x.split()

        inet6 = None

        for line in inet6lst:
            if iface == line[-1]:
                inet6 = line[0]

        return inet6

    def get_gwip(self, iface):
        octet_list = []
        gw_from_route = None
        f = open('/proc/net/route').readlines()
        for line in f:
            words = line.split()
            dest = words[1]
            try:
                if words[0] == iface and int(dest) == 0:
                    gw_from_route = words[2]
                    break
            except ValueError:
                pass

        if not gw_from_route:
            return None

        for i in range(8, 1, -2):
            octet = gw_from_route[i-2:i]
            octet = int(octet, 16)
            octet_list.append(str(octet))

        gw_ip = ".".join(octet_list)

        return gw_ip

    def get_gwmac(self, iface):
        gwmac = None

        f = open('/proc/net/arp').readlines()
        for line in f:
            words = line.split()
            words.reverse()
            if words[0] == iface:
                gwmac = words[2]
                break

        return gwmac
