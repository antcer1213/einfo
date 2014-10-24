
def run(command, entry, append=False, endfx=False):
    from ecore import Exe

    def received_data(cmd, event, entry, append, *args, **kwargs):
        if append:
            output = event.data
            if type(entry) == str:
                entry += output
            else:
                output = output.replace("\n", "")
                entry.entry_append(" (%s)" %output)
        else:
            if type(entry) == str:
                entry = event.data
            else:
                entry.entry_set(event.data)

    def command_done(cmd, event, entry, command, *args, **kwargs):
        if event.exit_code is not 0:
            if type(entry) == str:
                entry = "N/A"
            else:
                entry.entry_set("N/A")
        else:
            if endfx:
                endfx[0](endfx[1], endfx[2], endfx[3])

    cmd = Exe(command, 1|4)
    cmd.on_data_event_add(received_data, entry, append)
    cmd.on_del_event_add(command_done, entry, endfx)

def splitter(lst, breaker, search=False):
    current = []
    it = iter(lst)
    first = next(it)
    #~ assert first==breaker
    for item in it:
        if search == True and breaker in item:
            yield current
            current = []
        elif item == breaker:
            yield current
            current = []
        current.append(item)
    yield current

def export_as(typ, loc):
    import generalsys, generalcpu, generalmem, generalstor, generalhw

    gencpu  = generalcpu.CPU_info()
    genmem  = generalmem.Memory_Info("MB")
    genstr1 = generalstor.Storage_info()
    genstr2 = generalstor.Partition_info()
    genhw   = generalhw.Hardware_Info()

    if typ == "html":
        pass
    else:
        plain = ["eInfo - Information Sheet (Plain Text)", "\n\n\nOS\n\n"]
        plain.append("Release: %s\n"%generalsys.os_release())
        plain.append("Enlightenment: %s\n"%generalsys.e_ver())
        plain.append("OS Type: %s\n"%generalsys.os_type())
        plain.append("Kernel Info: %s\n"%generalsys.kernel_info())
        plain.append("Kernel Arch: %s\n"%generalsys.kernel_arch())
        plain.append("Boot CMD: %s\n"%generalsys.boot_cmd())
        plain.append("Display Manager: %s\n"%generalsys.display_man())
        plain.append("Installed Packages: %s\n"%generalsys.installed_pkgs())
        plain.append("GCC Version: %s\n"%generalsys.gcc_info())
        plain.append("X.Org Version: %s\n"%generalsys.xorg_info())
        plain.append("Host name: %s\n"%generalsys.hostname())
        plain.append("Domain Name: %s\n"%generalsys.domainname())
        plain.append("Uptime: %s\n"%generalsys.uptime())
        plain.append("Time Zone: %s\n"%generalsys.timezone())
        plain.append("Language: %s\n"%generalsys.language())
        plain.append("\n\n\nCPU\n")
        for i in range(gencpu.number()):
            plain.append("\nProcessor %s\n"%i+1)
            plain.append("Vendor: %s\n"%gencpu.vendor_id(i=i))
            plain.append("Model Name: %s\n"%gencpu.model_name(i=i))
            plain.append("CPU Arch: %s\n"%gencpu.cpu_arch(i=i))
            plain.append("HVM Support: %s\n"%gencpu.cpu_hvm(i=i))
            plain.append("Current Frequency: %s\n"%gencpu.cpu_freq(i=i))
            plain.append("L2 Cache: %s\n"%gencpu.cache_size(i=i))
            plain.append("Address Sizes: %s\n"%gencpu.addr_sizes(i=i))
            plain.append("Bogomips: %s\n"%gencpu.bogomips(i=i))
            plain.append("Signature: %s\n"%gencpu.numbering(i=i))
            plain.append("Flags: %s\n"%gencpu.flags(i=i))
        plain.append("\n\n\nMemory\n\n")
        plain.append("Total Usable Memory: %s\n\n"%genmem.memtotal())
        for x in genhw.mem_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            else:
                plain.append("%s\n"%x)
        plain.append("\n\n\nStorage\n\n")
        for i in range(genstr1.number()):
            plain.append(genstr1.vendor(i=i))
            plain.append(genstr1.model(i=i))
            plain.append(genstr1.revision(i=i))
            plain.append("\n")
        plain.append("\n")
        for x in genstr2.partition_combined():
            plain.append("%s\n"%x)
        plain.append("\n\n\n\nHardware\n\n\n")
        plain.append("System Unit Information\n\n")
        for x in genhw.sys_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            else:
                plain.append("%s\n"%x)
        plain.append("\n\nMotherboard Information\n\n")
        for x in genhw.mobo_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            else:
                plain.append("%s\n"%x)
        plain.append("\n\nBIOS Information\n\n")
        for x in genhw.bios_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            else:
                plain.append("%s\n"%x)
        plain.append("\n\nPCI Device Information\n\n")
        for x in genhw.pci_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            else:
                plain.append("%s\n"%x)
        plain.append("\n\nUSB Device Information\n\n")
        for x in genhw.usb_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            else:
                plain.append("%s\n"%x)
        plain.append("\n\nBattery Information\n\n")
        for x in genhw.bat_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            else:
                plain.append("%s\n"%x)
        plain.append("\n\nVideo Port Information\n\n")
        for x in genhw.vid_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            else:
                plain.append("%s\n"%x)
        plain.append("\n\nAudio Port Information\n\n")
        for x in genhw.aud_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            else:
                plain.append("%s\n"%x)
        plain.append("\n\nNetwork Port Information\n\n")
        for x in genhw.net_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            else:
                plain.append("%s\n"%x)
        plain.append("\n\nLocal Network Information\n\n")
        for x in genhw.net_int_loc_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            elif "<SEP>" in x:
                plain.append("\n")
            else:
                plain.append("%s\n"%x)
        plain.append("\n\nRemote Network Information\n\n")
        for x in genhw.net_int_rem_info():
            if type(x) is list:
                for z in x:
                    plain.append("\t%s\n"%z)
            elif "<SEP>" in x:
                plain.append("\n")
            else:
                plain.append("%s\n"%x)

        #~ for x in plain:
            #~ if type(x) is not str:
                #~ print x

        with open(loc, "w") as file:
            file.writelines(plain)
            file.close()

