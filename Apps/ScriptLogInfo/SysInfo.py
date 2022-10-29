import psutil
import platform
from datetime import datetime
from sty import fg, rs

class ANSI():
  def background(code):
    return "\33[{code}m".format(code=code)

  def style_text(code):
    return "\33[{code}m".format(code=code)

  def color_text(code):
    return "\33[{code}m".format(code=code)

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
        print(
           fg(250, 200, 0) + "T" +
           fg(250, 190, 0) + "o" +
           fg(250, 180, 0) + "t" +
           fg(250, 170, 0) + "a" +
           fg(250, 160, 0) + "l" +
           fg(250, 150, 0) + ": " +
           fg(250, 105, 60) + f"{adjust_size(virtual_mem.total)}"  + fg.rs)
        print(
           fg(250, 200, 0) + "A" +
           fg(250, 190, 0) + "v" +
           fg(250, 180, 0) + "a" +
           fg(250, 170, 0) + "i" +
           fg(250, 160, 0) + "l" +
           fg(250, 150, 0) + "a" +
           fg(250, 140, 0) + "b" +
           fg(250, 130, 0) + "l" +
           fg(250, 120, 0) + "e" +
           fg(250, 110, 0) + ": " +
           fg(250, 105, 60) + f"{adjust_size(virtual_mem.available)}"  + fg.rs)
        print(
            fg(250, 200, 0) + "U" +
            fg(250, 190, 0) + "s" +
            fg(250, 180, 0) + "e" +
            fg(250, 170, 0) + "d" +
            fg(250, 160, 0) + ": "  +
            fg(250, 105, 60) + f"{adjust_size(virtual_mem.used)}"  + fg.rs)
        print(
            fg(250, 200, 0) + "P" +
            fg(250, 190, 0) + "e" +
            fg(250, 180, 0) + "r" +
            fg(250, 170, 0) + "c" +
            fg(250, 160, 0) + "e" +
            fg(250, 150, 0) + "n" +
            fg(250, 140, 0) + "t" +
            fg(250, 130, 0) + "a" +
            fg(250, 120, 0) + "g" +
            fg(250, 110, 0) + "e" +
            fg(250, 100, 0) + ": " +
            fg(250, 105, 60) + f"{virtual_mem.percent}%" + fg.rs + "\n")

    def Sysinfo_SWAP(self):
        print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "SWAP", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
        swap = psutil.swap_memory()
        print(
            fg(250, 200, 0) + "T" +
            fg(250, 190, 0) + "o" +
            fg(250, 180, 0) + "t" +
            fg(250, 170, 0) + "a" +
            fg(250, 160, 0) + "l" +
            fg(250, 150, 0) + ": " +
            fg(250, 105, 60) + f"{adjust_size(swap.total)}" + fg.rs)
        print(
            fg(250, 200, 0) + "F" +
            fg(250, 190, 0) + "r" +
            fg(250, 180, 0) + "e" +
            fg(250, 170, 0) + "e" +
            fg(250, 160, 0) + ": " +
            fg(250, 105, 60) + f"{adjust_size(swap.free)}" + fg.rs)
        print(
            fg(250, 200, 0) + "U" +
            fg(250, 190, 0) + "s" +
            fg(250, 180, 0) + "e" +
            fg(250, 170, 0) + "d" +
            fg(250, 160, 0) + ": " +
            fg(250, 105, 60) + f"{adjust_size(swap.used)}" + fg.rs)
        print(
            fg(250, 200, 0) + "P" +
            fg(250, 190, 0) + "e" +
            fg(250, 180, 0) + "r" +
            fg(250, 170, 0) + "c" +
            fg(250, 160, 0) + "e" +
            fg(250, 150, 0) + "n" +
            fg(250, 140, 0) + "t" +
            fg(250, 130, 0) + "a" +
            fg(250, 120, 0) + "g" +
            fg(250, 110, 0) + "e" +
            fg(250, 100, 0) + ": " +
            fg(250, 105, 60) + f"{swap.percent}%" + fg.rs + "\n")

    def Sysinfo_HDD(self):
        print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "Disk Information", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
        partitions = psutil.disk_partitions()
        for p in partitions:
            print(
                fg(250, 200, 0) + "D" +
                fg(250, 190, 0) + "e" +
                fg(250, 180, 0) + "v" +
                fg(250, 170, 0) + "i" +
                fg(250, 160, 0) + "c" +
                fg(250, 150, 0) + "e" +
                fg(250, 140, 0) + ": " +
                fg(250, 105, 60) + f"{p.device}")
            print(
                fg(250, 200, 0) + "M" +
                fg(250, 190, 0) + "o" +
                fg(250, 180, 0) + "u" +
                fg(250, 170, 0) + "n" +
                fg(250, 160, 0) + "t" +
                fg(250, 150, 0) + "p" +
                fg(250, 140, 0) + "o" +
                fg(250, 130, 0) + "i" +
                fg(250, 120, 0) + "n" +
                fg(250, 110, 0) + "t" +
                fg(250, 90, 0) + ": " +
                fg(250, 105, 60) + f"{p.mountpoint}")
            print(
                fg(250, 200, 0) + "F" +
                fg(250, 190, 0) + "i" +
                fg(250, 180, 0) + "l" +
                fg(250, 170, 0) + "e " +
                fg(250, 160, 0) + "s" +
                fg(250, 150, 0) + "y" +
                fg(250, 140, 0) + "s" +
                fg(250, 130, 0) + "t" +
                fg(250, 120, 0) + "e" +
                fg(250, 110, 0) + "m " +
                fg(250, 100, 0) + "t" +
                fg(250, 90, 0) + "y" +
                fg(250, 80, 0) + "p" +
                fg(250, 70, 0) + "e" +
                fg(250, 60, 0) + ": " +
                fg(250, 105, 60) + f"{p.fstype}" + "\n")

            try:
                partition_usage = psutil.disk_usage(p.mountpoint)
            except PermissionError:
                continue

            print(
                fg(250, 200, 0) + "  T" +
                fg(230, 200, 0) + "o" +
                fg(210, 200, 0) + "t" +
                fg(190, 200, 0) + "a" +
                fg(170, 200, 0) + "l " +
                fg(150, 200, 0) + "S" +
                fg(130, 200, 0) + "i" +
                fg(110, 200, 0) + "z" +
                fg(90, 200, 0) + "e" +
                fg(70, 200, 0) + ": " +
                fg(250, 105, 60) + f"{adjust_size(partition_usage.total)}")
            print(
                fg(250, 200, 0) + "  U" +
                fg(230, 200, 0) + "s" +
                fg(210, 200, 0) + "e" +
                fg(190, 200, 0) + "d" +
                fg(170, 200, 0) + ": " +
                fg(250, 105, 60) + f"{adjust_size(partition_usage.used)}")
            print(
                fg(250, 200, 0) + "  F" +
                fg(230, 200, 0) + "r" +
                fg(210, 200, 0) + "e" +
                fg(190, 200, 0) + "e" +
                fg(170, 200, 0) + ": " +
                fg(250, 105, 60) + f"{adjust_size(partition_usage.free)}")
            print(
                fg(250, 200, 0) + "  P" +
                fg(230, 200, 0) + "e" +
                fg(210, 200, 0) + "r" +
                fg(190, 200, 0) + "c" +
                fg(170, 200, 0) + "e" +
                fg(150, 200, 0) + "n" +
                fg(130, 200, 0) + "t" +
                fg(110, 200, 0) + "a" +
                fg(90, 200, 0) + "g" +
                fg(70, 200, 0) + "e" +
                fg(50, 200, 0) + ": " +
                fg(250, 105, 60) + f"{partition_usage.percent}%" + "\n")

        disk_io = psutil.disk_io_counters()
        print(
            fg(250, 200, 160) + "R" +
            fg(250, 190, 150) + "e" +
            fg(250, 180, 140) + "a" +
            fg(250, 170, 130) + "d " +
            fg(250, 160, 120) + "s" +
            fg(250, 150, 110) + "i" +
            fg(250, 140, 100) + "n" +
            fg(250, 130, 90) + "c" +
            fg(250, 120, 80) + "e " +
            fg(250, 110, 70) + "b" +
            fg(250, 100, 60) + "o" +
            fg(250, 90, 50) + "o" +
            fg(250, 80, 40) + "t" +
            fg(250, 70, 30) + ": "  +
            fg(250, 105, 60) + f"{adjust_size(disk_io.read_bytes)}")
        print(
            fg(250, 200, 160) + "W" +
            fg(250, 190, 150) + "r" +
            fg(250, 180, 140) + "i" +
            fg(250, 170, 130) + "t" +
            fg(250, 160, 120) + "t" +
            fg(250, 150, 110) + "e" +
            fg(250, 140, 100) + "n " +
            fg(250, 130, 90) + "s" +
            fg(250, 120, 80) + "i" +
            fg(250, 110, 70) + "n" +
            fg(250, 100, 60) + "c" +
            fg(250, 90, 50) + "e " +
            fg(250, 80, 40) + "b" +
            fg(250, 70, 30) + "o" +
            fg(250, 60, 20) + "o" +
            fg(250, 50, 10) + "t" +
            fg(250, 40, 0) + ": "  +
            fg(250, 105, 60) + f"{adjust_size(disk_io.write_bytes)}")


    def Sysinfo_GPU(self):
        print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "GPU Details", fg(250, 195, 60), "-" * 40, fg.rs + "\n")
        import GPUtil
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            print(
                fg(200, 255, 0) + "I" +
                fg(190, 255, 0) + "D" +
                fg(180, 255, 0) + ": " +
                fg(250, 105, 60) + f"{gpu.id}",
                fg(200, 255, 0) + "N" +
                fg(190, 255, 0) + "a" +
                fg(180, 255, 0) + "m" +
                fg(170, 255, 0) + "e" +
                fg(160, 255, 0) + ": " +
                fg(250, 105, 60) + f"{gpu.name}")
            print(
                fg(200, 200, 0) + "\tL" +
                fg(190, 200, 0) + "o" +
                fg(180, 200, 0) + "a" +
                fg(170, 200, 0) + "d" +
                fg(160, 200, 0) + ": " +
                fg(189, 252, 201) + f"{gpu.load*100}" + fg(250, 105, 60) + " %")
            print(
                fg(200, 200, 0) + "\tF" +
                fg(190, 200, 0) + "r" +
                fg(180, 200, 0) + "e" +
                fg(170, 200, 0) + "e " +
                fg(160, 200, 0) + "M" +
                fg(150, 200, 0) + "e" +
                fg(140, 200, 0) + "m" +
                fg(130, 200, 0) + ": " +
                fg(189, 252, 201) + f"{gpu.memoryFree}" + fg(250, 105, 60) + " MB")
            print(
                fg(200, 200, 0) + "\tU" +
                fg(190, 200, 0) + "s" +
                fg(180, 200, 0) + "e" +
                fg(170, 200, 0) + "d " +
                fg(160, 200, 0) + "M" +
                fg(150, 200, 0) + "e" +
                fg(140, 200, 0) + "m" +
                fg(130, 200, 0) + ": " +
                fg(189, 252, 201) + f"{gpu.memoryUsed}" + fg(250, 105, 60) + " MB")
            print(
                fg(200, 200, 0) + "\tT" +
                fg(190, 200, 0) + "o" +
                fg(180, 200, 0) + "t" +
                fg(170, 200, 0) + "a" +
                fg(160, 200, 0) + "l " +
                fg(150, 200, 0) + "M" +
                fg(140, 200, 0) + "e" +
                fg(130, 200, 0) + "m" +
                fg(120, 200, 0) + ": " +
                fg(189, 252, 201) + f"{gpu.memoryTotal}" + fg(250, 105, 60) + " MB")
            print(
                fg(200, 200, 0) + "\tT" +
                fg(190, 200, 0) + "e" +
                fg(180, 200, 0) + "m" +
                fg(170, 200, 0) + "p" +
                fg(160, 200, 0) + "e" +
                fg(150, 200, 0) + "r" +
                fg(140, 200, 0) + "a" +
                fg(130, 200, 0) + "t" +
                fg(120, 200, 0) + "u" +
                fg(110, 200, 0) + "r" +
                fg(100, 200, 0) + "e" +
                fg(90, 200, 0) + ": " +
                fg(189, 252, 201) + f"{gpu.temperature}" + fg(250, 105, 60) + "°C" + fg.rs + "\n")



    def Sysinfo_Network(self):
        print(fg(250, 195, 60), "-" * 40, fg(250, 105, 60), "Network Information", fg(250, 195, 60), "-" * 40, fg.rs + "\n" + fg.rs)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(
                    fg(250, 200, 0) + "I" +
                    fg(250, 190, 0) + "n" +
                    fg(250, 180, 0) + "t" +
                    fg(250, 170, 0) + "e" +
                    fg(250, 160, 0) + "r" +
                    fg(250, 150, 0) + "f" +
                    fg(250, 140, 0) + "a" +
                    fg(250, 130, 0) + "c" +
                    fg(250, 120, 0) + "e" +
                    fg(250, 110, 0) + ": " +
                    fg(250, 105, 60) + f"{interface_name}" + fg.rs)

                if str(address.family) == 'AddressFamily.AF_INET':

                    print(
                        fg(250, 200, 0) + "  I" +
                        fg(250, 190, 0) + "P " +
                        fg(250, 180, 0) + "A" +
                        fg(250, 170, 0) + "d" +
                        fg(250, 160, 0) + "d" +
                        fg(250, 150, 0) + "r" +
                        fg(250, 140, 0) + "e" +
                        fg(250, 130, 0) + "s" +
                        fg(250, 120, 0) + "s" +
                        fg(250, 110, 0) + ": " +
                        fg(0, 255, 154) + f"{address.address}" + fg.rs)
                    print(
                        fg(250, 200, 0) + "  N" +
                        fg(250, 190, 0) + "e" +
                        fg(250, 180, 0) + "t" +
                        fg(250, 170, 0) + "m" +
                        fg(250, 160, 0) + "a" +
                        fg(250, 150, 0) + "s" +
                        fg(250, 140, 0) + "k" +
                        fg(250, 130, 0) + ": " +
                        fg(0, 255, 154) + f"{address.netmask}" + fg.rs)
                    print(
                        fg(250, 200, 0) + "  B" +
                        fg(250, 190, 0) + "r" +
                        fg(250, 180, 0) + "o" +
                        fg(250, 170, 0) + "a" +
                        fg(250, 160, 0) + "d" +
                        fg(250, 150, 0) + "c" +
                        fg(250, 140, 0) + "a" +
                        fg(250, 130, 0) + "s" +
                        fg(250, 120, 0) + "t " +
                        fg(250, 110, 0) + "I" +
                        fg(250, 100, 0) + "P" +
                        fg(250, 90, 0) + ": " +
                        fg(0, 255, 154) + f"{address.broadcast}" + fg.rs)

                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(
                        fg(250, 200, 0) + "  M" +
                        fg(250, 190, 0) + "A" +
                        fg(250, 180, 0) + "C " +
                        fg(250, 170, 0) + "A" +
                        fg(250, 160, 0) + "d" +
                        fg(250, 150, 0) + "d" +
                        fg(250, 140, 0) + "r" +
                        fg(250, 130, 0) + "e" +
                        fg(250, 120, 0) + "s" +
                        fg(250, 110, 0) + "s" +
                        fg(250, 100, 0) + ": " +
                        fg(0, 255, 154) + f"{address.address}" + fg.rs)
                    print(
                        fg(250, 200, 0) + "  N" +
                        fg(250, 190, 0) + "e" +
                        fg(250, 180, 0) + "t" +
                        fg(250, 170, 0) + "m" +
                        fg(250, 160, 0) + "a" +
                        fg(250, 150, 0) + "s" +
                        fg(250, 170, 0) + "k" +
                        fg(250, 160, 0) + ": " +
                        fg(0, 255, 154) + f"{address.netmask}" + fg.rs)
                    print(
                        fg(250, 200, 0) + "  B" +
                        fg(250, 190, 0) + "r" +
                        fg(250, 180, 0) + "o" +
                        fg(250, 170, 0) + "a" +
                        fg(250, 160, 0) + "d" +
                        fg(250, 150, 0) + "c" +
                        fg(250, 140, 0) + "a" +
                        fg(250, 130, 0) + "s" +
                        fg(250, 120, 0) + "t " +
                        fg(250, 110, 0) + "M" +
                        fg(250, 100, 0) + "A" +
                        fg(250, 90, 0) + "C" +
                        fg(250, 80, 0) + ": " +
                        fg(0, 255, 154) + f"{address.broadcast}" + fg.rs)
        print(fg.rs + "\n")
        net_io = psutil.net_io_counters()

        print(
            fg(0, 255, 255) + "T" +
            fg(0, 245, 245) + "o" +
            fg(0, 235, 235) + "t" +
            fg(0, 225, 225) + "a" +
            fg(0, 215, 215) + "l " +
            fg(0, 205, 205) + "B" +
            fg(0, 195, 195) + "y" +
            fg(0, 185, 185) + "t" +
            fg(0, 175, 175) + "e" +
            fg(0, 165, 165) + "s " +
            fg(0, 155, 155) + "S" +
            fg(0, 145, 145) + "e" +
            fg(0, 135, 135) + "n" +
            fg(0, 125, 125) + "t" +
            fg(0, 115, 115) + ": " +
            fg(0, 255, 154) + f"{adjust_size(net_io.bytes_sent)}" + fg.rs)
        print(
            fg(0, 255, 255) + "T" +
            fg(0, 245, 245) + "o" +
            fg(0, 235, 235) + "t" +
            fg(0, 225, 225) + "a" +
            fg(0, 215, 215) + "l " +
            fg(0, 205, 205) + "B" +
            fg(0, 195, 195) + "y" +
            fg(0, 185, 185) + "t" +
            fg(0, 175, 175) + "e" +
            fg(0, 165, 165) + "s " +
            fg(0, 155, 155) + "R" +
            fg(0, 145, 145) + "e" +
            fg(0, 135, 135) + "c" +
            fg(0, 125, 125) + "e" +
            fg(0, 115, 115) + "i" +
            fg(0, 105, 105) + "v" +
            fg(0, 95, 95) + "e" +
            fg(0, 85, 85) + "d" +
            fg(0, 75, 75) + ": " +
            fg(0, 255, 154) + f"{adjust_size(net_io.bytes_recv)}" + fg.rs)

        example_ansi = ANSI.background(2) + ANSI.color_text(49) + ANSI.style_text(39) + ""
        print(example_ansi)
