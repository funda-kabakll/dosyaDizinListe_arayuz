import os
from pdfminer.high_level import extract_text

class PDFIslemleri:
    @staticmethod
    def pdf_oku(klasor_yolu):
        pdf_dosyalar = [dosya for dosya in os.listdir(klasor_yolu) if dosya.endswith('.pdf')]

        basliklar = []

        for pdf_dosya in pdf_dosyalar:
            pdf_yol = os.path.join(klasor_yolu, pdf_dosya)
            metin = extract_text(pdf_yol, page_numbers=[0])

            satirlar = metin.split('\n')
            ilk_sayfa_baslik = None

            for satir in satirlar:
                if "-" in satir or "(" in satir or "/" in satir:
                    continue
                if satir.strip():
                    ilk_sayfa_baslik = satir
                    break

            if ilk_sayfa_baslik:
                basliklar.append(f"PDF Başlığı ({pdf_dosya}):\n{ilk_sayfa_baslik}\n")
            else:
                basliklar.append(f"{pdf_dosya} Başlık bulunamadı\n\n")

        return basliklar
