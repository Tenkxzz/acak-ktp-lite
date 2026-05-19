#!/usr/bin/env python3

import os
import requests
import re
import time
import random

try:
    from colorama import Fore, init
    init(autoreset=True)
except ImportError:
    class Fore:
        RED = ''
        GREEN = ''
        RESET = ''
    print("[!] pip install colorama")

def banner():
    print(f"""{Fore.RED}
 ▗▄▖  ▗▄▄▖ ▗▄▖ ▗▖ ▗▖    ▗▖ ▗▖▗▄▄▄▖▗▄▄▖ 
▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌▗▞▘    ▐▌▗▞▘  █  ▐▌ ▐▌
▐▛▀▜▌▐▌   ▐▛▀▜▌▐▛▚▖     ▐▛▚▖   █  ▐▛▀▘ 
▐▌ ▐▌▝▚▄▄▖▐▌ ▐▌▐▌ ▐▌    ▐▌ ▐▌  █  ▐▌   
{Fore.RESET}""")
    print("┌─────────────────────────────────────┐")
    print("│        ACAK KTP                     │")
    print("├─────────────────────────────────────┤")
    print("│ • AUTHOR    : Tenkzz                │")
    print("└─────────────────────────────────────┘")
    print("┌─────────────────────────────────────┐")
    print("│       JOIN CHANNEL WA GWEH          │")
    print("├─────────────────────────────────────┤")
    print("│ 📱 WhatsApp Channel:                │")
    print("│    https://tinyurl.com/2cxmlqtl     │")
    print("└─────────────────────────────────────┘")
    print("┌─────────────────────────────────────┐")
    print("│           NOTE                      │")
    print("├─────────────────────────────────────┤")
    print("│ tools yg gw kasih ini ga asli, klau │")
    print("│ mau tools asli nya                  │")
    print("│ tunggu 1k pengikut nnti bersama dgn │")
    print("│ tutorial nyuri WhatsApp orang       │")
    print("│ siapa suruh main suntik², btw tools │")
    print("│ yg ini open source kok              │")
    print("│ jadi bisa Klian kembangin lagi kalau│")
    print("│ mau                                 │")
    print("└─────────────────────────────────────┘")
    
def input_table():
    print("┌─────────────────────────────────────┐")
    print("│         INPUT TARGET KTP            │")
    print("├─────────────────────────────────────┤")
    print("│ Masukkan jumlah KTP yang diinginkan │")
    print("│                                     │")
    print("└─────────────────────────────────────┘")

def create_folder():
    folder = "fufufafa"
    if not os.path.exists(folder):
        os.makedirs(folder)
        return folder
    for f in os.listdir(folder):
        os.remove(os.path.join(folder, f))
    return folder

def get_images_from_bing(query, limit=50):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    url = f"https://www.bing.com/images/search?q={query}&qft=+filterui:imagesize-large"
    
    try:
        r = requests.get(url, headers=headers, timeout=15)
        urls = re.findall(r'murl&quot;:&quot;(https?://[^&]+?\.(jpg|jpeg|png))', r.text)
        urls = [u[0].replace(r'\u002f', '/') for u in urls]
        return list(dict.fromkeys(urls))[:limit]
    except:
        return []

def download_image(url, folder, filename):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        if r.status_code == 200 and len(r.content) > 10000:
            path = os.path.join(folder, filename)
            with open(path, 'wb') as f:
                f.write(r.content)
            return True
    except:
        pass
    return False

def main():
    banner()
    input_table()
    
    try:
        target = int(input(">> "))
    except:
        print("Angka njing!")
        return
    
    folder = create_folder()
    print(f"[+] Folder: {folder}")
    
    queries = [
    # queries
    "foto KTP asli Indonesia",
    "scan e-KTP penduduk",
    "KTP elektronik asli",
    "foto KTP jelas terbaru",
    "data KTP penduduk Indonesia",
    "KTP dengan NIK terlihat",
    "scan kartu KTP",
    "gambar e-KTP full",
    "foto KTP depan belakang",
    "KTP asli tanpa sensor",
    "dokumen KTP scan",
    "KTP penduduk desa",
    "e-KTP 2024",
    "KTP baru Indonesia",
    "foto KTP kabupaten",
    "scan KTP kelurahan",
    "data kependudukan KTP",
    "KTP digital asli",
    "foto KTP kecamatan",
    "KTP warga Indonesia",
    "scan KTP asli terbaru",
    "foto e-KTP Indonesia",
    "KTP penduduk Jakarta",
    "e-KTP kabupaten Bogor",
    "data kependudukan lengkap",
    "foto KTP buat verifikasi",
    "scan KTP untuk daftar",
    "KTP asli 2025",
    "gambar KTP Indonesia",
    "NIK terlihat jelas",
    "foto KTP resolusi tinggi",
    "KTP penduduk Surabaya",
    "e-KTP kota Bandung",
    "data penduduk KTP",
    "foto KTP tanpa edit",
    "scan KTP asli 2024",
    "KTP warga desa terpencil",
    "e-KTP terbaru Indonesia",
    "foto KTP ukuran besar",
    "scan KTP untuk pendaftaran",
    "KTP asli Depok",
    "KTP elektronik 2024",
    "foto KTP penduduk kota",
    "scan KTP jelas terbaca",
    "data KTP warga negara",
    "KTP baru format lama",
    "foto e-KTP mobile",
    "scan KTP aplikasi",
    "KTP asli Tangerang",
    "e-KTP provinsi Jawa Barat",
    "foto KTP 4K",
    "scan KTP high quality",
    "KTP penduduk Bali",
    "e-KTP Sumatera Utara",
    "data KTP lengkap dengan foto",
    "foto KTP scan asli",
    "KTP warga perbatasan",
    "scan e-KTP terbaru 2024",
    "KTP Indonesia asli tanpa sensor",
    "foto KTP untuk verifikasi akun",
    "scan KTP penduduk asli",
    "data kependudukan NIK KTP",
    "e-KTP format baru",
    "foto KTP wajah jelas",
    "scan KTP full tanpa blur",
    "KTP digital 2025",
    "foto e-KTP penduduk desa",
    "scan KTP asli Indonesia gratis",
    "data KTP warga biasa",
    "KTP baru e-KTP 2024",
    "foto scan KTP asli",
    "KTP penduduk kampung",
    "e-KTP dengan NIK",
    "foto KTP asli depan",
    "scan KTP untuk daftar online",
    "KTP tanpa sensor NIK",
    "foto e-KTP penduduk kota",
    "scan KTP buat verifikasi akun",
    "data kependudukan terbaru",
    "KTP elektronik scan",
    "foto KTP asli belakang",
    "scan KTP warga negara Indonesia",
    "KTP dengan alamat lengkap",
    "e-KTP asli tanpa sensor",
    "foto KTP untuk KYC",
    "scan KTP penduduk desa terpencil",
    "data NIK KTP Indonesia",
    "KTP format baru 2024",
    "foto e-KTP resolusi tinggi",
    "scan KTP untuk verifikasi bank",
    "KTP warga asli Indonesia",
    "e-KTP terbaru 2025",
    "foto KTP untuk pendaftaran SIM",
    "scan KTP penduduk Jakarta Pusat",
    "data KTP dengan foto",
    "KTP asli Indonesia terbaru",
    "foto e-KTP full color",
    "scan KTP untuk pembuatan NPWP",
    "KTP penduduk Jawa Timur",
    "e-KTP provinsi Jawa Tengah",
    "foto KTP untuk verifikasi e-wallet",
    "scan KTP asli tanpa edit",
    "data kependudukan dukcapil",
    "KTP elektronik asli 2024",
    "foto scan KTP e-KTP",
    "scan KTP untuk daftar BPJS",
    "KTP warga negara asing",
    "e-KTP kabupaten Bekasi",
    "foto KTP untuk verifikasi pinjaman",
    "scan KTP penduduk Bandung Barat",
    "data KTP terbaru 2024",
    "KTP asli Depok 2024",
    "foto e-KTP untuk verifikasi akun game",
    "scan KTP untuk pembuatan paspor",
    "KTP penduduk Semarang",
    "e-KTP kota Malang",
    "foto KTP untuk verifikasi aplikasi dating",
    "scan KTP penduduk Medan",
    "data kependudukan kelurahan",
    "KTP elektronik scan asli",
    "foto KTP untuk verifikasi crypto",
    "scan KTP penduduk Palembang",
    "KTP warga Surabaya asli",
    "e-KTP provinsi Banten",
    "foto scan KTP untuk verifikasi kerja",
    "scan KTP penduduk Makassar",
    "data KTP dengan NIK dan alamat",
    "KTP asli Jakarta Selatan",
    "foto e-KTP untuk verifikasi sekolah",
    "scan KTP penduduk Batam",
    "KTP elektronik terbaru 2025",
    "foto KTP untuk verifikasi kontrak kerja",
    "scan KTP penduduk Pekanbaru",
    "data kependudukan kecamatan",
    "KTP asli Tangerang Selatan",
    "e-KTP kota Surakarta",
    "foto KTP untuk verifikasi asuransi",
    "scan KTP penduduk Denpasar",
    
    # DORK
    "inurl:ktp filetype:jpg",
    "inurl:e-ktp filetype:png",
    "site:disdukcapil.go.id KTP",
    "site:kpud.go.id e-KTP",
    "KTP filetype:pdf",
    "e-KTP filetype:jpg site:go.id",
    "foto KTP site:bpk.go.id",
    "scan KTP filetype:png site:sch.id",
    "NIK KTP filetype:pdf",
    "Kartu Tanda Penduduk filetype:jpg",
    "site:bps.go.id KTP",
    "site:pemda.go.id e-KTP",
    "data kependudukan filetype:xlsx",
    "NIK filetype:xls site:co.id",
    "KTP-el filetype:pdf",
    "site:drive.google.com KTP scan",
    "intitle:e-KTP inurl:pdf",
    "Nomor Induk Kependudukan filetype:pdf",
    "site:facebook.com scan KTP",
    "site:twitter.com foto KTP",
    "KTP.jpg inurl:images",
    "scan_ktp filetype:jpeg",
    "site:instagram.com KTP asli",
    "KTP dan KK filetype:pdf",
    "foto e-KTP filetype:jpeg",
    "site:whatsapp.com KTP",
    "data penduduk filetype:csv",
    "KTP blora filetype:jpg",
    "e-KTP cirebon filetype:png",
    "scan KTP depok filetype:pdf",
    "foto KTP bekasi filetype:jpeg",
    "KTP tangerang filetype:jpg",
    "e-KTP bogor filetype:png",
    "scan KTP bandung filetype:pdf",
    "KTP surabaya filetype:jpg",
    "e-KTP malang filetype:png",
    "scan KTP semarang filetype:pdf",
    "KTP yogyakarta filetype:jpg",
    "e-KTP solo filetype:png",
    "scan KTP bali filetype:pdf",
    "KTP lombok filetype:jpg",
    "e-KTP medan filetype:png",
    "scan KTP palembang filetype:pdf",
    "KTP padang filetype:jpg",
    "e-KTP pekanbaru filetype:png",
    "scan KTP banjarmasin filetype:pdf",
    "KTP makassar filetype:jpg",
    "e-KTP manado filetype:png",
    "scan KTP ambon filetype:pdf",
    "KTP papua filetype:jpg",
    "e-KTP kalimantan filetype:png",
    "scan KTP sulawesi filetype:pdf",
    "KTP sumatera filetype:jpg",
    "e-KTP jawa filetype:png",
]
    
    downloaded = 0
    
    for query in queries:
        if downloaded >= target:
            break
        
        print(f"[+] Nyari: {query}")
        urls = get_images_from_bing(query, target - downloaded)
        
        for i, url in enumerate(urls):
            if downloaded >= target:
                break
            
            filename = f"ktp_{downloaded+1:04d}.jpg"
            if download_image(url, folder, filename):
                downloaded += 1
                print(f"[✓] [{downloaded}/{target}] ktp_{downloaded:04d}.jpg")
            else:
                print(f"[✓] proses berhasil")
            
            time.sleep(random.uniform(0.3, 0.8))
    
    print(f"\n[+] SELESAI! {downloaded} gambar di folder '{folder}/'")

if __name__ == "__main__":
    main()
