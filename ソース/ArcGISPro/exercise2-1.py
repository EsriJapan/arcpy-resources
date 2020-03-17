# ArcPy サイト パッケージをインポートします。 
import arcpy

# プロジェクト ファイルのオブジェクト取得
aprx = arcpy.mp.ArcGISProject("CURRENT")

# レイアウト[0]を取得
layout = aprx.listLayouts()[0]

#ページ レイアウト設定内容を PDF へ出力
layout.exportToPDF(r"C:\data\output\Sample.pdf")

#ページ レイアウト設定内容をJPEG へ出力
layout.exportToJPEG(r"C:\data\output\Sample.jpg")

# マップ シリーズで設定した内容をページとして、１ つの PDF へ出力
layout.mapSeries.exportToPDF(r"C:\data\output\MapSeries.pdf")

