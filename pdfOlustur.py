from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
import baslikOku

class PDFIslemleri:
    @staticmethod
    def pdf_olustur(klasor_yolu):
        hedef_pdf_adi = "yeni_pdf.pdf"
        doc = SimpleDocTemplate(hedef_pdf_adi, pagesize=letter)
        veri_listesi = baslikOku.PDFIslemleri.pdf_oku(klasor_yolu)

        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style.alignment = TA_CENTER
        veri = [Paragraph(paragraf, style) for paragraf in veri_listesi]

        contents = []
        contents.extend(veri)
        contents.append(Spacer(1, 12))

        doc.build(contents)

        messagebox.showinfo("Bilgi", f"{hedef_pdf_adi} adlı PDF dosyası oluşturuldu.")
