# ArcPy サイト パッケージをインポートします。
import arcpy
import os

# 作成するファイル名を設定　※すでに存在した場合は削除する
pdfPath = r"C:\data\output\MapBook.pdf"
if os.path.exists(pdfPath):
    os.remove(pdfPath)

# PDF ファイルを作成し、ページをマージする
pdfDoc = arcpy.mp.PDFDocumentCreate(pdfPath)
pdfDoc.appendPages(r"C:\data\output\title.pdf")
pdfDoc.appendPages(r"C:\data\output\MapSeries.pdf")

# PDF ファイルの変更を保存して、オブジェクトを削除する
pdfDoc.saveAndClose()
del pdfDoc

