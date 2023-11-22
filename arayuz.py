from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import klasorOku
import baslikOku
import pdfOlustur

class Arayuz:
    def __init__(self, ana_pencere):
        self.ana_pencere = ana_pencere
        self.ana_pencere.title("PDF İşlemleri")
        self.ana_pencere.geometry("300x200")

        self.menu_ogeleri = ["Pdf adlarını listele", "Pdf başlıklarını oku", "Başlıklardan yeni pdf oluştur", "Çıkış"]
        self.menu_fonksiyonlari = [self.klasor_oku, self.pdf_oku, self.pdf_olustur, quit]

        for idx, oge in enumerate(self.menu_ogeleri):
            ttk.Button(self.ana_pencere, text=oge, command=self.menu_fonksiyonlari[idx]).pack()

    def klasor_oku(self):
        klasorOku.PDFIslemleri.klasor_oku()

    def pdf_oku(self):
        klasor_yolu = filedialog.askdirectory(title="Klasör Seç")
        basliklar = baslikOku.PDFIslemleri.pdf_oku(klasor_yolu)
        for baslik in basliklar:
            print(baslik)

    def pdf_olustur(self):
        klasor_yolu = filedialog.askdirectory(title="Klasör Seç")
        pdfOlustur.PDFIslemleri.pdf_olustur(klasor_yolu)


if __name__ == "__main__":
    pencere = Tk()
    arayuz = Arayuz(pencere)
    pencere.mainloop()
