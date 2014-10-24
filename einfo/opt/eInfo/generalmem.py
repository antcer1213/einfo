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

        try:
            return used/total
        except:
            return 0

    def memtotal(self, entry=False):
        scale = self.scale
        data = self.data

        total = int(data[0].split()[1])

        if scale == "GB":
            total = '{:,}'.format(Decimal(total)/1048576)
            if entry:
                entry.entry_set("%s GB" % total)
            else:
                return "%s GB" %total
        elif scale == "MB":
            total = '{:,}'.format(total/1024)
            if entry:
                entry.entry_set("%s MB" % total)
            else:
                return "%s MB" %total
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


class moduleArrayInfo():
    def __init__(self):
        self.module_information()

    def module_number(self):
        try:
            return self.num
        except:
            import dmidecode
            self.num = len(dmidecode.QueryTypeId(17))
            return self.num
    def array_number(self):
        try:
            return self.arraynum
        except:
            import dmidecode
            self.arraynum = len(dmidecode.QueryTypeId(16))
            return self.arraynum

    def modules_in_use(self):
        return self.in_use

    def modules_total(self, scale="MB"):
        if scale=="MB":
            return self.mods_total
        else:
            return Decimal(self.mods_total)/1024

    def module_information(self, quantity=False, array=False, sticks=False, i=False):
        import dmidecode
        self.in_use = 0
        self.mods_total = 0
        data = {}
        module_data = dmidecode.QueryTypeId(17)
        array_data = dmidecode.QueryTypeId(16)

        for h, v in enumerate(module_data.keys()):
            data['Memory Device %s'%(h+1)] = {}
            data['Memory Device %s'%(h+1)]['Size'] = module_data[v]['data']['Size']
            if module_data[v]['data']['Size'] != "":
                self.mods_total += int(module_data[v]['data']['Size'].split()[0])
                self.in_use += 1
            data['Memory Device %s'%(h+1)]['Form Factor'] = module_data[v]['data']['Form Factor']
            data['Memory Device %s'%(h+1)]['Type'] = module_data[v]['data']['Type']
            data['Memory Device %s'%(h+1)]['Speed'] = module_data[v]['data']['Speed']
            data['Memory Device %s'%(h+1)]['Manufacturer'] = module_data[v]['data']['Manufacturer']
            data['Memory Device %s'%(h+1)]['Locator'] = module_data[v]['data']['Locator']
            data['Memory Device %s'%(h+1)]['Bank Locator'] = module_data[v]['data']['Bank Locator']
            data['Memory Device %s'%(h+1)]['Data Width'] = module_data[v]['data']['Data Width']
            data['Memory Device %s'%(h+1)]['Total Width'] = module_data[v]['data']['Total Width']
            data['Memory Device %s'%(h+1)]['Serial Number'] = module_data[v]['data']['Serial Number']
            data['Memory Device %s'%(h+1)]['Part Number'] = module_data[v]['data']['Part Number']
            #~ mem.append("Configured Clock Speed: %s" %(v['data']['Configured Clock Speed']))
            #~ mem.append("Rank: %s" %(v['data']['Rank']))
            data['Memory Device %s'%(h+1)]['Type Detail'] = module_data[v]['data']['Type Detail']
        for h, v in enumerate(array_data.keys()):
            data['Memory Array %s'%(h+1)] = {}
            data['Memory Array %s'%(h+1)]['Location'] = array_data[v]['data']['Location']
            data['Memory Array %s'%(h+1)]['Use'] = array_data[v]['data']['Use']
            data['Memory Array %s'%(h+1)]['Error Correction Type'] = array_data[v]['data']['Error Correction Type']
            data['Memory Array %s'%(h+1)]['Maximum Capacity'] = array_data[v]['data']['Maximum Capacity']
            data['Memory Array %s'%(h+1)]['Number of Possible Devices'] = array_data[v]['data']['Number Of Devices']
            data['Memory Array %s'%(h+1)]['Number of Current Devices'] = self.modules_in_use()

        self.full_data = data

    def module_list(self, i=0):
        data = self.full_data
        list_items = []
        for key in data['Memory Device %s'%(i+1)].keys():
            if key == "Type Detail":
                list_items.append("Type Detail:")
                for it in data['Memory Device %s'%(i+1)][key]:
                    if it != None:
                        list_items.append("    %s"%it)
            else:
                if data['Memory Device %s'%(i+1)][key] != "":
                    list_items.append("%s : %s"%(key,data['Memory Device %s'%(i+1)][key]))

        return list_items

