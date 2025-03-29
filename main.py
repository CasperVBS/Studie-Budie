from app import Window
from colorama import Fore
import psutil, os

p = psutil.Process(os.getpid())
p.nice(psutil.HIGH_PRIORITY_CLASS)  # Geeft Python meer CPU-kracht

print(Fore.GREEN)
window = Window()







