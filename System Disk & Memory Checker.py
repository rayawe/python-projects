import shutil
import psutil

def system_check():
    disk = shutil.disk_usage("C:\\")
    memory = psutil.virtual_memory()

    print("Disk Usage:")
    print(f"Total: {disk.total // (1024**3)} GB")
    print(f"Used: {disk.used // (1024**3)} GB")
    print(f"Free: {disk.free // (1024**3)} GB")

    print("\nMemory Usage:")
    print("Total:", memory.total // (1024**3), "GB")
    print("Used:", memory.used // (1024**3), "GB")
    print("Available:", memory.available // (1024**3), "GB")

system_check()
