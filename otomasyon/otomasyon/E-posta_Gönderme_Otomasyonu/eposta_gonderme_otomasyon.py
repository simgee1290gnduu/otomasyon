import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def email_gonder(gonderen, sifre, alici, konu, icerik):
    try:
        # E-posta sunucusuna bağlan
        mail_server = smtplib.SMTP('smtp.gmail.com', 587)
        mail_server.starttls()  # TLS (Transport Layer Security) bağlantısı başlat

        # Giriş yap
        mail_server.login(gonderen, sifre)

        # E-posta mesajı oluştur
        mesaj = MIMEMultipart()
        mesaj['From'] = gonderen
        mesaj['To'] = alici
        mesaj['Subject'] = konu

        # E-posta içeriği eklenir
        mesaj.attach(MIMEText(icerik, 'plain'))

        # E-postayı gönder
        mail_server.send_message(mesaj)

        # Bağlantıyı kapat
        mail_server.quit()

        print(f"E-posta başarıyla gönderildi: {alici}")

    except Exception as e:
        print(f"Hata oluştu: {e}")


if __name__ == "__main__":
    gonderen = input("Gönderen e-posta adresini girin: ")
    sifre = input("Gönderen e-posta şifresini girin: ")
    alici = input("Alıcı e-posta adresini girin: ")
    konu = input("E-posta konusunu girin: ")
    icerik = input("E-posta içeriğini girin: ")

    email_gonder(gonderen, sifre, alici, konu, icerik)
