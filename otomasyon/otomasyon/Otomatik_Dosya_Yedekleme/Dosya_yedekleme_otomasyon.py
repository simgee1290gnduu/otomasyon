import shutil
import os
import time


def dosya_yedekle(dizin, hedef_dizin):
    # Yedekleme tarihini al
    yedek_tarih = time.strftime('%Y-%m-%d_%H-%M-%S')
    yedek_dizin = os.path.join(hedef_dizin, f'yedek_{yedek_tarih}')

    try:
        # Hedef yedek dizinini oluştur
        os.makedirs(yedek_dizin)

        # Dizindeki tüm dosyaları yedekle
        for dosya in os.listdir(dizin):
            dosya_yolu = os.path.join(dizin, dosya)
            if os.path.isfile(dosya_yolu):
                shutil.copy2(dosya_yolu, yedek_dizin)
                print(f"{dosya} yedeklendi.")

        print(f"Yedekleme tamamlandı: {yedek_dizin}")
    except Exception as e:
        print(f"Hata oluştu: {e}")


if __name__ == "__main__":
    kaynak_dizin = input("Yedeklenecek dosyaların bulunduğu dizini girin: ")
    hedef_dizin = input("Yedeklerin kaydedileceği dizini girin: ")

    if os.path.isdir(kaynak_dizin) and os.path.isdir(hedef_dizin):
        dosya_yedekle(kaynak_dizin, hedef_dizin)
    else:
        print("Geçersiz dizin yolu.")
