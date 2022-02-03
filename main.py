from dhooks import Webhook, File
from datetime import datetime
from colorama import Fore
import platform
import colorama
import cpuinfo
import psutil
import socket
import uuid
import re
import os

os.system('cls')

class TheMachineScraper():
    """ ! This is a simple program built for gathering machine information ! """


    def Menu():
        """ Main Menu & Method Input """

        print(f"""\n\n                {Fore.RED}TheMachineScraper{Fore.RESET} - a simple tool for gathering machine data
                            {Fore.GREEN}github.com/codeuk/themachinescraper{Fore.RESET}\n\n""")
        print(f"                                   [{Fore.RED}1{Fore.RESET}] Save to File\n                                   [{Fore.RED}2{Fore.RESET}] Discord Webhook")
        method = str(input(f"\n [{Fore.GREEN}?{Fore.RESET}] What Method would you like to use? : "))

        if method == "2":
            webhook = input(f" [{Fore.GREEN}?{Fore.RESET}] Enter Webhook : ")
            return webhook
        else:return None


    def FormatBytes(bytes):
        """ Format Bytes """

        for amt in ["", "K", "M", "G", "T", "P"]:
            if bytes < 1024:return f"{bytes:.2f}{amt}B"
            bytes /= 1024
    

    def General():
        """ General System Information """

        print(f"\n [{Fore.RED}tms{Fore.RESET}] General  -> ", end="")
        f = open('C://ProgramData/TheMachineScraper.txt', 'a+', encoding="utf-8")

        f.write(""" ++++++  System Information  ++++++\n""")
        uname = platform.uname()
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        f.write(f"\nSystem: {uname.system}")
        f.write(f"\nNode Name: {uname.node}")
        f.write(f"\nRelease: {uname.release}")
        f.write(f"\nBoot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
        f.write(f"\nVersion: {uname.version}")
        f.write(f"\nMachine: {uname.machine}")
        f.write(f"\nProcessor: {uname.processor}")
        f.write(f"\nProcessor: {cpuinfo.get_cpu_info()['brand_raw']}")
        f.write(f"\nIp-Address: {socket.gethostbyname(socket.gethostname())}")
        f.write(f"\nMac-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")

        f.close()
        print(f" [{Fore.GREEN}DONE{Fore.RESET}]")  


    def HardWare():
        """ Hardware Information """

        print(f" [{Fore.RED}tms{Fore.RESET}] HardWare -> ", end="")
        f = open('C://ProgramData/TheMachineScraper.txt', 'a+', encoding="utf-8")

        f.write("\n\n ++++++  HardWare Information  ++++++")

        f.write("\n\n[ CPU Info ]")
        f.write(f"\n  >>Physical cores: {psutil.cpu_count(logical=False)}")
        f.write(f"\n  >>Total cores: {psutil.cpu_count(logical=True)}")
        f.write(f"\n  >>Max Frequency: {psutil.cpu_freq().max:.2f}Mhz")
        f.write(f"\n  >>Min Frequency: {psutil.cpu_freq().min:.2f}Mhz")
        f.write(f"\n  >>Current Frequency: {psutil.cpu_freq().current:.2f}Mhz")
        f.write("\n  >>CPU Usage Per Core:")
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):f.write(f"\n  >>Core {i}: {percentage}%")
        f.write(f"\n  >>Total CPU Usage: {psutil.cpu_percent()}%")

        f.write("\n\n[ Memory Information ]")
        f.write(f"\n  >>Total: {TheMachineScraper.FormatBytes(psutil.virtual_memory().total)}")
        f.write(f"\n  >>Available: {TheMachineScraper.FormatBytes(psutil.virtual_memory().available)}")
        f.write(f"\n  >>Used: {TheMachineScraper.FormatBytes(psutil.virtual_memory().used)}")
        f.write(f"\n  >>Percentage: {psutil.virtual_memory().percent}%")

        f.write("\n\n[ SWAP MEMORY ]")
        swap = psutil.swap_memory()
        f.write(f"\n  >>Total: {TheMachineScraper.FormatBytes(swap.total)}")
        f.write(f"\n  >>Free: {TheMachineScraper.FormatBytes(swap.free)}")
        f.write(f"\n  >>Used: {TheMachineScraper.FormatBytes(swap.used)}")
        f.write(f"\n  >>Percentage: {swap.percent}%")

        f.write("\n\n[ Disk Information ]")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            f.write(f"\n[ Device: {partition.device} ]")
            f.write(f"\n  >>Mountpoint: {partition.mountpoint}")
            f.write(f"\n  >>File system type: {partition.fstype}")
            try:partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:continue
            f.write(f"\n  >>Total Size: {TheMachineScraper.FormatBytes(partition_usage.total)}")
            f.write(f"\n  >>Used: {TheMachineScraper.FormatBytes(partition_usage.used)}")
            f.write(f"\n  >>Free: {TheMachineScraper.FormatBytes(partition_usage.free)}")
            f.write(f"\n  >>Percentage: {partition_usage.percent}%")
        disk_io = psutil.disk_io_counters()
        f.write(f"\n  >>Total read: {TheMachineScraper.FormatBytes(disk_io.read_bytes)}   ")
        f.write(f"\n  >>Total write: {TheMachineScraper.FormatBytes(disk_io.write_bytes)} ")

        f.close()
        print(f" [{Fore.GREEN}DONE{Fore.RESET}]")  


    def Network():
        """ Network & IP Information """

        print(f" [{Fore.RED}tms{Fore.RESET}] Network  -> ", end="")
        f = open('C://ProgramData/TheMachineScraper.txt', 'a+', encoding="utf-8")

        f.write("\n\n ++++++  Network Information  ++++++")
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                f.write(f"\n\n[ Interface: {interface_name} ]")
                if str(address.family) == 'AddressFamily.AF_INET':
                    f.write(f"\n  >>IP Address: {address.address}")
                    f.write(f"\n  >>Netmask: {address.netmask}")
                    f.write(f"\n  >>Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    f.write(f"\n  >>MAC Address: {address.address}")
                    f.write(f"\n  >>Netmask: {address.netmask}")
                    f.write(f"\n  >>Broadcast MAC: {address.broadcast}")

        net_io = psutil.net_io_counters()
        f.write(f"\n<<  Total Bytes Sent: {TheMachineScraper.FormatBytes(net_io.bytes_sent)}  >>")
        f.write(f"\n<<  Total Bytes Received: {TheMachineScraper.FormatBytes(net_io.bytes_recv)}  >>")

        f.close()
        print(f" [{Fore.GREEN}DONE{Fore.RESET}]")  
     
if __name__ == "__main__":
    webhook = TheMachineScraper.Menu()
    TheMachineScraper.General()
    TheMachineScraper.HardWare()
    TheMachineScraper.Network()

    if "discord" in webhook:
        print(f" [{Fore.RED}tms{Fore.RESET}] Sending  -> ", end="")
        output = File('C:\ProgramData\TheMachineScraper.txt', name='TheMachineScraper.txt')
        filehook = Webhook(webhook)
        filehook.send(file=output)
        print(f" [{Fore.GREEN}DONE{Fore.RESET}]")  
        os.remove('C:\ProgramData\TheMachineScraper.txt')
        print(f"\n [{Fore.RED}tms{Fore.RESET}] File Sent to Webhook\n\n")

    elif webhook == None:print(f"\n [{Fore.RED}tms{Fore.RESET}] File Saved to {Fore.RED}C:\ProgramData\TheMachineScraper.txt{Fore.RESET}\n\n")
