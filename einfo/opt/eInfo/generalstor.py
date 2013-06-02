#!/usr/bin/env python
# encoding: utf-8
from os import system

"""                 eInfo
==============================================
    Contains Storage Information functions.

  Maintainer:    Anthony "AntCer" Cervantes
"""

blank = " "

class Partition_info():
    def __init__(self):
        with open("/proc/partitions") as file:
            data = file.readlines()
        del data[0];del data[0]
        for i, x in enumerate(data):
            data[i] = x.split()
        self.data = data
        self.num = len(data)

        system("df -T > /tmp/partinfo")
        with open("/tmp/partinfo") as file:
            tmpdata = file.readlines()
        del tmpdata[0]
        self.test = tmpdata[:]
        for i, x in enumerate(tmpdata):
            tmpdata[i] = x.split()
        self.tmpdata = tmpdata
        self.tmpnum = len(tmpdata)

    def rawdata(self, tmp=False):
        if tmp:
            return self.tmpdata
        else:
            return self.data

    def number(self, tmp=False):
        if tmp:
            return self.tmpnum
        else:
            return self.num

    def partition_name(self):
        partname = []
        partname.append('Name'.ljust(8))
        for i in range(self.num):
            name = self.data[i][3]
            partname.append(name.ljust(8))
        return partname

    def partition_size(self):
        partsize = []
        partsize.append('Total'.ljust(12))
        for i in range(self.num):
            size = int(self.data[i][2])/1024
            size = '{:,}'.format(size)
            size = size + " MB"
            partsize.append(size.ljust(12))
        return partsize

    def partition_type(self):
        parttype = []
        parttype.append('Type'.ljust(10))
        for x in self.data:
            if x[3].isalpha():
                parttype.append(blank.ljust(10))
            elif x[3] in "".join(self.test):
                for i in range(self.tmpnum):
                    if x[3] in self.tmpdata[i][0]:
                        parttype.append(self.tmpdata[i][1].ljust(10))
            else:
                parttype.append(blank.ljust(10))
        return parttype

    def partition_used(self):
        partused = []
        partused.append('Used'.ljust(12))
        for x in self.data:
            if x[3].isalpha():
                partused.append(blank.ljust(12))
            elif x[3] in "".join(self.test):
                for i in range(self.tmpnum):
                    if x[3] in self.tmpdata[i][0]:
                        used = int(self.tmpdata[i][3])/1024
                        used = '{:,}'.format(used)
                        used = used + " MB"
                        partused.append(used.ljust(12))
            else:
                partused.append(blank.ljust(12))
        return partused

    def partition_free(self):
        partfree = []
        partfree.append('Free'.ljust(12))
        for x in self.data:
            if x[3].isalpha():
                partfree.append(blank.ljust(12))
            elif x[3] in "".join(self.test):
                for i in range(self.tmpnum):
                    if x[3] in self.tmpdata[i][0]:
                        free = int(self.tmpdata[i][4])/1024
                        free = '{:,}'.format(free)
                        free = free + " MB"
                        partfree.append(free.ljust(12))
            else:
                partfree.append(blank.ljust(12))
        return partfree

    def partition_combined(self):
        name = self.partition_name()
        typ = self.partition_type()
        free = self.partition_free()
        used = self.partition_used()
        total = self.partition_size()

        partcomb = []

        for i in range(self.num):
            comb = "%s  |   %s  |   %s  |  %s   |  %s" %(name[i], typ[i], free[i], used[i], total[i])
            partcomb.append(comb)
        return partcomb




class Storage_info():
    def __init__(self):
        with open("/proc/scsi/sg/device_strs") as file:
            data = file.readlines()
        for i, x in enumerate(data):
            data[i] = x.split("\t")
        self.num = len(data)
        self.data = data

    def rawdata(self):
        return self.data

    def number(self):
        return self.num

    def vendor(self, entry=False, i=False):
        data = self.data[i]

        if entry:
            entry.entry_set(data[0])
        else:
            return data[0]

    def model(self, entry=False, i=False):
        data = self.data[i]

        if entry:
            entry.entry_set(data[1])
        else:
            return data[1]


    def revision(self, entry=False, i=False):
        data = self.data[i]

        if entry:
            entry.entry_set(data[2][:-1])
        else:
            return data[2][:-1]


