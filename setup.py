import subprocess
import sys
import os

# ----------------------------------
# Gerekli kütüphaneler listesi
# ----------------------------------
required = ["psutil"]

print("🚀 FPS Booster Kurulum Başlatıldı...\n")

for package in required:
    try:
        __import__(package)
        print(f"[✓] {package} yüklü")
    except ImportError:
        print(f"[!] {package} eksik, yükleniyor...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"[✓] {package} yüklendi!")
        except subprocess.CalledProcessError:
            print(f"[✗] {package} yüklenemedi! Lütfen manuel kurulum yap.")

# ----------------------------------
# Kullanıcıya bilgi
# ----------------------------------
print("\n[Tamamlandı] Tüm kütüphaneler hazır!")

# FPS Booster dosyası aynı klasörde mi kontrol edelim
fps_booster_file = "fps_booster.py"
if os.path.exists(fps_booster_file):
    print(f"💻 Artık {fps_booster_file} dosyasını çalıştırabilirsin!")
else:
    print(f"⚠ Dikkat: {fps_booster_file} bulunamadı. Lütfen aynı klasöre koy.")
