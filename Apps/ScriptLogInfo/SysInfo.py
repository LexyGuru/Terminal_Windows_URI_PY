import psutil
import platform
from datetime import datetime
from sty import fg,rs

def Sysinfomenu():
    uname = platform.uname()
    print(
        fg(130, 255, 0) + "S" +
        fg(150, 245, 10) + "y" +
        fg(170, 235, 20) + "s" +
        fg(190, 225, 30) + "t" +
        fg(210, 215, 40) + "e" +
        fg(230, 205, 50) + "m" +
        fg(250, 195, 60) + ": " + fg.rs +

        fg(250, 195, 255) + f"{uname.system} {uname.version}" + fg.rs)


def adjust_size(size):
    factor = 1024
    for i in ["B", "KiB", "MiB", "GiB", "TiB"]:
        if size > factor:
            size = size / factor
        else:
            return f"{size:.3f}{i}"

class Sysinfo_all:
    def Sysinfo_win(self):
        print(fg(250, 195, 60), "-"*40, fg(250, 105, 60), "Sys Info", fg(250, 195, 60), "-"*40, fg.rs + "\n")
        uname = platform.uname()
        print(
            fg(250, 200, 0) + "S" +
            fg(250, 190, 0) + "y" +
            fg(250, 180, 0) + "s" +
            fg(250, 170, 0) + "t" +
            fg(250, 160, 0) + "e" +
            fg(250, 150, 0) + "m" +
            fg(250, 140, 0) + ": " +
            fg(250, 105, 60) + f"{uname.system}" + fg.rs)
        print(
            fg(250, 200, 0) + "N" +
            fg(250, 190, 0) + "o" +
            fg(250, 180, 0) + "d" +
            fg(250, 170, 0) + "e " +
            fg(250, 160, 0) + "N" +
            fg(250, 150, 0) + "a" +
            fg(250, 140, 0) + "m" +
            fg(250, 130, 0) + "e" +
            fg(250, 120, 0) + ": " +
            fg(250, 105, 60) + f"{uname.node}" + fg.rs)
        print(
            fg(250, 200, 0) + "R" +
            fg(250, 190, 0) + "e" +
            fg(250, 180, 0) + "l" +
            fg(250, 170, 0) + "e" +
            fg(250, 160, 0) + "a" +
            fg(250, 150, 0) + "s" +
            fg(250, 140, 0) + "e" +
            fg(250, 130, 0) + ": " +
            fg(250, 105, 60) + f"{uname.release}" + fg.rs)
        print(
            fg(250, 200, 0) + "V" +
            fg(250, 190, 0) + "e" +
            fg(250, 180, 0) + "r" +
            fg(250, 170, 0) + "s" +
            fg(250, 160, 0) + "i" +
            fg(250, 150, 0) + "o" +
            fg(250, 140, 0) + "n" +
            fg(250, 130, 0) + ": " +
            fg(250, 105, 60) + f"{uname.version}" + fg.rs)
        print(
            fg(250, 200, 0) + "M" +
            fg(250, 190, 0) + "a" +
            fg(250, 180, 0) + "c" +
            fg(250, 170, 0) + "h" +
            fg(250, 160, 0) + "i" +
            fg(250, 150, 0) + "n" +
            fg(250, 140, 0) + "e" +
            fg(250, 130, 0) + ": " +
            fg(250, 105, 60) + f"{uname.machine}" + fg.rs)
        print(
            fg(250, 200, 0) + "P" +
            fg(250, 190, 0) + "r" +
            fg(250, 180, 0) + "o" +
            fg(250, 170, 0) + "c" +
            fg(250, 160, 0) + "e" +
            fg(250, 150, 0) + "s" +
            fg(250, 140, 0) + "s" +
            fg(250, 130, 0) + "o" +
            fg(250, 120, 0) + "r" +
            fg(250, 110, 0) + ": " +
            fg(250, 105, 60) + f"{uname.processor}" + fg.rs + "\n")

    def Sysinfo_boot(self):
        print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "Boot Time", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(
            fg(250, 200, 0) + "B" +
            fg(250, 190, 0) + "o" +
            fg(250, 180, 0) + "o" +
            fg(250, 170, 0) + "t " +
            fg(250, 160, 0) + "T" +
            fg(250, 150, 0) + "i" +
            fg(250, 140, 0) + "m" +
            fg(250, 130, 0) + "e" +
            fg(250, 120, 0) + ": " +
            fg(250, 105, 60) + f"{bt.day}.{bt.month}.{bt.year} {bt.hour}:{bt.minute}:{bt.second}" + fg.rs + "\n")

    def Sysinfo_CPU(self):
        print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "CPU Info", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
        print(
            fg(250, 200, 0) + "A" +
            fg(250, 190, 0) + "c" +
            fg(250, 180, 0) + "t" +
            fg(250, 170, 0) + "u" +
            fg(250, 160, 0) + "a" +
            fg(250, 150, 0) + "l " +
            fg(250, 140, 0) + "C" +
            fg(250, 130, 0) + "o" +
            fg(250, 120, 0) + "r" +
            fg(250, 110, 0) + "e" +
            fg(250, 100, 0) + "s" +
            fg(250, 90, 0) + ":",
            fg(250, 105, 60) + str(psutil.cpu_count(logical=False)))
        print(
            fg(250, 200, 0) + "L" +
            fg(250, 190, 0) + "o" +
            fg(250, 180, 0) + "g" +
            fg(250, 170, 0) + "i" +
            fg(250, 160, 0) + "c" +
            fg(250, 150, 0) + "a" +
            fg(250, 140, 0) + "l " +
            fg(250, 130, 0) + "C" +
            fg(250, 120, 0) + "o" +
            fg(250, 110, 0) + "r" +
            fg(250, 100, 0) + "e" +
            fg(250, 90, 0) + "s" +
            fg(250, 80, 0) + ":",
            fg(250, 105, 60) + str(psutil.cpu_count(logical=True)))
        print(
            fg(250, 200, 0) + "M" +
            fg(250, 190, 0) + "a" +
            fg(250, 180, 0) + "x " +
            fg(250, 170, 0) + "F" +
            fg(250, 160, 0) + "r" +
            fg(250, 150, 0) + "e" +
            fg(250, 140, 0) + "q" +
            fg(250, 130, 0) + "u" +
            fg(250, 120, 0) + "e" +
            fg(250, 110, 0) + "n" +
            fg(250, 100, 0) + "c" +
            fg(250, 90, 0) + "y" +
            fg(250, 80, 0) + ": " +
            fg(250, 105, 60) + f"{psutil.cpu_freq().max:.1f}Mhz")
        print(
            fg(250, 200, 0) + "C" +
            fg(250, 190, 0) + "u" +
            fg(250, 180, 0) + "r" +
            fg(250, 170, 0) + "r" +
            fg(250, 160, 0) + "e" +
            fg(250, 150, 0) + "n" +
            fg(250, 140, 0) + "t " +
            fg(250, 130, 0) + "F" +
            fg(250, 120, 0) + "r" +
            fg(250, 110, 0) + "e" +
            fg(250, 100, 0) + "q" +
            fg(250, 90, 0) + "u" +
            fg(250, 80, 0) + "e" +
            fg(250, 70, 0) + "n" +
            fg(250, 60, 0) + "c" +
            fg(250, 50, 0) + "y" +
            fg(250, 40, 0) + ": " +
            fg(250, 105, 60) + f"{psutil.cpu_freq().current:.1f}Mhz")
        print(
            fg(250, 200, 0) + "C" +
            fg(250, 190, 0) + "P" +
            fg(250, 180, 0) + "U " +
            fg(250, 170, 0) + "U" +
            fg(250, 160, 0) + "s" +
            fg(250, 150, 0) + "a" +
            fg(250, 140, 0) + "g" +
            fg(250, 130, 0) + "e" +
            fg(250, 120, 0) + ": " +
            fg(250, 105, 60) + f"{psutil.cpu_percent()}%" + fg.rs + "\n")

        '''print("CPU Usage/Core:")
        for i, perc in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {perc}%")'''

    def Sysinfo_ram(self):
        print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "RAM Info", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
        virtual_mem = psutil.virtual_memory()
        print(f"Total: {adjust_size(virtual_mem.total)}")
        print(f"Available: {adjust_size(virtual_mem.available)}")
        print(f"Used: {adjust_size(virtual_mem.used)}")
        print(f"Percentage: {virtual_mem.percent}%")

    def Sysinfo_SWAP(self):
        print("-"*40, "SWAP", "-"*40)
        swap = psutil.swap_memory()
        print(f"Total: {adjust_size(swap.total)}")
        print(f"Free: {adjust_size(swap.free)}")
        print(f"Used: {adjust_size(swap.used)}")
        print(f"Percentage: {swap.percent}%")

    def Sysinfo_HDD(self):
        print("-"*40, "Disk Information", "-"*40)
        partitions = psutil.disk_partitions()
        for p in partitions:
            print(f"Device: {p.device}")
            print(f"\tMountpoint: {p.mountpoint}")
            print(f"\tFile system type: {p.fstype}")
            try:
                partition_usage = psutil.disk_usage(p.mountpoint)
            except PermissionError:
                continue
        print(f"  Total Size: {adjust_size(partition_usage.total)}")
        print(f"  Used: {adjust_size(partition_usage.used)}")
        print(f"  Free: {adjust_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
        disk_io = psutil.disk_io_counters()
        print(f"Read since boot: {adjust_size(disk_io.read_bytes)}")
        print(f"Written since boot: {adjust_size(disk_io.write_bytes)}")

    def Sysinfo_GPU(self):
        print("-"*40, "GPU Details", "-"*40)
        import GPUtil
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            print(f"ID: {gpu.id}, Name: {gpu.name}")
            print(f"\tLoad: {gpu.load*100}%")
            print(f"\tFree Mem: {gpu.memoryFree}MB")
            print(f"\tUsed Mem: {gpu.memoryUsed}MB")
            print(f"\tTotal Mem: {gpu.memoryTotal}MB")
            print(f"\tTemperature: {gpu.temperature} °C")

    def Sysinfo_Network(self):
        print("-"*40, "Network Information", "-"*40)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"Interface: {interface_name}")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {adjust_size(net_io.bytes_sent)}")
        print(f"Total Bytes Received: {adjust_size(net_io.bytes_recv)}")




'''
---------  KESSZ  --------
Sysinfo_all.Sysinfo_win('self')
Sysinfo_all.Sysinfo_boot('self')
Sysinfo_all.Sysinfo_CPU('self')
Sysinfo_all.Sysinfo_ram('self')
'''


'''
Sysinfo_all.Sysinfo_SWAP('self')
Sysinfo_all.Sysinfo_Network('self')
Sysinfo_all.Sysinfo_GPU('self')
Sysinfo_all.Sysinfo_HDD('self')
'''