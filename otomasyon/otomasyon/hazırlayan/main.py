import tkinter as tk
import time

def show_info():
    isim = "SİMGE GÜNDOĞDU"
    okul_numarasi = "21430070022"

    info_label.config(text=f"İsim: {isim}\nOkul Numarası: {okul_numarasi}")

    # Renk değişimi efekti
    info_label.config(fg="blue", bg="yellow")

    # Yazı büyüklüğü değişimi efekti
    info_label.config(font=("Helvetica", 14, "bold"))

    # Buton rengi ve yazı rengi değişimi efekti
    show_button.config(fg="white", bg="green", activeforeground="white", activebackground="darkgreen")

    # Buton boyut değişimi efekti
    show_button.config(width=15, height=2)

# Pencere oluşturma
root = tk.Tk()
root.title("Bilgi Gösterme Uygulaması")
root.geometry("300x200")

# Bilgi gösterme etiketi
info_label = tk.Label(root, text="", font=("Arial", 12))
info_label.pack(pady=20)

# Bilgileri gösterme düğmesi
show_button = tk.Button(root, text="Bilgileri Göster", command=show_info, bg="blue", fg="white", font=("Arial", 10, "bold"))
show_button.pack()

# Uygulamayı çalıştırma
root.mainloop()
