#!/usr/bin/env python
# encoding: utf-8
from os import listdir, path

"""                 eInfo
==============================================
Contains General System Information functions.

  Maintainer:    Anthony "AntCer" Cervantes
"""

def os_release(entry=False):
    with open("/etc/lsb-release") as file:
        osrel = file.readlines()
    osrel = osrel[3].split("=")[1].replace('"', '')[:-1]

    if entry:
        entry.entry_set(osrel)
    else:
        return osrel

def e_ver(entry=False):
    try:
        with open("/usr/lib/pkgconfig/enlightenment.pc") as file:
            data = file.readlines()
        data.reverse()
        for line in data:
            if line.startswith("Version: "):
                ever = "v%s" %line.split()[1]
    except:
        ever = "Not installed"

    if entry:
        entry.entry_set(ever)
    else:
        return ever

def os_type(entry=False):
    with open("/proc/sys/kernel/ostype") as file:
        ostype = file.readline()
    if entry:
        entry.entry_set(ostype)
    else:
        return ostype

def kernel_info(entry=False, os=False, ver=False):
    with open("/proc/sys/kernel/osrelease") as file:
        osr = file.readline()[:-1]
    with open("/proc/sys/kernel/version") as file:
        kernv = file.readline()[:-1]

    if os:
        return osr
    elif ver:
        return kernv
    elif entry:
        entry.entry_set('%s (%s)' %(osr, kernv))
    else:
        return "%s (%s)" %(osr, kernv)

def kernel_arch(entry=False):
    arch = "N/A"
    for x in listdir("/boot"):
        if x == "config-%s"%kernel_info(os=True):
            with open("/boot/%s"%x) as file:
                for line in file:
                    if line.startswith("# Linux"):
                        if "x86_64" in line:
                            arch = "x86_64 (64bit)"
                        else:
                            arch = "ix86 (32bit)"
                        break

    if entry:
        entry.entry_set(arch)
    else:
        return arch


def boot_cmd(win=False):
    from elementary import Popup, Entry, Button, Icon

    if win:
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
    else:
        return open("/proc/cmdline").readline()[:-1]

def display_man(entry=False):
    with open("/etc/X11/default-display-manager") as file:
        dm = file.readline()[:-1]

    if entry:
        entry.entry_set(dm)
    else:
        return dm

def installed_pkgs(entry=False):
    num = 0
    with open("/var/lib/dpkg/status") as file:
        for x in file:
            if x.startswith("Package: "):
                num += 1

    if entry:
        entry.entry_set("%s"%num)
    else:
        return num

def gcc_info(entry=False):
    gcc = "/usr/lib/gcc"
    test = 0
    if "i" in kernel_arch():
        arch = "i"
    else:
        arch = "_64"

    if path.isdir(gcc):
        y = listdir(gcc)
        for x in y:
            if arch in x:
                gccm = x
                z = listdir(gcc + "/" + x)
                if len(z) == 1:
                    gccv = z[1]
                    break
                for w in z:
                    if w > test:
                        gccv = "%s"%w
                        test = w
    else:
        gcc_info = "Not installed"

    gcc_info = "%s (%s)" %(gccv, gccm)

    if entry:
        entry.entry_set(gcc_info)
    else:
        return gcc_info

def xorg_info(entry=False):
    try:
        with open("/var/log/Xorg.0.log") as file:
            for x in file:
                if x.startswith("X.Org"):
                    ver = x.split()[3]
                    break
    except:
        ver = "Not detected"

    if entry:
        entry.entry_set(ver)
    else:
        return ver

def hostname(entry=False):
    with open("/proc/sys/kernel/hostname") as file:
        hn = file.readline()[:-1]

    if entry:
        entry.entry_set(hn)
    else:
        return hn

def domainname(entry=False):
    with open("/proc/sys/kernel/domainname") as file:
        dn = file.readline()[:-1]

    if entry:
        entry.entry_set(dn)
    else:
        return dn

def uptime(entry=False):
    from decimal import Decimal, getcontext
    getcontext().prec = 6

    with open("/proc/uptime") as file:
        up = file.readline()[:-1]
    up = up.split()
    upt = up[0].split(".")[0]
    upt = Decimal(int(upt))

    if upt >= 86400:
        days = upt/86400
        print days.split(".")
        if int(str(days).split(".")[1]) >= 0:
            days = int(str(days).split(".")[0])
        upt = upt-(86400*days)
    else:
        days = 0
    if days == 1:
        days = "1 Day"
    else:
        days = "%s Days" %days

    if upt >= 3600:
        hrs = upt/3600
        if int(str(hrs).split(".")[1]) >= 0:
            hrs = int(str(hrs).split(".")[0])
        upt = upt-(3600*hrs)
    else:
        hrs = 0
    if hrs == 1:
        hrs = "1 Hr"
    else:
        hrs = "%s Hrs" %hrs

    if upt >= 60:
        mns = upt/60
        if int(str(mns).split(".")[1]) >= 0:
            mns = int(str(mns).split(".")[0])
        upt = upt-(60*mns)
    else:
        mns = 0
    if mns == 1:
        mns = "1 Min"
    else:
        mns = "%s Mins" %mns

    secs = upt
    if secs == 1:
        secs = "1 Sec"
    else:
        secs = "%s Secs" %secs

    uptime = "%s %s %s %s" %(days, hrs, mns, secs)

    if entry:
        entry.entry_set(uptime)
    else:
        return uptime

def timezone(entry=False):
    with open("/etc/timezone") as file:
        tz = file.readline()[:-1]

    if entry:
        entry.entry_set(tz)
    else:
        return tz

def language(entry=False):
    with open("/etc/default/locale") as file:
        locale = file.readline()[:-1]
    locale = locale.split("=")[1].replace('"', '')

    if entry:
        entry.entry_set(locale)
    else:
        return locale
