import PyPDF2
import os


def pdf_birlestir_sikistir(dizin):
    # Tüm PDF dosyalarını listele
    pdf_listesi = [dosya for dosya in os.listdir(dizin) if dosya.endswith('.pdf')]

    if len(pdf_listesi) < 2:
        print("Birleştirme için en az 2 PDF dosyası gereklidir.")
        return

    # PDF birleştirme
    birlesik_pdf = PyPDF2.PdfFileMerger()
    for pdf in pdf_listesi:
        pdf_yol = os.path.join(dizin, pdf)
        birlesik_pdf.append(pdf_yol)

    # Birleştirilmiş PDF dosyasını oluştur
    birlesik_pdf_yolu = os.path.join(dizin, 'birlesik_pdf.pdf')
    with open(birlesik_pdf_yolu, 'wb') as dosya:
        birlesik_pdf.write(dosya)

    print(f"Birleştirilmiş PDF oluşturuldu: {birlesik_pdf_yolu}")

    # PDF sıkıştırma (isteğe bağlı olarak)
    # Sıkıştırma işlemi için ekstra bir kütüphane veya araç kullanılabilir


if __name__ == "__main__":
    dizin = input("PDF dosyalarının bulunduğu dizini girin: ")

    if os.path.isdir(dizin):
        pdf_birlestir_sikistir(dizin)
    else:
        print("Geçersiz dizin yolu.")
