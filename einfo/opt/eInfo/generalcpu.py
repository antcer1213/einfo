#!/usr/bin/env python
# encoding: utf-8
import general

"""                 eInfo
==============================================
    Contains CPU Information functions.

  Maintainer:    Anthony "AntCer" Cervantes
"""

import os

def number_of_cpus(entry=False):
    try:
        num = os.sysconf("SC_NPROCESSORS_ONLN")
    except ValueError:
        num = 0

        with open("/proc/cpuinfo") as file:
            lines = file.readlines()

        for line in lines:
            if line.lower().startswith('processor'):
                num += 1

    if entry:
        entry.entry_set(str(num))
    else:
        return num


class CPU_info():
    def __init__(self):
        with open("/proc/cpuinfo") as file:
            data = file.readlines()
        data.reverse()
        data = list(general.splitter(data, "\n"))
        data.reverse()
        for lst in data:
            lst.reverse()
        self.num = len(data)
        self.data = data

    def rawdata(self):
        return self.data

    def number(self, entry=False):
        if entry:
            entry.entry_set(str(self.num))
        else:
            return self.num

    def vendor_id(self, entry, i):
        for x in self.data[i]:
            if x.startswith("vendor_id"):
                vendor = x.split(":")[1].lstrip(" ")
                break
        entry.entry_set(vendor)

    def cpu_arch(self, entry, i):
        for x in self.data[i]:
            if x.startswith("flags"):
                if " lm " in x:
                    entry.entry_set("64bit")
                else:
                    entry.entry_set("32bit")
                break

    def cpu_hvm(self, entry, i):
        for x in self.data[i]:
            if x.startswith("flags"):
                if " svm " in x:
                    entry.entry_set("True")
                elif " vmx " in x:
                    entry.entry_set("True")
                else:
                    entry.entry_set("False")
                break

    def model_name(self, entry, i):
        for x in self.data[i]:
            if x.startswith("model name"):
                name = x.split(":")[1].lstrip(" ")
                break
        entry.entry_set(name)

    def cpu_freq(self, entry, i):
        for x in self.data[i]:
            if x.startswith("cpu MHz"):
                freq = "%s MHz" %x.split(":")[1].lstrip(" ")
                break
        entry.entry_set(freq)

    def cache_size(self, entry, i):
        for x in self.data[i]:
            if x.startswith("cache size"):
                cache = x.split(":")[1].lstrip(" ")
                break
        entry.entry_set(cache)

    def addr_sizes(self, entry, i):
        for x in self.data[i]:
            if x.startswith("address sizes"):
                sizes = x.split(":")[1].lstrip(" ")
                break
        entry.entry_set(sizes)

    def bogomips(self, entry, i):
        for x in self.data[i]:
            if x.startswith("bogomips"):
                bogo = x.split(":")[1].lstrip(" ")
                break
        entry.entry_set(bogo)

    def numbering(self, entry, i):
        for x in self.data[i]:
            if x.startswith("cpu family"):
                fam = x.split(":")[1].lstrip(" ")
                break
        for x in self.data[i]:
            if x.startswith("model		:"):
                mod = x.split(":")[1].lstrip(" ")
                break
        for x in self.data[i]:
            if x.startswith("stepping"):
                step = x.split(":")[1].lstrip(" ")
                break
        for x in self.data[i]:
            if x.startswith("cpu cores"):
                cor = x.split(":")[1].lstrip(" ")
                break
        for x in self.data[i]:
            if x.startswith("physical id"):
                pid = x.split(":")[1].lstrip(" ")
                break
        entry.entry_set("Family(%s), Model(%s), Stepping(%s) | Cores=%s | Phys ID=%s" %(fam, mod, step, cor, pid))

    def flags(self, entry, i):
        for x in self.data[i]:
            if x.startswith("flags"):
                flags = x.split(":")[1].lstrip(" ")
                break
        entry.entry_set(flags)

    def icon(self, i):
        data = self.data[i]

        if "AMD" in data[1]:
            return "/opt/eInfo/images/amd.jpg"
        elif "Intel" in data[1]:
            return "/opt/eInfo/images/intel.jpg"
        elif "Via" or "Centaur" in data[1]:
            return "/opt/eInfo/images/via.jpg"
        else:
            return "none"
