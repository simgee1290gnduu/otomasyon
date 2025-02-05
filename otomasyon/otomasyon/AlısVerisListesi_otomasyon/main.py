import json
from datetime import datetime

# Mevcut stoklar
stoklar = {
    "süt": 2,
    "yumurta": 10,
    "ekmek": 1,
    "elma": 5
}

# Günlük ihtiyaçlar
ihtiyaclar = {
    "süt": 3,
    "yumurta": 12,
    "ekmek": 2,
    "elma": 6
}

def stok_guncelle():
    print("Stok güncellemesi")
    for urun in stoklar.keys():
        yeni_stok = input(f"{urun} için yeni stok miktarını girin (mevcut: {stoklar[urun]}): ")
        if yeni_stok.isdigit():
            stoklar[urun] = int(yeni_stok)

def alisveris_listesi_olustur():
    eksikler = {}
    for urun, miktar in ihtiyaclar.items():
        if stoklar.get(urun, 0) < miktar:
            eksikler[urun] = miktar - stoklar.get(urun, 0)

    tarih = datetime.now().strftime('%Y-%m-%d')
    dosya_adi = f'alisveris_listesi_{tarih}.json'
    with open(dosya_adi, 'w') as file:
        json.dump(eksikler, file)

    print(f"Alışveriş listesi oluşturuldu: {dosya_adi}")

def menu():
    print("1. Stokları Güncelle")
    print("2. Alışveriş Listesi Oluştur")
    print("3. Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == '1':
        stok_guncelle()
    elif secim == '2':
        alisveris_listesi_olustur()
    elif secim == '3':
        print("Çıkış yapılıyor.")
        exit()
    else:
        print("Geçersiz seçim.")

if __name__ == "__main__":
    while True:
        menu()
