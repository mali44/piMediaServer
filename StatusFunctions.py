import HardDriveStatus
import json,psutil



def StatusFunc():
    hds = HardDriveStatus
    hdd = {}
    ram = {}
    cpu = {}
    general = {}

    # DepolamaAlani Bilgileri
    hdd["DepolamaAlani"] = hds.diskTotal
    hdd["Kullanilmayan"] = hds.freeSpace
    hdd["Kullanilan"] = hds.diskUsed
    hdd["Doluluk%"] = hds.diskPercent
    # Ram Bilgileri
    ram["ToplamHafiza"] = hds.memTotal
    ram["BosHafiza"] = hds.memFree
    ram["Kullanilan"] = hds.memUsed
    # Cpu Bilgileri
    cpu["CPUKullanimYuzdesi"] = hds.cpuStats
    cpu["CPUsayisi"] = hds.cpuNumber
    # self.wfile.write(json.dumps(hdd))

    # self.wfile.write(json.dumps(ram))
    general["HardDisk"] = hdd
    general["cpu"] = cpu
    general["Ram"] = ram


    a=json.dumps(general)

    return a
