from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import klasorOku
import baslikOku
import pdfOlustur

def klasor_oku():
    klasorOku.PDFIslemleri.klasor_oku()

def pdf_oku():
    klasor_yolu = filedialog.askdirectory(title="Klasör Seç")
    basliklar = baslikOku.PDFIslemleri.pdf_oku(klasor_yolu)
    for baslik in basliklar:
        print(baslik)

def pdf_olustur():
    klasor_yolu = filedialog.askdirectory(title="Klasör Seç")
    pdfOlustur.PDFIslemleri.pdf_olustur(klasor_yolu)

pencere = Tk()
pencere.title("PDF İşlemleri")
pencere.geometry("300x200")

menuOgeleri = ["Pdf adlarını listele", "Pdf başlıklarını oku", "Başlıklardan yeni pdf oluştur", "Çıkış"]
menuFonksiyonlari = [klasor_oku, pdf_oku, pdf_olustur, quit]

for idx, oge in enumerate(menuOgeleri):
    ttk.Button(pencere, text=oge, command=menuFonksiyonlari[idx]).pack()

pencere.mainloop()

