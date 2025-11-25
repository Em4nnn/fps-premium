import subprocess
import sys

# Gerekli kütüphaneler
required = ["psutil"]

for package in required:
    try:
        __import__(package)
        print(f"[✓] {package} yüklü")
    except ImportError:
        print(f"[!] {package} eksik, yükleniyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"[✓] {package} yüklendi!")

print("\n[Tamamlandı] Tüm kütüphaneler hazır! Artık FPS Booster'ı çalıştırabilirsin.")
