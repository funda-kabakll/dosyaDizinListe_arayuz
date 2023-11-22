import os
from tkinter import filedialog

class PDFIslemleri:
    @staticmethod
    def klasor_oku():
        klasor_adi = filedialog.askdirectory(title="Klasör Seç")
        nedir_bu = [dosya for dosya in os.listdir(klasor_adi) if dosya.endswith('.pdf')]

        for dosyalar in nedir_bu:
            print(dosyalar)
