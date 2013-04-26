#!/usr/bin/env python
# encoding: utf-8
import general

"""                 eInfo
==============================================
Contains General System Information functions.

  Maintainer:    Anthony "AntCer" Cervantes
"""

def os_release(entry):
    with open("/etc/lsb-release") as file:
        osrel = file.readlines()
    osrel = osrel[3].split("=")[1].replace('"', '')
    entry.entry_set(osrel)

def e_ver(entry):
    entry.entry_set("v0.17.1")

def os_type(entry):
    with open("/proc/sys/kernel/ostype") as file:
        ostype = file.readline()
    entry.entry_set(ostype)

def kernel_info(entry):
    with open("/proc/sys/kernel/osrelease") as file:
        osr = file.readline()
    with open("/proc/sys/kernel/version") as file:
        kernv = file.readline()
    entry.entry_set('%s (%s)' %(osr, kernv))

def kernel_arch(entry):
    general.run("arch", entry)

def boot_cmd(win):
    from elementary import Popup, Entry, Button, Icon

    en = Entry(win)
    en.file_set("/proc/cmdline", 0)

    bt = Button(win)
    bt.text = "Close"
    bt.callback_clicked_add(lambda o: popup.delete())

    ic = Icon(win)
    ic.standard_set("system")

    popup = Popup(win)
    popup.size_hint_weight = (1.0, 1.0)
    popup.part_content_set("title,icon", ic)
    popup.part_text_set("title,text", "Boot Command")
    popup.part_content_set("default", en)
    popup.part_content_set("button1", bt)
    popup.show()

def display_man(entry):
    with open("/etc/X11/default-display-manager") as file:
        dm = file.readline()
    entry.entry_set(dm)

def installed_pkgs(entry):
    general.run("dpkg --get-selections | wc -l", entry)

def gcc_info(entry):
    general.run("gcc -dumpmachine", entry, True)
    general.run("gcc -dumpversion", entry)

def xorg_info(entry):
    with open("/var/log/Xorg.0.log") as file:
        for i, x in enumerate(file):
            if i is 1:
                x = x.split() ; x = x[3]
                entry.entry_set(x)
                break

def hostname(entry):
    with open("/proc/sys/kernel/hostname") as file:
        hn = file.readline()
    entry.entry_set(hn)

def domainname(entry):
    with open("/proc/sys/kernel/domainname") as file:
        dn = file.readline()
    entry.entry_set(dn)

def uptime(entry):
    with open("/proc/uptime") as file:
        up = file.readline()
    up = up.split()
    upt = up[0]
    upt = float(upt)

    days = int(round(float(upt/86400)))
    upt = float(upt-(86400*days))
    if days == 1:
        days = "1 Day"
    else:
        days = "%s Days" %days

    hrs = int(round(float(upt/3600)))
    upt = float(upt-(3600*hrs))
    if hrs == 1:
        hrs = "1 Hr"
    else:
        hrs = "%s Hrs" %hrs

    mns = int(float(upt/60))
    upt = float(upt-(60*mns))
    if mns == 1:
        mns = "1 Min"
    else:
        mns = "%s Mins" %mns

    #~ secs = int(round(float(upt)))
    #~ if secs == 1:
        #~ secs = "1 Sec"
    #~ else:
        #~ secs = "%s Secs" %secs

    entry.entry_set("%s %s %s" %(days, hrs, mns))

def timezone(entry):
    with open("/etc/timezone") as file:
        tz = file.readline()
    entry.entry_set(tz)

def language(entry):
    with open("/etc/default/locale") as file:
        locale = file.readline()
    locale = locale.split("=")[1].replace('"', '')
    entry.entry_set(locale)
