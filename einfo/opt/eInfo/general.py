
def run(command, entry, append=False):
    from ecore import Exe

    def received_data(cmd, event, append, *args, **kwargs):
        if append:
            output = event.data
            output = output.replace("\n", "")
            entry.entry_append(" (%s)" %output)
        else:
            entry.entry_set(event.data)

    def command_done(cmd, event, *args, **kwargs):
        if event.exit_code is not 0:
            entry.entry_set("N/A")

    cmd = Exe(command, 1|4)
    cmd.on_data_event_add(received_data, append)
    cmd.on_del_event_add(command_done)

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
    import generalsys, generalcpu, generalmem, generalstor,generalhw

    gencpu  = generalcpu.CPU_info()
    genmem  = generalmem.Memory_Info("MB")
    genstr1 = generalstor.Storage_info()
    genstr2 = generalstor.Partition_info()
    genhw   = generalhw.Hardware_Info()

    if typ == "html":
        pass
    else:
        plain = ["eInfo - Information Sheet (Plain Text)", "\n\n", "OS\n"]
        plain.append(generalsys.os_release())
        plain.append(generalsys.e_ver())
        plain.append(generalsys.os_type())
        plain.append(generalsys.kernel_info())
        plain.append(generalsys.kernel_arch())
        plain.append(generalsys.boot_cmd())
        plain.append(generalsys.display_man())
        plain.append(generalsys.installed_pkgs())
        plain.append(generalsys.gcc_info())
        plain.append(generalsys.xorg_info())
        plain.append(generalsys.hostname())
        plain.append(generalsys.domainname())
        plain.append(generalsys.uptime())
        plain.append(generalsys.timezone())
        plain.append(generalsys.language())
        plain.append("\n\n")
        plain.append("CPU\n")
        for i in range(gencpu.number()):
            plain.append("cpu%s"%i)
            plain.append(gencpu.vendor_id(i=i))
            plain.append(gencpu.model_name(i=i))
            plain.append(gencpu.cpu_arch(i=i))
            plain.append(gencpu.cpu_hvm(i=i))
            plain.append(gencpu.cpu_freq(i=i))
            plain.append(gencpu.cache_size(i=i))
            plain.append(gencpu.addr_sizes(i=i))
            plain.append(gencpu.bogomips(i=i))
            plain.append(gencpu.numbering(i=i))
            plain.append(gencpu.flags(i=i))
        plain.append("\n\n")
        plain.append("Memory\n")
        plain.append(genmem.memtotal())
        for x in genhw.mem_info():
            plain.append(x)
        plain.append("\n\n")
        plain.append("Storage\n")
        for i in range(genstr1.number()):
            plain.append(genstr1.vendor(i=i))
            plain.append(genstr1.model(i=i))
            plain.append(genstr1.revision(i=i))
        plain.append("\n")
        for x in genstr2.partition_combined():
            plain.append(x)
        plain.append("\n\n")
        plain.append("Hardware\n")
        for x in genhw.sys_info():
            plain.append(x)
        for x in genhw.mobo_info():
            plain.append(x)
        for x in genhw.bios_info():
            plain.append(x)
        for x in genhw.pci_info():
            plain.append(x)
        for x in genhw.bat_info():
            plain.append(x)
        for x in genhw.vid_info():
            plain.append(x)
        for x in genhw.aud_info():
            plain.append(x)
        for x in genhw.net_info():
            plain.append(x)
        for x in genhw.net_int_loc_info():
            plain.append(x)
        for x in genhw.net_int_rem_info():
            plain.append(x)

        with open(loc, "w") as file:
            file.writelines(plain)
            file.close()

