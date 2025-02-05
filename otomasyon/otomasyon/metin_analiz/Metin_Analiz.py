import os
import string


def metin_istatistikleri_hesapla(dosya_yolu):
    # Metin dosyasını oku
    try:
        with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
            metin = dosya.read()
    except FileNotFoundError:
        print(f"{dosya_yolu} bulunamadı.")
        return

    # Karakter sayısı hesaplama
    karakter_sayisi = len(metin)

    # Kelime sayısı hesaplama
    kelimeler = metin.split()
    kelime_sayisi = len(kelimeler)

    # Cümle sayısı hesaplama (nokta, ünlem, soru işareti ile bitenler)
    cümle_ayrac = ".!?\\n"
    cümleler = [cümle.strip() for cümle in metin.splitlines() if cümle.strip()]
    cümle_sayisi = sum([cümle.count(c) for cümle in cümleler for c in cümle_ayrac])

    # İstatistikleri ekrana yazdır
    print(f"Karakter Sayısı: {karakter_sayisi}")
    print(f"Kelime Sayısı: {kelime_sayisi}")
    print(f"Cümle Sayısı: {cümle_sayisi}")


if __name__ == "__main__":
    dosya_yolu = input("Analiz edilecek metin dosyasının yolunu girin: ")

    if os.path.isfile(dosya_yolu):
        metin_istatistikleri_hesapla(dosya_yolu)
    else:
        print("Geçersiz dosya yolu.")
