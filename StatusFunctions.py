import json
import psutil as ps


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def hddInfo():
    hdd = {}
    diskUsage = ps.disk_usage(".")
    diskTotal = diskUsage.total
    diskUsed = diskUsage.used
    freeSpace = diskUsage.free
    diskPercent = diskUsage.percent

    # Depolama Alani Bilgileri
    hdd["DepolamaAlani"] = diskTotal
    hdd["Kullanilmayan"] = freeSpace
    hdd["Kullanilan"] = diskUsed
    hdd["Doluluk%"] = diskPercent

    return hdd

def cpuInfo():
    cpu = {}
    # per Cpu Times
    cpuStats = ps.cpu_percent(interval=1, percpu=False)
    cpuNumber = ps.cpu_count()

    # Cpu Bilgileri
    cpu["CPUKullanimYuzdesi"] = cpuStats
    cpu["CPUsayisi"] = cpuNumber

    return cpu

def memInfo():
    ram ={}
    # Memory Information
    memGeneralInfos = ps.virtual_memory()
    memTotal = memGeneralInfos.total
    memUsed = memGeneralInfos.used
    memFree = memGeneralInfos.free

    # Ram Bilgileri
    ram["ToplamHafiza"] = memTotal
    ram["BosHafiza"] = memFree
    ram["Kullanilan"] = memUsed

    return ram

def StatusFunc():

    general = {}
    general["HardDisk"] = hddInfo()
    general["cpu"] = cpuInfo()
    general["Ram"] = memInfo()

    return json.dumps(general)

def humanReadable():
    huread={}
    huread["bosAlan"]=sizeof_fmt(hddInfo()['Kullanilmayan'])
    return huread