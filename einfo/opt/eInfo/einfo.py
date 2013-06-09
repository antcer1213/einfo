#!/usr/bin/env python
# encoding: utf-8
import os
import elementary as elm
import evas

"""eInfo

Simple Elm program to give detailed system information.
By: AntCer (bodhidocs@gmail.com)

Started: March 29, 2013
"""



class eInfo(object):
    def __init__(self):
        self.hs = False

        def vipbox():
            n.delete()

            def system(tb, tbi):
                self.system()
            def cpu(tb, tbi):
                self.cpu()
            def memory(tb, tbi):
                self.memory()
            def storage(tb, tbi):
                self.storage()
            def hardware(tb, tbi):
                self.hardware()

            vbox = elm.Box(self.win)
            vbox.size_hint_weight_set(1.0, 1.0)
            vbox.show()

            self.win.resize_object_add(vbox)

            tbox = elm.Box(self.win)
            tbox.size_hint_weight_set(1.0, 0.0)
            tbox.horizontal_set(True)
            vbox.pack_end(tbox)
            tbox.show()

            tb = elm.Toolbar(self.win)
            tb.item_append("", "OS", system)
            tb.item_append("", "CPU", cpu)
            tb.item_append("", "Memory", memory)
            tb.item_append("", "Storage", storage)
            tb.item_append("", "Hardware", hardware)
            tb.homogeneous_set(True)
            tb.select_mode_set(3)
            tbox.pack_end(tb)
            tb.show()

            tbr = elm.Toolbar(self.win)
            opts = tbr.item_append("", "Options")
            opts.menu_set(True)
            tb.menu_parent_set(self.win)
            menu = opts.menu_get()
            menu.item_add(label="Export as Plain Text", callback=lambda a,b: exporting())
            tbr.homogeneous_set(True)
            tbox.pack_end(tbr)
            tbr.show()

            self.separator(vbox)

            self.informationbox(vbox)

            tb.first_item_get().selected_set(True)

        def timer_func():
            from ecore import Timer
            Timer(0.6, vipbox)

        def exporting():
            import general
            lb = elm.Label(self.win)
            lb.text = "<b>...exported : %s/system.info</b>"%os.getenv("HOME")
            general.export_as("plain", "%s/system.info"%os.getenv("HOME"))
            n = elm.Notify(self.win)
            n.orient = 2
            n.content = lb
            n.timeout_set(3.0)
            n.show()

        win = self.win = elm.StandardWindow("einfo", "eInfo")
        win.callback_delete_request_add(lambda o: elm.exit())
        win.resize(400, 295)
        win.show()

        n = elm.Notify(self.win)
        lb = elm.Label(self.win)
        lb.text = "<b>Loading System Information...</b>"
        n.orient = 1
        n.allow_events_set(False)
        n.content = lb
        n.show()

        timer_func()


#---------GENERAL SYSTEM
    def system(self):
        import generalsys

        infobox = self.infobox
        infobox.clear()

        hor = self.box(infobox, [1.0, 0.0])

        inhor = self.box(hor, [1.0, 1.0], True)

        innerhor = self.box(inhor)
        self.label(innerhor, "Release:")
        info = self.info(innerhor, [False, True, False])
        generalsys.os_release(info)

        innerhor = self.box(inhor)
        self.label(innerhor, "Enlightenment:")
        info = self.info(innerhor, [False, True, False])
        generalsys.e_ver(info)

        innerhor = self.box(inhor)
        self.label(innerhor, "OS Type:")
        info = self.info(innerhor, [False, True, False])
        generalsys.os_type(info)

        self.icon(hor, "bodhi.png", [0.3, 0.0])

        self.separator(infobox)

        hor = self.box(infobox)
        self.label(hor, "Kernel Info:")
        info = self.info(hor, [False, True, False])
        generalsys.kernel_info(info)

        hor = self.box(infobox)

        inhor = self.box(hor)
        self.label(inhor, "Kernel Arch:")
        info = self.info(inhor, [False, True, False])
        generalsys.kernel_arch(info)

        inhor = self.box(hor, [0.0, 0.0])
        bt = elm.Button(self.win)
        bt.text = "Boot Command"
        self.size_hints(bt, [0.3, 0.0])
        bt.callback_clicked_add(lambda o: generalsys.boot_cmd(self.win))
        inhor.pack_end(bt)
        bt.show()

        self.separator(infobox)

        hor = self.box(infobox)
        hor.homogeneous_set(True)

        inhor = self.box(hor)
        self.label(inhor, "Display Manager:")
        info = self.info(inhor, [False, True, False])
        generalsys.display_man(info)

        inhor = self.box(hor)
        self.label(inhor, "Installed Packages:")
        info = self.info(inhor, [False, True, False])
        generalsys.installed_pkgs(info)

        hor = self.box(infobox)
        hor.homogeneous_set(True)

        inhor = self.box(hor)
        self.label(inhor, "GCC Version:")
        info = self.info(inhor, [False, True, False])
        generalsys.gcc_info(info)

        inhor = self.box(hor)
        self.label(inhor, "X.Org Version:")
        info = self.info(inhor, [False, True, False])
        generalsys.xorg_info(info)

        self.separator(infobox)

        hor = self.box(infobox)
        hor.homogeneous_set(True)

        inhor = self.box(hor)
        self.label(inhor, "Host Name:")
        info = self.info(inhor, [False, True, False])
        generalsys.hostname(info)

        inhor = self.box(hor)
        self.label(inhor, "Domain Name:")
        info = self.info(inhor, [False, True, False])
        generalsys.domainname(info)

        self.separator(infobox)

        hor = self.box(infobox)

        self.label(hor, "Uptime:")
        uptimeinfo = self.info(hor, [False, True, False])
        generalsys.uptime(uptimeinfo)

        bt = elm.Button(self.win)
        self.icon(None, "refresh", False, False, bt)
        self.size_hints(bt, [0.3, 0.0])
        bt.callback_clicked_add(lambda x: generalsys.uptime(uptimeinfo))
        hor.pack_end(bt)
        bt.show()

        hor = self.box(infobox)
        hor.homogeneous_set(True)

        inhor = self.box(hor)
        self.label(inhor, "Time Zone:")
        info = self.info(inhor, [False, True, False])
        generalsys.timezone(info)

        inhor = self.box(hor)
        self.label(inhor, "Language:")
        info = self.info(inhor, [False, True, False])
        generalsys.language(info)

        fill = elm.Box(self.win)
        self.size_hints(fill)
        infobox.pack_end(fill)
        fill.show()


#---------CPU
    def cpu(self, data=False, hstext=False):
        def gencpuinfo():
            gencpu = generalcpu.CPU_info()
            i = self.i

            ic.standard_set(gencpu.icon(i))
            gencpu.vendor_id(info0, i)
            #~ gencpu.number(info1)
            gencpu.cpu_arch(info2, i)
            gencpu.cpu_hvm(info3, i)
            gencpu.model_name(info4, i)
            gencpu.cpu_freq(info5, i)
            gencpu.cache_size(info6, i)
            gencpu.addr_sizes(info7, i)
            gencpu.bogomips(info8, i)
            gencpu.numbering(info9, i)
            gencpu.flags(info10, i)

        def ch(hs, z):
            for i, x in enumerate(ALPHA):
                if ALPHA[i] == z:
                    hs.text_set(CPU[i])
                    self.i = i
                    gencpuinfo()
                    break

        import generalcpu
        infobox = self.infobox

        CPU = ["cpu0", "cpu1", "cpu2", "cpu3"]
        ALPHA = ["a", "b", "c", "d"]
        self.i = 0

        infobox.clear()

        hor = self.box(infobox)

        hs = elm.Hoversel(self.win)
        hs.hover_parent_set(self.win)
        hs.text_set("cpu0")
        for i in range(generalcpu.number_of_cpus()):
            ALPHA[i] = hs.item_add(CPU[i])
        hs.callback_selected_add(ch)
        self.size_hints(hs, [1.0, 0.0])
        hor.pack_end(hs)
        hs.show()

        bt = elm.Button(self.win)
        self.icon(None, "refresh", False, False, bt)
        self.size_hints(bt, [0.05, 0.0])
        bt.callback_clicked_add(lambda o : gencpuinfo())
        hor.pack_end(bt)
        bt.show()

        cpubox = elm.Box(self.win)
        self.size_hints(cpubox)
        infobox.pack_end(cpubox)
        cpubox.show()

        hor = self.box(cpubox)

        left = elm.Box(self.win)
        self.size_hints(left)
        hor.pack_end(left)
        left.show()

        top = self.box(left)
        self.label(top, "Vendor:")
        info0 = self.info(top, [False, True, False])

        bot = self.box(left)
        #~ self.label(bot, "CPUs:")
        #~ info1 = self.info(bot, [False, True, False])

        self.label(bot, "CPU Arch:")
        info2 = self.info(bot, [False, True, False])

        self.label(bot, "HVM Support:")
        info3 = self.info(bot, [False, True, False])

        right = elm.Box(self.win)
        self.size_hints(right)
        hor.pack_end(right)
        right.show()

        ic = self.icon(right, None, [1.0, 1.0])

        self.separator(cpubox)

        hor = self.box(cpubox)

        self.label(hor, "Model Name:")
        info4 = self.info(hor, [False, True, False])

        hor = self.box(cpubox)
        hor.homogeneous_set(True)

        inhor = self.box(hor)
        self.label(inhor, "Frequency:")
        info5 = self.info(inhor, [False, True, False])

        inhor = self.box(hor)
        self.label(inhor, "L2 Cache:")
        info6 = self.info(inhor, [False, True, False])

        self.separator(cpubox)

        hor = self.box(cpubox)

        inhor = self.box(hor)
        self.label(inhor, "Address Sizes:")
        info7 = self.info(inhor, [False, True, False])

        inhor = self.box(hor)
        self.label(inhor, "Bogomips:")
        info8 = self.info(inhor, [False, True, False])

        hor = self.box(cpubox)

        self.label(hor, "Signature:")
        info9 = self.info(hor, [False, True, False])

        self.separator(cpubox)

        hor = self.box(cpubox)
        hor.size_hint_weight_set(1.0, 1.0)
        self.label(hor, "Flags:")
        info10 = self.info(hor, [False, False, True])

        gencpuinfo()


#---------MEMORY
    def memory(self):
        def genmeminfo(bt):
            from generalmem import Memory_Info

            genmem = Memory_Info(self.scale)
            genmem.memtotal(info0)
            genmem.buffers(info3)
            genmem.active(info4)
            genmem.swaptotal(info5)
            genmem.swapfree(info6)
            genmem.swapused(info7)
            genmem.cached(info8)
            genmem.inactive(info9)

            if self.pure:
                pb0.value_set(genmem.mem(True))
                pb1.value_set(genmem.swap())
                pb0.value_get()
                genmem.memfree(info1, True)
                genmem.memused(info2, True)
            else:
                pb0.value_set(genmem.mem(False))
                pb1.value_set(genmem.swap())
                genmem.memfree(info1)
                genmem.memused(info2)

            return True

        def change_scale(bt):
            if "KB" in bt.text:
                bt.text = "View Mode: MB"
                self.scale = "MB"
                genmeminfo(None)
            elif "MB" in bt.text:
                bt.text = "View Mode: GB"
                self.scale = "GB"
                genmeminfo(None)
            else:
                bt.text = "View Mode: KB"
                self.scale = "KB"
                genmeminfo(None)

        def mem_auto_refresh(chk):
            from ecore import Timer

            if chk.state_get():
                self.auto_refresh = Timer(0.7, genmeminfo, None)
            else:
                self.auto_refresh.delete()

        def mem_pure(chk):
            if chk.state_get():
                self.pure = True
            else:
                self.pure = False

            genmeminfo(None)

        self.scale = False
        self.pure  = False

        infobox = self.infobox
        infobox.clear()

        hor = self.box(infobox)

        bt = elm.Button(self.win)
        bt.text = "View Mode: KB"
        bt.callback_clicked_add(change_scale)
        self.size_hints(bt, [1.0, 0.0])
        hor.pack_end(bt)
        bt.show()

        bt = elm.Button(self.win)
        self.icon(None, "refresh", False, False, bt)
        self.size_hints(bt, [0.058, 0.0])
        bt.callback_clicked_add(genmeminfo)
        hor.pack_end(bt)
        bt.show()

        chkbox = self.box(infobox)

        chk = elm.Check(self.win)
        chk.text = "Ignore Buffers/Cached  "
        chk.size_hint_weight_set(0.0, 0.0)
        chk.size_hint_align_set(-1.0, -1.0)
        chkbox.pack_end(chk)
        chk.callback_changed_add(mem_pure)
        chk.show()

        chk = elm.Check(self.win)
        chk.text = "Automatically Refresh"
        chk.size_hint_weight_set(0.0, 0.0)
        chk.size_hint_align_set(1.0, 1.0)
        chkbox.pack_end(chk)
        chk.callback_changed_add(mem_auto_refresh)
        chk.show()

        self.separator(infobox)

        meminfo = elm.Box(self.win)
        self.size_hints(meminfo, [1.0, 0.0])
        infobox.pack_end(meminfo)
        meminfo.show()

        lab = elm.Label(self.win)
        lab.text = "<b>Memory</b>"
        lab.size_hint_weight_set(1.0, 0.0)
        lab.size_hint_align_set(0.5, -1.0)
        meminfo.pack_end(lab)
        lab.show()

        pb0 = elm.Progressbar(self.win)
        self.size_hints(pb0, [1.0, 0.0])
        meminfo.pack_end(pb0)
        pb0.show()

        hor = elm.Box(self.win)
        self.size_hints(hor)
        hor.homogeneous_set(True)
        hor.horizontal_set(True)
        meminfo.pack_end(hor)
        hor.show()

        inhor = self.box(hor, [1.0, 1.0])
        self.label(inhor, "Total:", [0.0, 1.0])
        info0 = self.info(inhor, [False, True, False])

        inhor = self.box(hor, [1.0, 1.0])
        self.label(inhor, "Free:", [0.0, 1.0])
        info1 = self.info(inhor, [False, True, False])

        inhor = self.box(hor, [1.0, 1.0])
        self.label(inhor, "Used:", [0.0, 1.0])
        info2 = self.info(inhor, [False, True, False])

        self.separator(meminfo)

        lab = elm.Label(self.win)
        lab.text = "<b>Swap</b>"
        lab.size_hint_weight_set(1.0, 0.0)
        lab.size_hint_align_set(0.5, -1.0)
        meminfo.pack_end(lab)
        lab.show()

        pb1 = elm.Progressbar(self.win)
        self.size_hints(pb1, [1.0, 0.0])
        meminfo.pack_end(pb1)
        pb1.show()

        hor = elm.Box(self.win)
        self.size_hints(hor)
        hor.homogeneous_set(True)
        hor.horizontal_set(True)
        meminfo.pack_end(hor)
        hor.show()

        inhor = self.box(hor, [1.0, 1.0])
        self.label(inhor, "Total:", [0.0, 1.0])
        info5 = self.info(inhor, [False, True, False])

        inhor = self.box(hor, [1.0, 1.0])
        self.label(inhor, "Free:", [0.0, 1.0])
        info6 = self.info(inhor, [False, True, False])

        inhor = self.box(hor, [1.0, 1.0])
        self.label(inhor, "Used:", [0.0, 1.0])
        info7 = self.info(inhor, [False, True, False])

        self.separator(meminfo)

        lab = elm.Label(self.win)
        lab.text = "<b>Extra</b>"
        lab.size_hint_weight_set(1.0, 0.0)
        lab.size_hint_align_set(0.5, -1.0)
        meminfo.pack_end(lab)
        lab.show()

        hor = elm.Box(self.win)
        self.size_hints(hor)
        hor.homogeneous_set(True)
        hor.horizontal_set(True)
        meminfo.pack_end(hor)
        hor.show()

        inhor = self.box(hor)
        inhor.size_hint_align_set(0.5, -1.0)
        self.label(inhor, "Active:", [0.0, 1.0])
        info4 = self.info(inhor, [False, True, False])

        inhor = self.box(hor, [1.0, 1.0])
        inhor.size_hint_align_set(0.5, -1.0)
        self.label(inhor, "Inactive:", [0.0, 1.0])
        info9 = self.info(inhor, [False, True, False])

        hor = elm.Box(self.win)
        self.size_hints(hor)
        hor.homogeneous_set(True)
        hor.horizontal_set(True)
        meminfo.pack_end(hor)
        hor.show()

        inhor = self.box(hor, [1.0, 1.0])
        inhor.size_hint_align_set(0.5, -1.0)
        self.label(inhor, "Buffers:", [0.0, 1.0])
        info3 = self.info(inhor, [False, True, False])

        inhor = self.box(hor, [1.0, 1.0])
        inhor.size_hint_align_set(0.5, -1.0)
        self.label(inhor, "Cached:", [0.0, 1.0])
        info8 = self.info(inhor, [False, True, False])

        fill = elm.Box(self.win)
        self.size_hints(fill)
        infobox.pack_end(fill)
        fill.show()

        genmeminfo(None)


#---------STORAGE
    def storage(self):
        def change_scale(bt):
            if "MB" in bt.text:
                bt.text = "View Mode: GB"
                genpart.create_table("GB", self.win, table=table)
                self.scale = "GB"
            else:
                bt.text = "View Mode: MB"
                genpart.create_table("MB", self.win, table=table)
                self.scale = "MB"

        def refresh(bt):
            genpart = Partition_info()
            genpart.create_table(self.scale, self.win, table=table)


        from generalstor import Partition_info
        genpart = Partition_info()

        self.scale = "MB"

        infobox = self.infobox
        infobox.clear()

        hor = self.box(infobox, [1.0, 0.0])

        bt = elm.Button(self.win)
        bt.text = "View Mode: MB"
        bt.callback_clicked_add(change_scale)
        self.size_hints(bt, [1.0, 0.0])
        hor.pack_end(bt)
        bt.show()

        bt = elm.Button(self.win)
        self.icon(None, "refresh", False, False, bt)
        self.size_hints(bt, [0.058, 0.0])
        bt.callback_clicked_add(refresh)
        hor.pack_end(bt)
        bt.show()

        table = genpart.partition_table_comb(self.win, infobox)

        self.separator(infobox)

        self.storage_devices(infobox)

    def storage_devices(self, infobox):
        def genstorinfo(i):
            genstor.vendor(info0, i)
            genstor.model(info1, i)
            genstor.revision(info2, i)

        def ch(hs, z):
            for i, x in enumerate(ALPHA):
                if ALPHA[i] == z:
                    hs.text_set(STOR[i])
                    genstorinfo(i)
                    break

        from generalstor import Storage_info
        genstor = Storage_info()

        STOR = ["scsi0", "scsi1", "scsi2", "scsi3", "scsi4", "scsi5", "scsi6", "scsi7"]
        ALPHA = ["a", "b", "c", "d", "e", "f", "g", "h"]
        NUM = genstor.number()

        hs = elm.Hoversel(self.win)
        hs.hover_parent_set(self.win)
        hs.text_set("scsi0")
        for i in range(NUM):
            ALPHA[i] = hs.item_add(STOR[i])
        hs.callback_selected_add(ch)
        self.size_hints(hs, [1.0, 0.0])
        infobox.pack_end(hs)
        hs.show()

        storinfo = elm.Box(self.win)
        self.size_hints(storinfo, [1.0, 0.0])
        infobox.pack_end(storinfo)
        storinfo.show()

        hor = self.box(storinfo)

        inhor = self.box(hor)
        self.label(inhor, "Vendor:")
        info0 = self.info(inhor, [False, True, False])

        inhor = self.box(hor)
        self.label(inhor, "Model:")
        info1 = self.info(inhor, [False, True, False])

        inhor = self.box(hor)
        self.label(inhor, "Rev:")
        info2 = self.info(inhor, [False, True, False])

        self.separator(storinfo)

        genstorinfo(0)


#---------HARDWARE
    def hardware(self):
        infobox = self.infobox
        infobox.clear()

        from generalhw import Hardware_Info
        hwinfo = Hardware_Info()

        ALPHA = ["a", "b", "c", "d", "e", "f", "g", "h"]

        conbox = self.box(infobox, [1.0, 1.0])
        conbox.horizontal_set(False)



        def sys():
            def ch(hs, z):
                for i, x in enumerate(ALPHA):
                    if ALPHA[i] == z:
                        hs.text_set(moboname[i])
                        lstbox.clear()
                        self.lst(lstbox, moboinfo[i]())
                        break

            conbox.clear()

            hs = elm.Hoversel(self.win)
            hs.hover_parent_set(self.win)
            hs.text_set("Motherboard Information")
            hs.callback_selected_add(ch)
            self.size_hints(hs, [1.0, 0.0])
            conbox.pack_end(hs)
            hs.show()

            lstbox = self.box(conbox, [1.0, 1.0])

            self.lst(lstbox, hwinfo.mobo_info())

            moboname = ["Motherboard Information", "BIOS Information", "System Unit Information", "Memory Information", "PCI Device Information", "USB Device Information", "Battery Information"]
            moboinfo = [hwinfo.mobo_info, hwinfo.bios_info, hwinfo.sys_info, hwinfo.mem_info, hwinfo.pci_info, hwinfo.usb_info, hwinfo.bat_info]

            for i in range(6):
                ALPHA[i] = hs.item_add(moboname[i])

        def vid():
            def ch(hs, z):
                for i, x in enumerate(ALPHA):
                    if ALPHA[i] == z:
                        hs.text_set(moboname[i])
                        lstbox.clear()
                        self.lst(lstbox, moboinfo[i]())
                        break

            conbox.clear()

            hs = elm.Hoversel(self.win)
            hs.hover_parent_set(self.win)
            hs.text_set("Video Port Information")
            hs.callback_selected_add(ch)
            self.size_hints(hs, [1.0, 0.0])
            conbox.pack_end(hs)
            hs.show()

            lstbox = self.box(conbox, [1.0, 1.0])

            self.lst(lstbox, hwinfo.vid_info())

            moboname = ["Video Port Information", "Video Device Information"]
            moboinfo = [hwinfo.vid_info, hwinfo.vid_dev_info]

            for i in range(2):
                ALPHA[i] = hs.item_add(moboname[i])

        def aud():
            def ch(hs, z):
                for i, x in enumerate(ALPHA):
                    if ALPHA[i] == z:
                        hs.text_set(moboname[i])
                        lstbox.clear()
                        self.lst(lstbox, moboinfo[i]())
                        break

            conbox.clear()

            hs = elm.Hoversel(self.win)
            hs.hover_parent_set(self.win)
            hs.text_set("Audio Port Information")
            hs.callback_selected_add(ch)
            self.size_hints(hs, [1.0, 0.0])
            conbox.pack_end(hs)
            hs.show()

            lstbox = self.box(conbox, [1.0, 1.0])

            self.lst(lstbox, hwinfo.aud_info())

            moboname = ["Audio Port Information", "Audio Device Information"]
            moboinfo = [hwinfo.aud_info, hwinfo.aud_dev_info]

            for i in range(2):
                ALPHA[i] = hs.item_add(moboname[i])

        def net():
            def ch(hs, z):
                for i, x in enumerate(ALPHA):
                    if ALPHA[i] == z:
                        hs.text_set(moboname[i])
                        lstbox.clear()
                        self.lst(lstbox, moboinfo[i]())
                        break

            conbox.clear()

            hs = elm.Hoversel(self.win)
            hs.hover_parent_set(self.win)
            hs.text_set("Network Port Information")
            hs.callback_selected_add(ch)
            self.size_hints(hs, [1.0, 0.0])
            conbox.pack_end(hs)
            hs.show()

            lstbox = self.box(conbox, [1.0, 1.0])

            self.lst(lstbox, hwinfo.net_info())

            moboname = ["Network Port Information", "Network Device Information", "Local Network Information", "Remote Network Information"]
            moboinfo = [hwinfo.net_info, hwinfo.net_dev_info, hwinfo.net_int_loc_info, hwinfo.net_int_rem_info]

            for i in range(4):
                ALPHA[i] = hs.item_add(moboname[i])




        tb = elm.Toolbar(self.win)
        tb.item_append("", "System",   lambda x,y: sys())
        tb.item_append("", "Video",    lambda x,y: vid())
        tb.item_append("", "Audio",    lambda x,y: aud())
        tb.item_append("", "Network",  lambda x,y: net())
        #~ tb.item_append("", "USB/Input")
        tb.homogeneous_set(True)
        tb.select_mode_set(3)
        infobox.pack_end(tb)
        tb.show()

        tb.first_item_get().selected_set(True)



#----------------------CREATORS
    def informationbox(self, vbox):
        infobox = self.infobox = elm.Box(self.win)
        infobox.size_hint_weight_set(1.0, 1.0)
        infobox.size_hint_align_set(-1.0, -1.0)
        infobox.padding_set(5, 4)
        vbox.pack_end(infobox)
        infobox.show()
        return infobox

    def separator(self, vbox=None):
        sep = elm.Separator(self.win)
        sep.horizontal_set(True)
        if vbox:
            vbox.pack_end(sep)
            sep.show()
        else:
            return sep

    def box(self, infobox, dim=False, vert=False):
        hor = elm.Box(self.win)
        if dim:
            hor.size_hint_weight_set(dim[0], dim[1])
        else:
            hor.size_hint_weight_set(1.0, 0.0)
        if vert:
            pass
        else:
            hor.horizontal_set(True)
        hor.size_hint_align_set(-1.0, -1.0)
        infobox.pack_end(hor)
        hor.show()
        return hor

    def label(self, hor, text, weight=False, align=False):
        lab = elm.Label(self.win)
        lab.text = "<b>%s</b>" %text
        if weight or align:
            self.size_hints(lab, weight, align)
        hor.pack_end(lab)
        lab.show()

    def info(self, hor, options, weight=False, align=False):
        info = elm.Entry(self.win)
        self.size_hints(info, weight, align)
        info.editable_set(options[0])
        info.single_line_set(options[1])
        info.scrollable_set(options[2])
        hor.pack_end(info)
        info.show()

        return info

    def icon(self, box, image, weight=False, align=False, addto=False):
        ic = elm.Icon(self.win)
        if not ic.standard_set(image):
            ic.standard_set("none")
        if addto:
            addto.content_set(ic)
        else:
            self.size_hints(ic, weight, align)
            box.pack_end(ic)
            ic.show()
        return ic

    def lst(self, box, data, weight=False, align=False):
        lst = elm.List(self.win)
        for i in range(len(data)):
            self.lst_add(lst, data[i])
        self.size_hints(lst, weight, align)
        lst.select_mode_set(2)
        lst.mode_set(0)
        box.pack_end(lst)
        lst.show()

    def lst_add(self, lst, label, child=False):
        if type(label) is list:
            for x in label:
                lst.item_append("            %s" %x)
        elif "<SEP>" in label or label == " ":
            sep = lst.item_append(" ")
            sep.separator_set(True)
        elif child:
            lst.item_append(" -" + label)
        else:
            lst.item_append(label)

    def size_hints(self, item, weight=False, align=False):
        if weight:
            item.size_hint_weight_set(weight[0], weight[1])
        else:
            item.size_hint_weight_set(1.0, 1.0)
        if align:
            item.size_hint_align_set(align[0], align[1])
        else:
            item.size_hint_align_set(-1.0, -1.0)


#---Start

if __name__ == "__main__":
    elm.init()

    eInfo()

    elm.run()
    elm.shutdown()
