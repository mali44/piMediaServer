import os
import psutil


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)



#Hard Drive Selection :
usbBellek='/Volumes/piStatus'
statvfs = os.statvfs(usbBellek)

#HDD Free Space Alignment
freeSpace = float(statvfs.f_frsize * statvfs.f_bfree)
freeSpace=sizeof_fmt(freeSpace)
diskUsage=psutil.disk_usage(usbBellek)
diskTotal=sizeof_fmt(diskUsage.total)
diskUsed=sizeof_fmt(diskUsage.used)
diskPercent=diskUsage.percent

#per Cpu Times
cpuStats=psutil.cpu_percent(interval=1,percpu=False)
cpuNumber=psutil.cpu_count()


#Memory Information
memGeneralInfos=psutil.virtual_memory()
memTotal=sizeof_fmt(memGeneralInfos.total)
memUsed=sizeof_fmt(memGeneralInfos.used)
memFree=sizeof_fmt(memGeneralInfos.free)

