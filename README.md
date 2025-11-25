"""
------------------------------------------------------------
FPS BOOSTER PREMIUM - Python Script
------------------------------------------------------------

**- Sahte Yada Virüslü yazlılım değildir!**
  
Bu program, Windows üzerinde oyun performansını artırmak için tasarlanmıştır.
GUI tabanlıdır ve kullanıcıya aşağıdaki FPS artırma özelliklerini sunar:

Özellikler:
1. Temp Dosyalarını Temizleme
   - Windows geçici dosyalarını temizler (TEMP, TMP ve C:\Windows\Temp)
   - Disk performansını artırır

2. DNS Cache Temizleme
   - ipconfig /flushdns komutu ile DNS önbelleğini temizler
   - Ağ gecikmesini azaltabilir

3. Yüksek Performans Modu
   - Windows güç planını "High Performance" olarak ayarlar
   - CPU/GPU performansını maksimum seviyeye çıkarır

4. İşlem Önceliği Yönetimi
   - Seçilen işlem/oyun için öncelik seviyesini değiştirebilirsiniz
     (High, Above Normal, Normal, Below Normal, Idle)
   - Oyun sırasında CPU önceliğini artırarak FPS stabilitesini yükseltir

5. Tüm Ayarları Tek Tuşla Uygulama
   - Temp temizleme, DNS flush ve yüksek performans modunu birden uygular
   - Seçili işlem varsa öncelik de otomatik yükseltilir

6. Premium Görünüm
   - Neon yeşil log ekranı
   - Glow efektli butonlar
   - Özel neon scrollbar

Kullanım:
- Python 3.10+ ile çalışır.
- Gerekli kütüphaneler: psutil (pip install psutil)
- GUI üzerinden tüm işlemler kolayca uygulanabilir.

Notlar:
- Bu yazılım oyun performansını artırmak içindir, sistem dosyalarına zarar vermez.
- Yönetici yetkisi gerektirebilir (özellikle temp temizleme ve güç planı değiştirme için).
