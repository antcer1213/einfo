#!/usr/bin/env python
# encoding: utf-8

"""                 eInfo
==============================================
    Contains Memory Information functions.

  Maintainer:    Anthony "AntCer" Cervantes
"""

from decimal import Decimal, getcontext
getcontext().prec = 4

class Memory_Info():
    def __init__(self, scale=False):
        self.scale = scale

        with open("/proc/meminfo") as file:
            self.data = file.readlines()

    def mem(self, pure=False):
        #~ getcontext().prec = 10
        data = self.data

        total = Decimal(int(data[0].split()[1]))
        free = Decimal(int(data[1].split()[1]))
        used = total - free

        if pure:
            for x in data:
                if x.startswith("Buffers"):
                    buffers = Decimal(int(x.split()[1]))
                    break
            for x in data:
                if x.startswith("Cached"):
                    cached = Decimal(int(x.split()[1]))
                    break

            used = used - (buffers + cached)

        return used/total

    def swap(self):
        #~ getcontext().prec = 10
        data = self.data

        for x in data:
            if x.startswith("SwapTotal"):
                total = Decimal(int(x.split()[1]))
                break
        for x in data:
            if x.startswith("SwapFree"):
                free = Decimal(int(x.split()[1]))
                break
        used = total - free

        return used/total

    def memtotal(self, entry):
        scale = self.scale
        data = self.data

        total = int(data[0].split()[1])

        if scale == "GB":
            total = '{:,}'.format(Decimal(total)/1048576)
            entry.entry_set("%s GB" % total)
        elif scale == "MB":
            total = '{:,}'.format(total/1024)
            entry.entry_set("%s MB" % total)
        else:
            total = '{:,}'.format(total)
            entry.entry_set("%s KB" % total)

    def memfree(self, entry, pure=False):
        scale = self.scale
        data = self.data

        free = int(data[1].split()[1])

        if pure:
            for x in data:
                if x.startswith("Buffers"):
                    buffers = int(x.split()[1])
                    break
            for x in data:
                if x.startswith("Cached"):
                    cached = int(x.split()[1])
                    break

            free = free + buffers + cached

        if scale == "GB":
            free = '{:,}'.format(Decimal(free)/1048576)
            entry.entry_set("%s GB" % free)
        elif scale == "MB":
            free = '{:,}'.format(free/1024)
            entry.entry_set("%s MB" % free)
        else:
            free = '{:,}'.format(free)
            entry.entry_set("%s KB" % free)

    def memused(self, entry, pure=False):
        scale = self.scale
        data = self.data

        total = int(data[0].split()[1])
        free = int(data[1].split()[1])
        used = total - free

        if pure:
            for x in data:
                if x.startswith("Buffers"):
                    buffers = int(x.split()[1])
                    break
            for x in data:
                if x.startswith("Cached"):
                    cached = int(x.split()[1])
                    break

            used = used - (buffers + cached)

        if scale == "GB":
            used = '{:,}'.format(Decimal(used)/1048576)
            entry.entry_set("%s GB" % used)
        elif scale == "MB":
            used = '{:,}'.format(used/1024)
            entry.entry_set("%s MB" % used)
        else:
            used = '{:,}'.format(used)
            entry.entry_set("%s KB" % used)

    def swaptotal(self, entry):
        scale = self.scale
        data = self.data

        for x in data:
            if x.startswith("SwapTotal"):
                total = int(x.split()[1])
                break

        if scale == "GB":
            total = '{:,}'.format(Decimal(total)/1048576)
            entry.entry_set("%s GB" % total)
        elif scale == "MB":
            total = '{:,}'.format(total/1024)
            entry.entry_set("%s MB" % total)
        else:
            total = '{:,}'.format(total)
            entry.entry_set("%s KB" % total)

    def swapfree(self, entry):
        scale = self.scale
        data = self.data

        for x in data:
            if x.startswith("SwapFree"):
                free = int(x.split()[1])
                break

        if scale == "GB":
            free = '{:,}'.format(Decimal(free)/1048576)
            entry.entry_set("%s GB" % free)
        elif scale == "MB":
            free = '{:,}'.format(free/1024)
            entry.entry_set("%s MB" % free)
        else:
            free = '{:,}'.format(free)
            entry.entry_set("%s KB" % free)

    def swapused(self, entry):
        scale = self.scale
        data = self.data

        for x in data:
            if x.startswith("SwapTotal"):
                total = int(x.split()[1])
                break
        for x in data:
            if x.startswith("SwapFree"):
                free = int(x.split()[1])
                break
        used = total - free

        if scale == "GB":
            used = '{:,}'.format(Decimal(used)/1048576)
            entry.entry_set("%s GB" % used)
        elif scale == "MB":
            used = '{:,}'.format(used/1024)
            entry.entry_set("%s MB" % used)
        else:
            used = '{:,}'.format(used)
            entry.entry_set("%s KB" % used)

    def buffers(self, entry):
        scale = self.scale
        data = self.data

        for x in data:
            if x.startswith("Buffers"):
                buffers = int(x.split()[1])
                break

        if scale == "GB":
            buffers = '{:,}'.format(Decimal(buffers)/1048576)
            entry.entry_set("%s GB" % buffers)
        elif scale == "MB":
            buffers = '{:,}'.format(buffers/1024)
            entry.entry_set("%s MB" % buffers)
        else:
            buffers = '{:,}'.format(buffers)
            entry.entry_set("%s KB" % buffers)

    def cached(self, entry):
        scale = self.scale
        data = self.data

        for x in data:
            if x.startswith("Cached"):
                cached = int(x.split()[1])
                break

        if scale == "GB":
            cached = '{:,}'.format(Decimal(cached)/1048576)
            entry.entry_set("%s GB" % cached)
        elif scale == "MB":
            cached = '{:,}'.format(cached/1024)
            entry.entry_set("%s MB" % cached)
        else:
            cached = '{:,}'.format(cached)
            entry.entry_set("%s KB" % cached)

    def active(self, entry):
        scale = self.scale
        data = self.data

        for x in data:
            if x.startswith("Active:"):
                act = int(x.split()[1])
                break

        if scale == "GB":
            act = '{:,}'.format(Decimal(act)/1048576)
            entry.entry_set("%s GB" % act)
        elif scale == "MB":
            act = '{:,}'.format(act/1024)
            entry.entry_set("%s MB" % act)
        else:
            act = '{:,}'.format(act)
            entry.entry_set("%s KB" % act)

    def inactive(self, entry):
        scale = self.scale
        data = self.data

        for x in data:
            if x.startswith("Inactive:"):
                inact = int(x.split()[1])
                break

        if scale == "GB":
            inact = '{:,}'.format(Decimal(inact)/1048576)
            entry.entry_set("%s GB" % inact)
        elif scale == "MB":
            inact = '{:,}'.format(inact/1024)
            entry.entry_set("%s MB" % inact)
        else:
            inact = '{:,}'.format(inact)
            entry.entry_set("%s KB" % inact)
