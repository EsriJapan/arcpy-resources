# ArcPy サイト パッケージをインポートします。 
import arcpy
# プロジェクト ファイルのオブジェクト取得
aprx = arcpy.mp.ArcGISProject("current")
# マップのオブジェクト取得
maps = aprx.listMaps()[0]
# レイヤーのオブジェクト取得
lyrs =maps.ｌistLayers()

for lyr in lyrs:
     # レイヤーの表示設定
     lyr.visible = True
