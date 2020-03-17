# ArcPy サイト パッケージをインポートします。 
import arcpy

# マップ ドキュメントのオブジェクト取得
mxd = arcpy.mapping.MapDocument("CURRENT")

# データ フレーム[0]を取得
df = arcpy.mapping.ListDataFrames(mxd)[0]

#　ページ レイアウト設定内容を PDF へ出力
arcpy.mapping.ExportToPDF(mxd, r"C:\data\output\Sample.pdf", df)

#　ページ レイアウト設定内容をワールド ファイル付きで JPEG へ出力
arcpy.mapping.ExportToJPEG(mxd, r"C:\data\output\Sample.jpg", df, 1600, 1200, 96, "TRUE")

# データ ドリブン ページで設定した内容をページとして、１ つの PDF へ出力
mxd.dataDrivenPages.exportToPDF(r"C:\data\output\SampleDrv.pdf")
