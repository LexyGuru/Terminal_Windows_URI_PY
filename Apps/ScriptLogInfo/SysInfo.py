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
        print("-"*40, "Sys Info", "-"*40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")

    def Sysinfo_boot(self):
        print("-"*40, "Boot Time", "-"*40)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.day}.{bt.month}.{bt.year} {bt.hour}:{bt.minute}:{bt.second}")

    def Sysinfo_CPU(self):
        print("-"*40, "CPU Info", "-"*40)
        print("Actual Cores:", psutil.cpu_count(logical=False))
        print("Logical Cores:", psutil.cpu_count(logical=True))
        print(f"Max Frequency: {psutil.cpu_freq().max:.1f}Mhz")
        print(f"Current Frequency: {psutil.cpu_freq().current:.1f}Mhz")
        print(f"CPU Usage: {psutil.cpu_percent()}%")
        print("CPU Usage/Core:")
        for i, perc in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {perc}%")

    def Sysinfo_ram(self):
        print("-"*40, "RAM Info", "-"*40)
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
Sysinfo_all.Sysinfo_win('self')
Sysinfo_all.Sysinfo_boot('self')
Sysinfo_all.Sysinfo_CPU('self')
Sysinfo_all.Sysinfo_ram('self')
Sysinfo_all.Sysinfo_SWAP('self')
Sysinfo_all.Sysinfo_Network('self')
Sysinfo_all.Sysinfo_GPU('self')
Sysinfo_all.Sysinfo_HDD('self')
'''