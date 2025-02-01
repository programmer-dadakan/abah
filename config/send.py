import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

###################################################################
# Membaca User-Agent dari file
def get_random_user_agent(file_path):
    with open(file_path, "r") as f:
        user_agents = f.readlines()
    return random.choice(user_agents).strip()

###################################################################
# Membaca URL acak dari file
def get_random_url(file_path):
    with open(file_path, "r") as f:
        urls = f.readlines()
    return random.choice(urls).strip()

###################################################################
# Membaca Referer acak dari file
def get_random_referer(file_path):
    with open(file_path, "r") as f:
        referers = f.readlines()
    return random.choice(referers).strip()

###################################################################
# File konfigurasi
ua_file = "./ua-pc.txt"
url_target = "./url.txt"
referer_file = "./reff.txt"

###################################################################
# Fungsi utama untuk menjalankan proses
def run_bot():
    # Pilih User-Agent acak
    random_user_agent = get_random_user_agent(ua_file)
    print(f"User-Agent yang digunakan: {random_user_agent}\n")

    ###################################################################
    # Pilih Referer acak
    random_referer = get_random_referer(referer_file)
    print(f"Referer yang digunakan: {random_referer}\n")

    ###################################################################
    # Atur opsi Chrome dengan User-Agent acak dan menonaktifkan cache
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={random_user_agent}")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--disable-cache")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")  # Gunakan jika ingin tanpa GUI

    ###################################################################
    # Inisialisasi driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    ###################################################################
    try:
        # Set Referer menggunakan header HTTP (dengan JavaScript pada halaman)
        driver.execute_cdp_cmd(
            "Network.setExtraHTTPHeaders",
            {"headers": {"Referer": random_referer}}
        )

        ###################################################################
        # Membuka URL acak
        random_url = get_random_url(url_target)
        driver.get(random_url)
        print(f"Membuka URL: {random_url}")

        ###################################################################
        # Simulasi waktu menonton video
        play_time = random.randint(30, 50)
        print(f"Tinggal di halaman selama {play_time} detik...")
        time.sleep(play_time)

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    finally:
        # Menutup browser setelah sesi selesai
        driver.quit()
        print("Browser ditutup.")

###################################################################
# Loop dengan interval acak
while True:
    try:
        run_bot()
        # Tunggu interval 10-30 detik sebelum loop berikutnya
        interval_time = random.randint(1, 10)
        print(f"Menunggu interval {interval_time} detik sebelum menjalankan ulang...\n")
        time.sleep(interval_time)
    except KeyboardInterrupt:
        print("Program dihentikan oleh pengguna.")
        break
