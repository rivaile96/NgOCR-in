import os
import time
import cv2
import pytesseract
import pygame
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

ascii_art = f"""{CYAN}
 ███▄    █   ▄████  ▒█████   ▄████▄   ██▀███   ██▓ ███▄    █ 
 ██ ▀█   █  ██▒ ▀█▒▒██▒  ██▒▒██▀ ▀█  ▓██ ▒ ██▒▓██▒ ██ ▀█   █ 
▓██  ▀█ ██▒▒██░▄▄▄░▒██░  ██▒▒▓█    ▄ ▓██ ░▄█ ▒▒██▒▓██  ▀█ ██▒
▓██▒  ▐▌██▒░▓█  ██▓▒██   ██░▒▓▓▄ ▄██▒▒██▀▀█▄  ░██░▓██▒  ▐▌██▒
▒██░   ▓██░░▒▓███▀▒░ ████▓▒░▒ ▓███▀ ░░██▓ ▒██▒░██░▒██░   ▓██░
░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░▒░▒░ ░ ░▒ ▒  ░░ ▒▓ ░▒▓░░▓  ░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░  ░   ░   ░ ▒ ▒░   ░  ▒     ░▒ ░ ▒░ ▒ ░░ ░░   ░ ▒░
   ░   ░ ░ ░ ░   ░ ░ ░ ░ ▒  ░          ░░   ░  ▒ ░   ░   ░ ░ 
         ░       ░     ░ ░  ░ ░         ░      ░           ░ 
                            ░                                 
{YELLOW}                 Author: Rivaile{RESET}
"""

os.system("clear" if os.name == "posix" else "cls")  # Bersihkan layar terminal
print(ascii_art)

def pilih_bahasa():
    bahasa_dict = {
        1: "English", 2: "Indonesian", 3: "Simplified Chinese", 4: "Traditional Chinese",
        5: "Russian", 6: "Japanese", 7: "Japanese (Vertical)", 8: "Korean", 9: "Arabic"
    }
    ocr_code_dict = {"English": "eng", "Indonesian": "ind", "Simplified Chinese": "chi_sim", "Traditional Chinese": "chi_tra",
                      "Russian": "rus", "Japanese": "jpn", "Japanese (Vertical)": "jpn_vert", "Korean": "kor", "Arabic": "ara"}
    
    while True:
        print(f"{MAGENTA}🗣 Pilih bahasa OCR:{RESET}")
        for k, v in bahasa_dict.items():
            print(f"{GREEN}{k}. {v}{RESET}")
        print(f"{RED}0. Kembali\n99. Keluar{RESET}")
        
        try:
            pilihan = int(input(f"{CYAN}Masukkan nomor bahasa (default: English): {RESET}") or 1)
            if pilihan == 99:
                exit(f"{RED}❌ Program dihentikan.{RESET}")
            return ocr_code_dict.get(bahasa_dict.get(pilihan, "English"), "eng")
        except ValueError:
            print(f"{RED}❌ Masukkan angka yang valid!{RESET}")

def pilih_psm():
    while True:
        print(f"\n🔍 {YELLOW}Pilih Page Segmentation Mode (PSM):{RESET}")
        print(f"{GREEN}6.{RESET} Teks dalam blok (cocok untuk kalimat panjang)")
        print(f"{GREEN}11.{RESET} Teks dalam satu baris (cocok untuk kaligrafi atau teks pendek)")
        print(f"{RED}0. Kembali\n99. Keluar{RESET}")
        
        try:
            pilihan = int(input(f"{CYAN}Masukkan nomor PSM (default: 6): {RESET}") or 6)
            if pilihan == 99:
                exit(f"{RED}❌ Program dihentikan.{RESET}")
            return pilihan if pilihan in [6, 11] else 6
        except ValueError:
            print(f"{RED}❌ Masukkan angka yang valid!{RESET}")

def jalankan_ocr():
    lang = pilih_bahasa()
    psm = pilih_psm()
    print(f"\n🚀 {CYAN}OCR berjalan dengan bahasa: {lang}, PSM: {psm}{RESET}")
    
    while True:
        path_gambar = input(f"{CYAN}Masukkan path gambar: {RESET}")
        if not os.path.exists(path_gambar):
            print(f"{RED}❌ File tidak ditemukan! Coba lagi.{RESET}")
            continue
        
        try:
            img = cv2.imread(path_gambar)
            if img is None:
                print(f"{RED}❌ Gambar tidak valid!{RESET}")
                continue
            
            custom_config = f'--oem 3 --psm {psm}'
            hasil_ocr = pytesseract.image_to_string(img, lang=lang, config=custom_config)
            
            print(f"{GREEN}✔ Hasil OCR:{RESET}\n{WHITE}{hasil_ocr}{RESET}")
            break
        except Exception as e:
            print(f"{RED}⚠ Error selama OCR: {e}{RESET}")
            continue

def main():
    while True:
        print(f"\n🚀 {CYAN}Sistem OCR Otomatis Dimulai!{RESET}")
        print(f"{GREEN}1. Mulai OCR{RESET}")
        print(f"{RED}99. Keluar{RESET}")
        
        try:
            pilihan = int(input(f"{CYAN}Masukkan pilihan: {RESET}"))
            if pilihan == 1:
                jalankan_ocr()
            elif pilihan == 99:
                exit(f"{RED}❌ Program dihentikan.{RESET}")
            else:
                print(f"{RED}❌ Pilihan tidak tersedia!{RESET}")
        except ValueError:
            print(f"{RED}❌ Masukkan angka yang valid!{RESET}")

if __name__ == "__main__":
    main()
