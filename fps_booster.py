import os
import subprocess
import shutil
import psutil
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

# ------------------------------------
# Yardımcı Fonksiyonlar
# ------------------------------------
def log(msg):
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)

def clear_temp():
    log("→ Temp dosyaları temizleniyor...")

    temp_paths = [
        os.environ.get('TEMP'),
        os.environ.get('TMP'),
        r'C:\\Windows\\Temp'
    ]

    for p in temp_paths:
        if p and os.path.exists(p):
            for item in Path(p).iterdir():
                try:
                    if item.is_file():
                        item.unlink()
                        log(f"  Dosya silindi: {item.name}")
                    else:
                        shutil.rmtree(item, ignore_errors=True)
                        log(f"  Klasör silindi: {item.name}")
                except PermissionError:
                    log(f"  ⚠ İzin yok: {item.name}, atlandı")
                except Exception as e:
                    log(f"  ⚠ Hata: {item.name}, {e}")

    log("✓ Temp temizleme tamamlandı.")

def flush_dns():
    log("→ DNS cache temizleniyor...")
    subprocess.run(['ipconfig', '/flushdns'], check=False)
    log("✓ DNS temizlendi.")

def set_high_performance():
    log("→ Güç planı yüksek performansa alınıyor...")
    subprocess.run(['powercfg', '/S', '8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'], check=False)
    log("✓ Yüksek performans modu aktif.")

# ------------------------------------
# İşlem Önceliği Dropdown Bölümü
# ------------------------------------
def set_process_priority_dropdown():
    proc = proc_combobox.get().strip()
    level = priority_combobox.get()
    if not proc:
        messagebox.showwarning("Uyarı", "İşlem seçilmedi.")
        return

    log(f"→ {proc} işlemine {level} öncelik veriliyor...")

    priority_map = {
        "High": psutil.HIGH_PRIORITY_CLASS,
        "Above Normal": psutil.ABOVE_NORMAL_PRIORITY_CLASS,
        "Normal": psutil.NORMAL_PRIORITY_CLASS,
        "Below Normal": psutil.BELOW_NORMAL_PRIORITY_CLASS,
        "Idle": psutil.IDLE_PRIORITY_CLASS
    }

    for p in psutil.process_iter(['name','pid']):
        if p.info['name'] and p.info['name'].lower() == proc.lower():
            ps = psutil.Process(p.info['pid'])
            ps.nice(priority_map.get(level, psutil.HIGH_PRIORITY_CLASS))
            log(f"✓ {proc} önceliği {level} olarak ayarlandı.")
            return

    log(f"! {proc} bulunamadı. Oyunun açık olduğundan emin olun.")

# ------------------------------------
# Tüm FPS Boost
# ------------------------------------
def boost_all():
    clear_temp()
    flush_dns()
    set_high_performance()
    if proc_combobox.get():  # Eğer bir işlem seçildiyse öncelik ver
        set_process_priority_dropdown()
    messagebox.showinfo("Tamamlandı", "FPS artırma işlemleri tamamlandı!")

# ------------------------------------
# GUI Tasarımı (Premium + Glow + Click Animation)
# ------------------------------------
root = tk.Tk()
root.title("FPS Booster Premium")
root.geometry("520x600")
root.configure(bg="#121212")

style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox",
                fieldbackground="#1a1a1a",
                background="#1f1f1f",
                foreground="#00ff88",
                font=("Segoe UI", 10),
                bordercolor="#00ff88",
                lightcolor="#00ff88",
                darkcolor="#00ff88")

# Başlık
title = tk.Label(root,
                 text="FPS BOOSTER PREMIUM",
                 font=("Segoe UI", 18, "bold"),
                 fg="#00ff88",
                 bg="#121212")
title.pack(pady=15)

# Glow animasyonu fonksiyonu
def glow(widget, base="#00ff88", glow="#00ffbb", interval=500):
    def toggle():
        current = widget.cget("fg")
        widget.config(fg=glow if current==base else base)
        widget.after(interval, toggle)
    toggle()

glow(title, base="#00ff88", glow="#00ffbb", interval=700)

# Buton tıklama animasyonu
def click_animation(btn, click_color="#00ffbb", base_color="#1f1f1f", duration=150):
    btn.config(bg=click_color)
    btn.after(duration, lambda: btn.config(bg=base_color))

# Glow buton oluşturma fonksiyonu
def create_glow_button(text, command, interval):
    btn = tk.Button(root, text=text, bg="#1f1f1f", fg="#00ff88",
                    font=("Segoe UI", 11, "bold"),
                    activebackground="#2e2e2e", activeforeground="#00ffbb",
                    bd=0, relief="flat")
    btn.pack(pady=6, fill='x', padx=20)
    glow(btn, base="#00ff88", glow="#00ffbb", interval=interval)
    # Buton tıklama animasyonunu komut ile birleştir
    def combined_command():
        click_animation(btn)
        command()
    btn.config(command=combined_command)
    return btn

btn1 = create_glow_button("🧹 Temp Temizle", clear_temp, 600)
btn2 = create_glow_button("🌐 DNS Cache Temizle", flush_dns, 650)
btn3 = create_glow_button("⚡ Yüksek Performans Modu", set_high_performance, 700)
btn4 = create_glow_button("🚀 İşlem Önceliğini Yükselt", set_process_priority_dropdown, 750)
btn5 = create_glow_button("🔥 TÜM FPS BOOST Ayarlarını Uygula", boost_all, 800)

# İşlem Önceliği Bölümü
proc_frame = tk.Frame(root, bg="#121212")
proc_frame.pack(pady=12, padx=20, fill='x')

proc_label = tk.Label(proc_frame, text="Öncelik Verilecek İşlem Seç:", fg="#00ff88", bg="#121212", font=("Segoe UI", 10, "bold"))
proc_label.grid(row=0, column=0, padx=5, pady=2, sticky="w")

process_list = sorted(list({p.info['name'] for p in psutil.process_iter(['name']) if p.info['name']}))
proc_combobox = ttk.Combobox(proc_frame, values=process_list, width=30, state="readonly")
proc_combobox.grid(row=0, column=1, padx=5, pady=2, sticky="ew")

priority_label = tk.Label(proc_frame, text="Öncelik Seviyesi:", fg="#00ff88", bg="#121212", font=("Segoe UI", 10, "bold"))
priority_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

priority_levels = ["High", "Above Normal", "Normal", "Below Normal", "Idle"]
priority_combobox = ttk.Combobox(proc_frame, values=priority_levels, width=15, state="readonly")
priority_combobox.current(0)
priority_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Log ekranı (Glow + Neon Scrollbar)
log_frame = tk.Frame(root, bg="#121212")
log_frame.pack(fill="both", padx=15, pady=12, expand=True)

log_box = tk.Text(log_frame,
                  height=15,
                  bg="#1a1a1a",
                  fg="#00ff88",
                  font=("Consolas", 10),
                  borderwidth=2,
                  relief="sunken",
                  insertbackground="#00ff88")
log_box.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(log_frame, command=log_box.yview,
                         bg="#1a1a1a", activebackground="#00ff88",
                         troughcolor="#121212", width=12)
scrollbar.pack(side="right", fill="y")
log_box.config(yscrollcommand=scrollbar.set)

def glow_log(widget, base="#00ff88", glow="#00ffbb", interval=500):
    def toggle():
        current = widget.cget("fg")
        widget.config(fg=glow if current==base else base)
        widget.after(interval, toggle)
    toggle()

glow_log(log_box, base="#00ff88", glow="#00ffbb", interval=700)

root.mainloop()