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
        from os import system

        self.data = data = []

        with open("/proc/partitions") as file:
            for i, x in enumerate(file):
                if i > 1:
                    data.append(x.split())

        self.num = len(data)


        self.mnt_data = mnt_data = []

        with open("/etc/mtab") as file:
            mtab = file.readlines()
        for i in range(self.num):
            name = data[i][3]
            if not name.isalpha():
                if name in " ".join(mtab):
                    for x in mtab:
                        if name in x:
                            mnt_data.append(x.split()[1:3])
                else:
                    mnt_data.append(None)
            else:
                mnt_data.append(None)


        self.stat_data = stat_data = []

        for x in mnt_data:
            if x is None:
                stat_data.append(None)
            else:
                stat_data.append(self.usage_stats(x[0]))


    def usage_stats(self, path):
        from os import statvfs

        def percentage(used, total, increment):
            try:
                perc = (used / total) * 100
            except:
                perc = 0

            return round(perc, increment)

        info = statvfs(path)
        free = (info.f_bavail * info.f_frsize)
        total = (info.f_blocks * info.f_frsize)
        used = (info.f_blocks - info.f_bfree) * info.f_frsize
        percent = percentage(used, total, 1)
        # NB: the percentage is -5% than what shown by df due to
        # reserved blocks that we are currently not considering:
        # http://goo.gl/sWGbH
        return [total, used, free, percent]

    def rawdata(self, data=False, mnt=False, stat=False):
        if data and mnt and stat:
            return self.data, self.mnt_data, self.stat_data
        elif mnt and stat:
            return self.mnt_data, self.stat_data
        elif mnt:
            return self.mnt_data
        elif stat:
            return self.stat_data
        else:
            return self.data

    def number(self):
        return self.num

    def partition_name(self, tb=False):
        partname = []
        if tb:
            for i in range(self.num):
                index = str(i)
                index = {}
                index['Category0'] = "<b>Name</b>"
                index['Category1'] = "<b>Device</b>"
                index['Category2'] = "<b>Mounted</b>"
                index['Name'] = self.data[i][3]
                index['Device Path'] = "/dev/%s"%self.data[i][3]
                if self.mnt_data[i] is None:
                    index['Mount Point'] = None
                else:
                    index['Mount Point'] = self.mnt_data[i][0]
                partname.append(index)
        else:
            partname.append('Name'.ljust(8))
            for i in range(self.num):
                name = self.data[i][3]
                partname.append(name.ljust(8))

        return partname

    def partition_size(self, tb=False):
        partsize = []

        if tb:
            for i in range(self.num):
                index = str(i)
                index = {}
                index['Category'] = "<b>Total</b>"
                size = int(self.data[i][2])/1024
                strsiz = '{:,}'.format(size)
                index['Total(MB)'] = strsiz + " MB"
                size = round(round(int(self.data[i][2]), 4)/1048576, 2)
                strsiz = '{:,}'.format(size)
                index['Total(GB)'] = strsiz + " GB"
                partsize.append(index)
        else:
            partsize.append('Total'.ljust(12))
            for i in range(self.num):
                size = int(self.data[i][2])/1024
                size = '{:,}'.format(size)
                size = size + " MB"
                partsize.append(size.ljust(12))

        return partsize

    def partition_type(self, tb=False):
        parttype = []

        if tb:
            for i in range(self.num):
                index = str(i)
                index = {}
                index['Category'] = "<b>Type</b>"
                if self.mnt_data[i] is None:
                    index['Type'] = None
                else:
                    index['Type'] = self.mnt_data[i][1]
                parttype.append(index)
        else:
            parttype.append('Type'.ljust(10))
            for i in range(self.num):
                if self.mnt_data[i] is None:
                    parttype.append(blank.ljust(10))
                else:
                    ftype = self.mnt_data[i][1]
                    parttype.append(ftype.ljust(10))

        return parttype

    def partition_used(self, tb=False):
        partused = []

        if tb:
            for i in range(self.num):
                index = str(i)
                index = {}
                index['Category'] = "<b>Used</b>"
                if self.stat_data[i] is None:
                    index['Used(MB)'] = None
                    index['Used(GB)'] = None
                else:
                    index['Used(MB)'] = '{:,}'.format(self.stat_data[i][1]/1048576) + " MB"
                    index['Used(GB)'] = '{:,}'.format(round(round(self.stat_data[i][1], 4)/1073741824, 2)) + " GB"
                partused.append(index)
        else:
            partused.append('Used'.ljust(12))
            for i in range(self.num):
                if self.stat_data[i] is None:
                    partused.append(blank.ljust(12))
                else:
                    used = int(self.stat_data[i][1])/1048576
                    used = '{:,}'.format(used)
                    used = used + " MB"
                    partused.append(used.ljust(12))

        return partused

    def partition_free(self, tb=False):
        partfree = []

        if tb:
            for i in range(self.num):
                index = str(i)
                index = {}
                index['Category'] = "<b>Free</b>"
                if self.stat_data[i] is None:
                    index['Free(MB)'] = None
                    index['Free(GB)'] = None
                else:
                    index['Free(MB)'] = '{:,}'.format(self.stat_data[i][2]/1048576) + " MB"
                    index['Free(GB)'] = '{:,}'.format(round(round(self.stat_data[i][2], 4)/1073741824, 2)) + " GB"
                partfree.append(index)
        else:
            partfree.append('Free'.ljust(12))
            for i in range(self.num):
                if self.stat_data[i] is None:
                    partfree.append(blank.ljust(12))
                else:
                    free = int(self.stat_data[i][2])/1048576
                    free = '{:,}'.format(free)
                    free = free + " MB"
                    partfree.append(free.ljust(12))

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

    def partition_table_comb(self, win, box):
        from evas import EVAS_HINT_FILL, EVAS_HINT_EXPAND
        from elementary import Scroller

        table = self.create_table("MB", win, box)

        sc = Scroller(win)
        sc.content_set(table)
        sc.policy_set(0, 0)
        sc.size_hint_weight_set(EVAS_HINT_EXPAND, EVAS_HINT_EXPAND)
        sc.size_hint_align_set(EVAS_HINT_FILL, EVAS_HINT_FILL)
        box.pack_end(sc)
        sc.show()

        return table

    def create_table(self, scale, win, box= False, table=False):
        from evas import EVAS_HINT_FILL, EVAS_HINT_EXPAND
        from elementary import Table, Label

        def label(win, label):
            lb = Label(win)
            lb.size_hint_weight_set(EVAS_HINT_EXPAND, 0.0)
            if label is None:
                pass
            elif " MB" in label or " GB" in label or "Free" in label or "Used" in label or "Total" in label:
                lb.size_hint_align_set(1.0, EVAS_HINT_FILL)
            else:
                lb.size_hint_align_set(-1.0, EVAS_HINT_FILL)
            lb.text = label
            lb.show()
            return lb

        name  = self.partition_name(True)
        typ   = self.partition_type(True)
        free  = self.partition_free(True)
        used  = self.partition_used(True)
        total = self.partition_size(True)

        if table:
            table.clear(True)
        else:
            table = Table(win)
            table.padding_set(0, 1)
            table.size_hint_weight_set(EVAS_HINT_EXPAND, EVAS_HINT_EXPAND)
            table.size_hint_align_set(EVAS_HINT_FILL, EVAS_HINT_FILL)
            #~ table.homogeneous_set(True)
            table.show()

        table.pack(label(win,  name[0]['Category0']), 0, 0, 1, 1)
        table.pack(label(win,   typ[0]['Category']),  1, 0, 1, 1)
        table.pack(label(win,  name[0]['Category1']), 2, 0, 1, 1)
        table.pack(label(win,  name[0]['Category2']), 3, 0, 1, 1)
        table.pack(label(win,  free[0]['Category']),  4, 0, 1, 1)
        table.pack(label(win,  used[0]['Category']),  5, 0, 1, 1)
        table.pack(label(win, total[0]['Category']),  6, 0, 1, 1)

        for i in range(self.num):
            table.pack(label(win,  name[i]['Name']),        0, i+1, 1, 1)
            table.pack(label(win,   typ[i]['Type']),        1, i+1, 1, 1)
            table.pack(label(win,  name[i]['Device Path']), 2, i+1, 1, 1)
            table.pack(label(win,  name[i]['Mount Point']), 3, i+1, 1, 1)
            table.pack(label(win,  free[i]['Free(%s)'%scale]),    4, i+1, 1, 1)
            table.pack(label(win,  used[i]['Used(%s)'%scale]),    5, i+1, 1, 1)
            table.pack(label(win, total[i]['Total(%s)'%scale]),   6, i+1, 1, 1)

        return table


class Storage_info():
    def __init__(self, ecore=False):
        import showsmart as smart
        self.data = {}
        devices = smart.get_block_devices()
        self.num = len(devices)
        for dev in devices:
            if ecore:
                self.data[dev] = smart.process_device(dev, self.receive_processed_data, "ecore")
            else:
                self.data[dev] = smart.process_device(dev, self.receive_processed_data)
    def number(self,values=False):
        if values:
            try:
                return self.valuenum
            except:
                self.valuenum = len(self.data[self.data.keys()[0]].values())
                return self.valuenum
        return self.num
    def devices(self):
        return self.data.keys();
    def receive_processed_data(self, dev, data):
        self.data[dev]= data
    def return_data(self, i=False, entries=False):
        if entries:
            data = self.data[self.data.keys()[i]]
            for r in range(len(entries)):
                entries[r].entry_set(data.values()[r])
        else:
            return self.data
    def return_list(self,i=0):
        info_keys0 = [x for x in self.data[self.devices()[i]]['info'].keys() if self.data[self.devices()[i]]['info'][x] != False]
        stat_keys0 = [x for x in self.data[self.devices()[i]]['stats'].keys() if self.data[self.devices()[i]]['stats'][x] != False]

        info_keys = []
        stat_keys = []
        for x in self.return_info_keys():
            if x in info_keys0:
                info_keys.append(x)
        for x in self.return_stat_keys():
            if x in stat_keys0:
                stat_keys.append(x)

        list_items = ['Information']
        for key in info_keys:
            list_items.append("%s : %s"%(key, self.data[self.devices()[i]]['info'][key]))
        list_items.append("")
        list_items.append("SMART Statistics")
        list_items.append("Health Status : %s"%self.data[self.devices()[i]]['stats']['Health Status'])
        for key in stat_keys:
            if key != "Health Status":
                list_items.append("%s : %s"%(key, self.data[self.devices()[i]]['stats'][key]))
        return list_items
    def return_info_keys(self):
        #~ data['info']['Device is'] = get_param_from_smart(d,"Device is:",delimiter=":")
        return ['Model Family','Device Model','Serial Number','LU WWN Device ID','Firmware Version','User Capacity','Sector Size','Rotation Rate','ATA Version','SATA Version','SMART Support']
    def return_stat_keys(self):
        return ['Health Status','Spin-Up Time','Start/Stop Count','Reallocated Sector Count','Power-On Hours','Power Cycle Count','Host Writes (32MiB)','Work ID - Media Wear Indicator','Work ID - Host Reads Percentage','Workload Minutes','Available Reserved Space','Media Wearout Indicator','End-to-end Error']

class Storage_info_old():
    def __init__(self):
        data = []
        with open("/proc/scsi/sg/device_strs") as file:
            for x in file:
                if not "no active device" in x:
                    data.append(x.split("\t"))
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


