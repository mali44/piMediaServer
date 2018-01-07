import json, psutil


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def StatusFunc():
    hdd = {}
    ram = {}
    cpu = {}
    general = {}

    diskUsage = psutil.disk_usage(".")
    diskTotal = sizeof_fmt(diskUsage.total)
    diskUsed = sizeof_fmt(diskUsage.used)
    freeSpace = sizeof_fmt(diskUsage.free)
    diskPercent = diskUsage.percent

    # per Cpu Times
    cpuStats = psutil.cpu_percent(interval=1, percpu=False)
    cpuNumber = psutil.cpu_count()

    # Memory Information
    memGeneralInfos = psutil.virtual_memory()
    memTotal = sizeof_fmt(memGeneralInfos.total)
    memUsed = sizeof_fmt(memGeneralInfos.used)
    memFree = sizeof_fmt(memGeneralInfos.free)

    # Depolama Alani Bilgileri
    hdd["DepolamaAlani"] = diskTotal
    hdd["Kullanilmayan"] = freeSpace
    hdd["Kullanilan"] = diskUsed
    hdd["Doluluk%"] = diskPercent

    # Ram Bilgileri
    ram["ToplamHafiza"] = memTotal
    ram["BosHafiza"] = memFree
    ram["Kullanilan"] = memUsed

    # Cpu Bilgileri
    cpu["CPUKullanimYuzdesi"] = cpuStats
    cpu["CPUsayisi"] = cpuNumber

    general["HardDisk"] = hdd
    general["cpu"] = cpu
    general["Ram"] = ram

    return json.dumps(general)
