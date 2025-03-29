from datetime import datetime
import settings
from pathlib import Path 

debug = settings.overschrijven_debug
logs = settings.overschrijven_logs
newfile = False

def set_word(word):
    word = word
    if debug:
        print(word)
def controleer(word,input):
    if logs:
        save(input)
    if debug == True:
        print(f"woord: {word} input {input}")
    if input == word:
        return True
    else:
        return False
    
def make_new_file():
    global date
    global newfile
    global file_path

    date = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
    
    script_dir = Path(__file__).parent
    log_dir = script_dir / "logs" / "overschrijven_log"
    file_path = log_dir / f"log_{date}.txt"


    date_days = datetime.now().strftime("%d/%m/%y")
    date_time = datetime.now().strftime("%H:%M:%S")
    file = open(file_path,"a")
    file.write(f"log van {date_days} om {date_time} \n \n")
    newfile = True
    if debug:
        print("newfile")

def save(word):
    if newfile:
        file = open(file_path,"a")
        file.write(word+"\n")
    else:
        make_new_file()


